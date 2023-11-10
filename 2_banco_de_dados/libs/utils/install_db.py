'''
Estou configurando o banco de dados para o supervisorio offline.

No entanto, quando eu executo o supervisorio no cMTViewer, ele não consegue se conectar com o banco de dados.
Mas quando se conecto pelo Easybuilder, eu consigo me conectar com o banco de dados pelo'''

'''
Passo a passo para instalar o banco de dados e configurar o supervisorio offline.


1 - Instalar o banco de dados o wampserver
    1.1 - Baixar o wampserver
    1.2 - Instalar o wampserver com o MariaDB 10.4.8
    1.3 - Iniciar o wampserver

2 - Configurar o banco de dados
    2.1 - Abrir o phpmyadmin
    2.2 - Criar um banco de dados (engesepdb)
            CREATE DATABASE engesepdb;
    2.3 - Criar um usuario com todos os privilégios
            username: paraisoto
            password: 654123

3 - Configurar o supervisorio
    3.1 - Abrir o supervisorio
    3.2 - Configurar a conexão com o banco de dados
        3.2.1 - Configurações de conexão
            host: localhost
            port: 3306
            username: paraisoto
            password: 654123@engesep
            database: engesepdb
        3.2.2 - Configurações de controle e operações para Macro
            'parisoto local': {
            'status': {
                'address': 'LW-400',
                '0': 'parado',
                '1': 'desconectado',
                '2': 'conectado',
            },
            'Error': {
                'address': 'LW-401',
                '0': 'sem erro',
                '1': 'erro'
            },
            'Control': {
                'address': 'LW-410',
                '0': 'None',
                '1': 'Start',
                '2': 'Stop',
                '3': 'update',
            },
            'Reserved': {
                'address': 'LW-411',
            },
            'Port': {
                'address': 'LW-415',
            },
            'Username': {
                'address': 'LW-416',
            },
            'Password': {
                'address': 'LW-432',
            },
            'Database Name': {
                'address': 'LW-448',
            },
            'Domain name': {
                'address': 'LW-464',
            },
        3.2.3 - Configurações de inserção de dados
            'Consulta sql local': {
                'Command ID': 'LW-300',
                'Row select': 'LW-301',
                'Row status': 'LW-302',
                'Error code': 'LW-303',
                'Error message': 'LW-304',
            },
    3.3 - Criar comando SQL com o arquivo create_table.sql, que está na pasta libs\utils\create_table.sql
        3.1 -

'''