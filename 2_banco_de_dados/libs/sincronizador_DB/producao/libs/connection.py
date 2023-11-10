'''
 Class Connection - Classe de conexão com o banco de dados.
'''
import mysql.connector
import pandas as pd
import subprocess
import os


class DatabaseManager:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        try:
            print(f"Connecting to database {self.database}...")
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            print(f"Connected to database {self.database}.")
        except mysql.connector.Error as err:
            print(f"Failed to connect to database: {err}")
            raise Exception(f"Falha na conexão do banco de dados: {err}")

    def read_data(self, table_name):
        try:
            df = pd.read_sql(f'SELECT * FROM {table_name}', self.connection)
            return df
        except mysql.connector.Error as err:
            print(f"Failed to read data: {err}")
            raise
    def read_where(self, table_name, where):
        try:
            # print(f"Reading data from {table_name}...")
            # print(f"SELECT * FROM {table_name} WHERE id <= {where}")
            # print(self.connection)
            df = pd.read_sql(f'SELECT * FROM {table_name} WHERE id < {where}', self.connection)
            return df
        except mysql.connector.Error as err:
            print(f"Failed to read data: {err}")
            raise

    def close(self):
        if self.connection:
            self.connection.close()

    def create_table(self, table_name, columns):
        cursor = self.connection.cursor()
        query = f"CREATE TABLE {table_name} ("
        query += ", ".join([f"{name} {data_type}" for name, data_type in columns.items()])
        query += ")"
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Failed to create table: {err}")
            raise
    def insert_sincronizacao(self, table_name, values):
        # values = ', '.join('%s' for _ in columns)
        # columns = ', '.join(columns)
        cursor = self.connection.cursor()
        query = f"INSERT INTO `{table_name}` (`id_sincronizado`, `qtd_registros_sincronizados`) VALUES {values};"
        print(query)
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Failed to insert data: {err}")
            raise
        self.connection.commit()

    def las_index(self, table_name):
        cursor = self.connection.cursor()
        query = f"SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1"
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Failed to get last index: {err}")
            raise
        last_index = cursor.fetchall()
        return last_index
    def delete_data(self, table_name):
        cursor = self.connection.cursor()
        query = f"DELETE FROM {table_name}"
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Failed to delete data: {err}")
            raise
        self.connection.commit()
    def insert_data(self, table, columns, values_list, batch_size=500):
        columns_str = ', '.join(columns)
        placeholders = ', '.join('%s' for _ in columns)
        query = f'INSERT INTO {table} ({columns_str}) VALUES ({placeholders})'

        cursor = self.connection.cursor()

        errors = []
        for i in range(0, len(values_list), batch_size):
            batch_values = values_list[i:i+batch_size]
            try:
                cursor.executemany(query, batch_values)
                self.connection.commit()
                print(f"Inserted {len(batch_values)} rows of data.")
            except mysql.connector.Error as err:
                self.connection.rollback()
                errors.append(err)
                print(f"Failed to insert batch starting at index {i}: {err}")

        cursor.close()

        if errors:
            for err in errors:
                print(err)
            raise Exception("Errors occurred during insertion. See logs for details.")

    def insert_data_from_csv(self, table_name, csv_path):
        df = pd.read_csv(csv_path)
        data = df.values.tolist()
        self.insert_data(table_name, data)

    def update_data(self, table_name, set_columns, condition):
        cursor = self.connection.cursor()
        query = f"UPDATE {table_name} SET "
        query += ", ".join([f"{column} = %s" for column in set_columns.keys()])
        query += f" WHERE {condition}"
        try:
            cursor.execute(query, tuple(set_columns.values()))
        except mysql.connector.Error as err:
            print(f"Failed to update data: {err}")
            raise
        self.connection.commit()

    def get_columns(self, table_name):
        cursor = self.connection.cursor()
        query = f"SHOW COLUMNS FROM {table_name}"
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Failed to get columns: {err}")
            raise
        columns = cursor.fetchall()
        return columns
    def reverse_rename(self, abbr):
        try:
            mapping = {
                '101s': 'ug01_status',
                '201ae': 'ug01_acumulador_energia',
                '301na': 'ug01_nivel_agua',
                '401tfA': 'ug01_tensao_fase_A',
                '501tfB': 'ug01_tensao_fase_B',
                '601tfC': 'ug01_tensao_fase_C',
                '701cfA': 'ug01_corrente_fase_A',
                '801cfB': 'ug01_corrente_fase_B',
                '901cfC': 'ug01_corrente_fase_C',
                '1001te': 'ug01_tensao_excitacao',
                '1101ce': 'ug01_corrente_excitacao',
                '1201f': 'ug01_frequencia',
                '1301pa': 'ug01_potencia_ativa',
                '1401pr': 'ug01_potencia_reativa',
                '1501pa': 'ug01_potencia_aparente',
                '1601f': 'ug01_fp',
                '1701d': 'ug01_distribuidor',
                '1801v': 'ug01_velocidade',
                '1901hm': 'ug01_horimetro_mecanico',
                '2001he': 'ug01_horimetro_eletrico',
                '2101teA': 'ug01_temp_enrol_A',
                '2201teB': 'ug01_temp_enrol_B',
                '2301teC': 'ug01_temp_enrol_C',
                '2401tme': 'ug01_temp_mancal_estat',
                '2501tmc': 'ug01_temp_mancal_comb',
                '2601tme': 'ug01_temp_mancal_escora',
                '2701tou': 'ug01_temp_oleo_uhrv',
                '2801tou': 'ug01_temp_oleo_uhlm',
                '2901tc': 'ug01_temp_csu2',
                '3001te': 'ug01_temp_excitatriz',
                '3101vmgx': 'ug01_vibr_mancal_guia_x',
                '3201vmgY': 'ug01_vibr_mancal_guia_Y',
                '3301vmcX': 'ug01_vibr_mancal_comb_X',
                '3401vmcY': 'ug01_vibr_mancal_comb_Y',
                '3501vmcZ': 'ug01_vibr_mancal_comb_Z',
                '3601clA': 'ug01_corrente_linha_A',
                '3701clB': 'ug01_corrente_linha_B',
                '3801clC': 'ug01_corrente_linha_C',
                '3901csP': 'ug01_corrente_seq_P',
                '4001csN': 'ug01_corrente_seq_N',
                '4101csZ': 'ug01_corrente_seq_Z',
                '4201tb': 'ug01_tensao_barra',
                '4301tt': 'ug01_tensao_te',
                '4402s': 'ug02_status',
                '4502ae': 'ug02_acumulador_energia',
                '4602tfA': 'ug02_tensao_fase_A',
                '4702tfB': 'ug02_tensao_fase_B',
                '4802tfC': 'ug02_tensao_fase_C',
                '4902cfA': 'ug02_corrente_fase_A',
                '5002cfB': 'ug02_corrente_fase_B',
                '5102cfC': 'ug02_corrente_fase_C',
                '5202te': 'ug02_tensao_excitacao',
                '5302ce': 'ug02_corrente_excitacao',
                '5402f': 'ug02_frequencia',
                '5502pa': 'ug02_potencia_ativa',
                '5602pr': 'ug02_potencia_reativa',
                '5702pa': 'ug02_potencia_aparente',
                '5802f': 'ug02_fp',
                '5902d': 'ug02_distribuidor',
                '6002v': 'ug02_velocidade',
                '6102hm': 'ug02_horimetro_mecanico',
                '6202he': 'ug02_horimetro_eletrico',
                '6302teA': 'ug02_temp_enrol_A',
                '6402teB': 'ug02_temp_enrol_B',
                '6502teC': 'ug02_temp_enrol_C',
                '6602tme': 'ug02_temp_mancal_estat',
                '6702tmc': 'ug02_temp_mancal_comb',
                '6802tme': 'ug02_temp_mancal_escora',
                '6902tou': 'ug02_temp_oleo_uhrv',
                '7002tou': 'ug02_temp_oleo_uhlm',
                '7102tc': 'ug02_temp_csu2',
                '7202te': 'ug02_temp_excitatriz',
                '7302vmgx': 'ug02_vibr_mancal_guia_x',
                '7402vmgY': 'ug02_vibr_mancal_guia_Y',
                '7502vmcX': 'ug02_vibr_mancal_comb_X',
                '7602vmcY': 'ug02_vibr_mancal_comb_Y',
                '7702vmcZ': 'ug02_vibr_mancal_comb_Z',
            }
            valor = mapping.get(abbr, None)
            return valor
        except Exception as e:
            raise Exception(f"Falha na decodificacao do nome da tabela: {e}")

# def main():
#     railway_connect()
#
#     with DatabaseManager(host=os.getenv('RAILWAY_HOST'),
#                          user=os.getenv('RAILWAY_USER'),
#                          password=os.getenv('RAILWAY_PASSWORD'),
#                          database=os.getenv('RAILWAY_DATABASE')) as db_manager:
#
#         # Exemplo de criação de tabela
#         db_manager.create_table('TestTable', {'id': 'INT', 'name': 'VARCHAR(255)'})
#
#         # Exemplo de inserção de dados
#         db_manager.insert_data('TestTable', [(1, 'John Doe'), (2, 'Jane Doe')])
#
#         # Exemplo de inserção de dados a partir de um arquivo .csv
#         db_manager.insert_data_from_csv('TestTable', 'data.csv')
#
#         # Exemplo de leitura de dados
#         data = db_manager.read_data('TestTable')
#         print(data)
#
#         # Exemplo de atualização de dados
#         db_manager.update_data('TestTable', {'name': 'John Smith'}, "id = 1")
#
#         # Exemplo de exclusão de dados
#         db_manager.delete_data('TestTable', "id = 2")
#
# if __name__ == "__main__":
#     main()
