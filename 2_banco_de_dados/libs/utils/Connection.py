
'''
 Class Connection - Classe de conexão com o banco de dados.
'''
import mysql.connector
import pandas as pd
import subprocess
import os

class DatabaseManager:
    def __init__(self, host, user, password, database, port=3306):
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
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
        except mysql.connector.Error as err:
            print(f"Failed to connect to database: {err}")
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

    def insert_data(self, table, columns, values_list):
        columns_str = ', '.join(columns) # 'usina, valores'
        placeholders = ', '.join('%s' for _ in columns) # '%s, %s'
        query = f'INSERT INTO {table} ({columns_str}) VALUES ({placeholders})'
        print(query)
        cursor = self.connection.cursor()
        for row in values_list:
            try:
                cursor.execute(query, row)
            except mysql.connector.Error as err:
                print(f"Failed to insert data: {err}")
                raise
            self.connection.commit()
            print(f"Inserted {cursor.rowcount} rows of data.")
    def insert_data_from_csv(self, table_name, csv_path):
        df = pd.read_csv(csv_path)
        data = df.values.tolist()
        self.insert_data(table_name, data)

    def read_data(self, table_name):
        try:
            df = pd.read_sql(f'SELECT * FROM {table_name}', self.connection)
            return df
        except mysql.connector.Error as err:
            print(f"Failed to read data: {err}")
            raise

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

def railway_connect():
    try:
        subprocess.run(["railway", "connect"], shell=True, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Failed to connect to Railway: {err}")
        raise

def main():
    railway_connect()

    with DatabaseManager(host=os.getenv('RAILWAY_HOST'),
                         user=os.getenv('RAILWAY_USER'),
                         password=os.getenv('RAILWAY_PASSWORD'),
                         database=os.getenv('RAILWAY_DATABASE')) as db_manager:

        # Exemplo de criação de tabela
        db_manager.create_table('TestTable', {'id': 'INT', 'name': 'VARCHAR(255)'})

        # Exemplo de inserção de dados
        db_manager.insert_data('TestTable', [(1, 'John Doe'), (2, 'Jane Doe')])

        # Exemplo de inserção de dados a partir de um arquivo .csv
        db_manager.insert_data_from_csv('TestTable', 'data.csv')

        # Exemplo de leitura de dados
        data = db_manager.read_data('TestTable')
        print(data)

        # Exemplo de atualização de dados
        db_manager.update_data('TestTable', {'name': 'John Smith'}, "id = 1")

        # Exemplo de exclusão de dados
        db_manager.delete_data('TestTable', "id = 2")

if __name__ == "__main__":
    main()
