'''
Interface que gerência todos os banco de dados.

Funções:
    - Criar tabelas
    - Inserir dados
    - Atualizar dados
    - Deletar dados
    - Consultar dados
    - Consultar todas informações sobre todas tabelas existentes
    - Consultar a integradade dos dados de uma tabela
    - Retornar relatório de erros de integridade
    - Retornar relatório das ultimas persistências feitas no banco de dados

Estrutura:
    - Classe principal : Main
    - Classe de conexão com o banco de dados : libs.utils.Connection
Par654123@
'''

# Importações
from libs.utils.Connection import DatabaseManager
from libs.utils.imprimir import pr
from libs.utils.var_conexoes import conexoes, supervisorio
from libs.utils.modelo_sql import criar_modelo
import importlib

'''
Banco de dados OFFLINE

Passo 1: WampServer
    - Instalar WampServer com MariaDB e Mysql 5.4;
    - Alterar configurações do Apache, no arquivo http.conf para; 
            - Alterar configurações de compartilhamento de pastas do wampserver;
            - Require local -> Require all granted
            - Verificar se porta 80, não está sendo usada, se sim, alterar.
    - Acrescentar a linha configurações do Mysql, no arquivo bin/mysql/my.cnf;
            - bind-address = 0.0.0.0
    - Configurar MariaDB como banco principal;
    - Reiniciar o WampServer e testar;

Passo 2: Exceção de porta no Firewall
    - Digitar no menu iniciar: Firewall -> configurações avançadas;
    - Adicionar Regra de entrada e saida de execeção para a porta 3306 porta;

Passo 3: Criar banco de dados, usuario e tabela para usina.
    - criar configurar os dados e executar os passos abaixo:
            - [executar main.py], antes:
                - alterar o nome da usina na variavel nome_usina;
                - definir o numero de turbinas na variavel numero_turbinas;
    - criar banco de dados:
    - criar o usuario:
    - configurar as entradas da tabela na pasta libs/usinas;

'''
usinas = {
    '1': {
        'nome': 'cgh_maria_da_luz',
        'numero_turbinas': 1,
        'estado': 'Finalizado.',
    },
    '2': {
        'nome': 'cgh_fae',
        'numero_turbinas': 2,
        'estado': 'Finalizado.',
    },
    '3': {
        'nome': 'cgh_parisoto',
        'numero_turbinas': 1,
        'estado': 'Finalizado.',
    },
    '4': {
        'nome': 'cgh_granada',
        'numero_turbinas': 2,
        'estado': 'Finalizdao.',
    },
    '5': {
        'nome': 'cgh_ponte_serrada',
        'numero_turbinas': 1,
        'estado': 'Andamento.',
    },
    '6': {
        'nome': 'cgh_sao_sebastiao',
        'numero_turbinas': 2,
        'estado': 'Andamento.',
    },
    '7': {
        'nome': 'cgh_taquaruçu',
        'numero_turbinas': 1,
        'estado': 'Andamento.',
    },
    '8': {
            'nome': 'cgh_jasp',
            'numero_turbinas': 4,
            'estado': 'Andamento.',
        },
}
ug = '8'
nome_usina = usinas[ug]['nome']
numero_turbinas = usinas[ug]['numero_turbinas']

modulo = criar_modelo(nome_usina, numero_turbinas)

sql_usina = importlib.import_module(modulo)

# def connect_database(conexao: dict):
#     '''
#     Função que se conecta ao banco de dados.
#     '''
#     try:
#         connection = DatabaseManager(**conexao)
#         connection.connect()
#
#         pr.pr(f'Conectado ao banco de dados {conexao["database"]} com sucesso!')
#         return connection
#     except Exception as e:
#         pr.pr(f'Erro ao conectar ao banco de dados {conexao["database"]}')
#         pr.pr(f'Erro: {e}')
#         return None
#
# db_manager = connect_database(conexoes['railway'])
# pd = db_manager.read_data('cgh_fae')
# print(pd.columns)
# pd.to_csv('cgh_fae_novo.csv', index=False)
# db_manager.create_table('usina', {'id': 'INT', 'name': 'VARCHAR(255)'})
# db_manager.insert_data('usina', 'valor', [('1',), ('2',)])
