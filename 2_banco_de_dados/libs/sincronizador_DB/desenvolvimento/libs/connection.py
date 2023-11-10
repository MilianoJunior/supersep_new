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
            print(f"Reading data from {table_name}...")
            print(f"SELECT * FROM {table_name} WHERE id >= {where}")
            print(self.connection)
            df = pd.read_sql(f'SELECT * FROM {table_name} WHERE id > {where}', self.connection)
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

    def delete_data(self, table_name, condition):
        cursor = self.connection.cursor()
        query = f"DELETE FROM {table_name} WHERE {condition}"
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Failed to delete data: {err}")
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
