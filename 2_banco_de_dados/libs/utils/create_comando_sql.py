comandos_sql = {
                1: {
                    'command': 'CREATE DATABASE nome;',
                    'help': 'criar banco de dados',
                },
                2: {
                    'command': 'CREATE TABLE nome_tabela (nome_coluna tipo configuracao);',
                    'help': 'criar tabela no banco de dados',
                },
                3: {
                    'command': {'VARCHAR(arg)':4000,'TEXT':2*10**9,'CHAR':8000},
                    'help': 'cadeias de caracteres',
                },
                4: {
                    'command': {'BIGINT':8*8,'NUMERIC':(5,17),
                                'BIT':1,'SMALLINT':2,
                                'DECIMAL':(5,17),'INT':4,
                                'SMALLMONEY':4,'TINYINT':2,
                                'MONEY':8},
                    'help': 'Númericos exatos todos em bytes',
                },
                5: {
                    'command': {'DATE':4,'DATETIME2':(6,8),'SMALLDATETIME':4,'DATETIME':8,'TIME':(3,5),'DATETIMEOFFSET':(8,10)},
                    'help': 'Data e hora todos em bytes',
                },
                6: {
                    'command': {'FLOAT':(4,8),'REAL':4},
                    'help': 'Númericos aproximados',
                },
                7: {
                    'command': {'NCHAR':4000,'NTEXT':2*10**9,'NVARCHAR':4000},
                    'help': 'Cadeias de caracteres unicode',
                },
                8: {
                    'command': {'BINARY':8000,'IMAGEM':2*10**9,'VARBINARY':2*10**9},
                    'help': 'Cadeias de caracteres binária',
                },
                9: {
                    'command': 'INSERT INTO nome_tabela (coluna) VALUES (value);',
                    'help': 'Insere dados no banco de dados',
                }
}




''' 3 passo: Criar dados para inserir no banco de dados: semear dados no DB '''
# import random
#
# command = comandos_sql[9]["command"].replace('nome_tabela','dados')
# colunas = '('
# values = '('
# cont = 0
# for tags in tags_list:
#
#     for key, value in tags.items():
#         cont += 1
#         colunas += f'{key},\n'
#         values += "'${" + str(cont) +"}',\n"
#         # if value[5] == 'INT':
#         #     values += f'{random.randint(0,800000)},\n'
#         # else:
#         #     values += f'{random.uniform(0, 1.0)},\n'
# colunas += ')'
# values += ')'
# command = command.replace('(coluna)',colunas)
# command = command.replace('(value)',values)
#
# print(f'\n{command}\n')
# print('AQUI')


parisoto_local = {
    'ug01_nivel_agua': {
        '0': 'USINA_750_862',
        '1': 'USINA_Leitura.NivelCamaraCarga',
        '2': 13569,
        '3': 'Nível Água',
        '4': '32-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_tensao_fase_A': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_U_FaseAB',
        '2': 13349,
        '3': 'UG-01 Tensão Fase A',
        '4': 'Undesigned',
        '5': 'INT',
    },
    'ug01_tensao_fase_B': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_U_FaseBC',
        '2': 13350,
        '3': 'UG-01 Tensão Fase B',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_tensao_fase_C': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_U_FaseCA',
        '2': 13351,
        '3': 'UG-01 Tensão Fase C',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_corrente_fase_A': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_I_INST_A',
        '2': 13355,
        '3': 'UG-01 Corrente Fase A',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_corrente_fase_B': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_I_INST_B',
        '2': 13356,
        '3': 'UG-01 Corrente Fase B',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_corrente_fase_C': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_I_INST_C',
        '2': 13357,
        '3': 'UG-01 Corrente Fase C',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_tensao_excitacao': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.Gerador_ExcitacaoTensao',
        '2': 13380,
        '3': 'UG-01 Tensão Excitação',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_corrente_excitacao': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.Gerador_ExcitacaoCorrente',
        '2': 13381,
        '3': 'UG-01 Corren. Excitação',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_frequencia': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_FHz_INST',
        '2': 13363,
        '3': 'UG-01 Frequência',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_potencia_ativa': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_P_INST',
        '2': 13359,
        '3': 'UG-01 Potência Ativa',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_potencia_reativa': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_Q_INST',
        '2': 13360,
        '3': 'UG-01 Potência Reativa',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_potencia_aparente': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_S_INST',
        '2': 13361,
        '3': 'UG-01 Potência Aparente',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_fp': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.F50_PF_INST',
        '2': 13362,
        '3': 'UG-01 Fator de Potência',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_horimetro_e': {
        '0': 'UG01_750_862',
        '1': 'UG01_Setpoint.Horimetro_Eletrico',
        '2': 14105,
        '3': 'UG-01 Horimetro',
        '4': '32-bit Float',
        '5': 'FLOAT',
    },
    'ug01_horimetro_m': {
        '0': 'UG01_750_862',
        '1': 'UG01_Setpoint.Horimetro_Mecanico',
        '2': 14099,
        '3': 'UG-01 Horimetro',
        '4': '32-bit Float',
        '5': 'FLOAT',
    },
    'ug01_horimetro_UHRV': {
        '0': 'UG01_750_862',
        '1': 'UG01_Setpoint.Horimetro_UHRV',
        '2': 14111,
        '3': 'UG-01 Horimetro',
        '4': '32-bit Float',
        '5': 'FLOAT',
    },
    'ug01_distribuidor': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.Turbina_PosicaoDistribuidor',
        '2': 13303,
        '3': 'UG-01 Distribuidor',
        '4': '32-bit Float',
        '5': 'INT',
    },
    'ug01_velocidade': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.Turbina_Velocidade',
        '2': 13307,
        '3': 'UG-01 Velocidade RPM',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_acumulador_energia': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.Gerador_EnergiaFornecidakWh',
        '2': 13385,
        '3': 'UG-01 Acum. Energia',
        '4': '32-bit Float',
        '5': 'FLOAT',
    },
    'ug01_temp_fase_A': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD1_RTD1',
        '2': 13409,
        '3': 'UG-01 Temp. Fase A',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_fase_B': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD1_RTD2',
        '2': 13411,
        '3': 'UG-01 Temp. Fase B',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_fase_C': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD1_RTD3',
        '2': 13413,
        '3': 'UG-01 Temp. Fase C',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_nucleo_estator': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD1_RTD4',
        '2': 13415,
        '3': 'UG-01 Temp. Nucleo do estator.',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_casq_inf': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD2_RTD1',
        '2': 13417,
        '3': 'UG-01 Temp. Mancal Guia casquilo radial',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_man_comb': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD2_RTD2',
        '2': 13419,
        '3': 'UG-01 Temp. Mancal Comb. Casq. Radial',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_comb_escora': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD2_RTD3',
        '2': 13421,
        '3': 'UG-01 Temp. Mancal Escora',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_oleo_UHRV': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD2_RTD4',
        '2': 13423,
        '3': 'UG-01 Temp. Óleo UHRV',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_oleo_UHLM': {
        '0': 'UG01_750_862',
        '1': 'UG01_Leitura.RIO600_MOD3_RTD1',
        '2': 13425,
        '3': 'UG-01 Temp. Óleo UHRV',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_cs_u1': {
        '0': 'UG01_750_862',
        '1': 'UG01_Status.RegV_TurbinaParada',
        '2': 13427,
        '3': 'UG-01 Turbina Parada',
        '4': 'bool',
        '5': 'FLOAT',
    },
    'ug01_temp_engex': {
        '0': 'UG01_750_862',
        '1': 'UG01_Status.RegV_TurbinaParada',
        '2': 13429,
        '3': 'UG-01 Turbina Parada',
        '4': 'bool',
        '5': 'FLOAT',
    },
    'ug01_status': {
        '0': 'UG01_750_862',
        '1': 'UG01_Status.RegV_TurbinaParada',
        '2': 20548,
        '3': 'UG-01 Turbina Parada',
        '4': 'bool',
        '5': 'BOOLEAN',
    },
}

data_types = {
        1: {'16/32-bit BCD': 'TINYINT'},
        2: {'16/32-bit HEX': 'SMALLINT'},
        3: {'16/32-bit Binary': 'MEDIUMINT'},
        4: {'16/32-bit Signed': 'INT'},
        5: {'16/32-bit Unsigned': ['BIGINT', 'BIT']},
        6: {'32-bit Float': ['FLOAT','DOUBLE','DECIMAL']},
        7: {'String': ['DATETIME','CHAR', 'BINARY', 'VARCHAR', 'VARBINARY', 'TINYBLOB', 'TINYTEXT', 'BLOB', 'TEXT', 'MEDIUMBLOB',
                       'MEDIUMTEXT', 'LONGBLOB', 'LONGTEXT']},
}
def definir_entradas():
    '''Define as colunas para o banco de dados.'''
    entradas =['device', 'name', 'address', 'data_type', 'data_type_sql']
    tagss = {}
    cont = 0
    while True:
        cont += 1
        coluna = input(f'Coluna {cont} Continuar? ')
        if coluna == 'sair':
            break
        if coluna == 'print':
            print(tagss)
            continue
        tagss[str(cont)] = {}
        for index in range(0,4):
            if index == 3:
                print('opções: ')
                for key, value in data_types.items():
                    print(f'{key} - {value}')
                resp = input(f'Escolha um numero: ')
                chave = list(data_types[int(resp)].keys())[0]
                valor = list(data_types[int(resp)].values())[0]
                if isinstance(valor, list):
                    print(valor)
                    resp1 = input(f'Escolha um index: ')
                    valor = valor[int(resp1)]
                tagss[str(cont)][str(index)] = chave
                tagss[str(cont)][str(index+1)] = valor
            else:
                resp = input(f'{entradas[index]}: ')
                tagss[str(cont)][str(index)] = resp
    print('  ')
    return tagss

def generate_sql_command(data, ugs):
    table_name = 'my_table'  # nome da tabela
    command = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, "
    for ug in range(1, int(ugs)+1):
        for key in data.keys():
            if 'UG' in data[key]['0']:
                column_name =f'UG0{ug}_' + data[key]['1']
                column_type = data[key]['4']
                command += f"{column_name} {column_type}, "
            else:
                if ug == 1:
                    column_name = data[key]['1']
                    column_type = data[key]['4']
                    command += f"{column_name} {column_type}, "

    command += "data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    return command

def formatar_leituras(tags):
    cont = 0
    for key, value in tags.items():
        cont += 1
        print(f"'{cont}'" + ': {')
        for i in value.keys():
            if i == '2':
                print(f"    '{i}': {value[i]},")
            else:
                print(f"    '{i}': '{value[i]}',")
            if i == '4':
                continue
        print('},')
    print('}')

import re

import re

import re

def create_insert_sql(create_table_sql):
    # Verificando se a string de entrada é uma string SQL de criação de tabela válida
    if not isinstance(create_table_sql, str) or not create_table_sql.lower().startswith('create table'):
        raise ValueError("A string de entrada não é uma string SQL de criação de tabela válida.")

    # Extraindo o nome da tabela
    match = re.search(r"create table (\w*)", create_table_sql, re.IGNORECASE)
    if match is None:
        raise ValueError("A string de entrada não contém um nome de tabela válido.")
    table_name = match.group(1)

    # Extraindo os nomes das colunas
    match = re.search(r"\((.*)\)", create_table_sql)
    if match is None:
        raise ValueError("A string de entrada não contém definições de colunas válidas.")
    column_part = match.group(1)

    # Dividindo as definições de colunas e removendo espaços extras
    column_definitions = column_part.split(',')

    # Pegando apenas o nome das colunas e excluindo a coluna 'id'
    column_names = [col.strip().split(' ')[0] for col in column_definitions if not col.strip().startswith('id')]

    # Se não houver colunas para inserir, lança um erro
    if not column_names:
        raise ValueError("A string de entrada não contém colunas válidas para inserir (excluindo 'id').")

    # Montando a string de inserção
    insert_sql = "INSERT INTO {} ({}) VALUES ({})".format(
        table_name,
        ', '.join(column_names),
        ', '.join("'${{{}}}'".format(i+1) for i in range(len(column_names)))  # alteração aqui
    )

    # Retornando a string de inserção
    return insert_sql + ";"
cx = '''CREATE TABLE cgh_parisoto (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, ug01_nivel_agua FLOAT DEFAULT NULL, 
ug01_tensao_fase_A INT DEFAULT NULL, ug01_tensao_fase_B INT DEFAULT NULL, ug01_tensao_fase_C INT DEFAULT NULL);'''
'''
ug01_corrente_fase_A INT DEFAULT NULL,
ug01_corrente_fase_B INT DEFAULT NULL,
ug01_corrente_fase_C INT DEFAULT NULL,
ug01_tensao_excitacao INT DEFAULT NULL,
ug01_corrente_excitacao INT DEFAULT NULL,
ug01_frequencia INT DEFAULT NULL,
ug01_potencia_ativa INT DEFAULT NULL,
ug01_potencia_reativa INT DEFAULT NULL,
ug01_potencia_aparente INT DEFAULT NULL,
ug01_fp INT DEFAULT NULL,
ug01_horimetro_e FLOAT DEFAULT NULL,
ug01_horimetro_m FLOAT DEFAULT NULL,
ug01_horimetro_UHRV FLOAT DEFAULT NULL,
ug01_distribuidor INT DEFAULT NULL,
ug01_velocidade INT DEFAULT NULL,
ug01_acumulador_energia FLOAT DEFAULT NULL,
ug01_temp_fase_A FLOAT DEFAULT NULL,
ug01_temp_fase_B FLOAT DEFAULT NULL,
ug01_temp_fase_C FLOAT DEFAULT NULL,
ug01_temp_nucleo_estator FLOAT DEFAULT NULL,
ug01_temp_casq_inf FLOAT DEFAULT NULL,
ug01_temp_man_comb FLOAT DEFAULT NULL,
ug01_temp_comb_escora FLOAT DEFAULT NULL,
ug01_temp_oleo_UHRV FLOAT DEFAULT NULL,
ug01_temp_oleo_UHLM FLOAT DEFAULT NULL,
ug01_temp_cs_u1 FLOAT DEFAULT NULL,
ug01_temp_engex FLOAT DEFAULT NULL,
ug01_status BOOLEAN DEFAULT NULL,
data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);'''

if __name__ == '__main__':
    from Connection import DatabaseManager
    from var_conexoes import conexoes, supervisorio
    from imprimir import pr
    import json

    # 1 passo preencher os dados de configuraçoes do banco de dados
    pr.pr('1 Passo preencher os dados de configuraçoes do banco de dados')
    name_table = 'leituras'
    usina = input('Nome da usina: ')
    ugs = input('Numero de geradores: ')

    #2 passo consultar ver se o nome da tabela existe
    try:
        db_manager = DatabaseManager(**conexoes['local_utils'])
        db_manager.connect()
        dados = db_manager.read_data('leituras')
    except Exception as e:
        raise Exception('Erro ao conectar ao banco de dados: ', e)

    # 3 passo verificar se a usina já existe
    if dados['usina'].isin([usina]).any():
        pr.pr('A Usina já existe!')
        resp = input('Deseja criar um nova query(1), ou usar a que existe (2)? ')
        print('resposta : ', resp)
        if resp == '1':
            pr.pr('Criar uma nova query')
            new_colunas = definir_entradas()
            pr.pr('Armazenar a nova query no banco de dados')
            new_colunas= json.dumps(new_colunas)
            db_manager.insert_data('leituras', ('usina','valores'), [(usina, new_colunas) ])
            new_colunas = json.loads(new_colunas)
        else:
            pr.pr('Usar a query que já existe')
            new_colunas = dados[dados.values == usina]['valores']
            new_colunas = json.loads(new_colunas.values[0])
    else:
        pr.pr('Criar uma nova query')
        new_colunas = definir_entradas()
        pr.pr('Armazenar a nova query no banco de dados')
        new_colunas = json.dumps(new_colunas)
        db_manager.insert_data('leituras', ('usina','valores'), [(usina, new_colunas) ])
        new_colunas = json.loads(new_colunas)

    # formatar_leituras(new_colunas)
    # 4 passo Criar comando sql para criar a tabela
    pr.pr('2 Criar comando sql')
    cmd_create_table = generate_sql_command(new_colunas, ugs)
    pr.pr(cmd_create_table)
    # 5 passo Criar o comando sql para inserir os dados com o formato do EasyBuilder
    cmd_insert_table = create_insert_sql(cmd_create_table)
    pr.pr(cmd_insert_table)


'''
Preciso de uma função em python que receba uma string em python e retorne um comando sql
como no formato abaixo:

argumento da função:
'CREATE TABLE my_table (id INT AUTO_INCREMENT PRIMARY KEY, nivel_agua INT, UG01_tensao_fase_a INT, UG02_tensao_fase_a INT, data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'

retorno da função:
INSERT INTO my_table (nivel_agua, UG01_tensao_fase_a, UG02_tensao_fase_a) VALUES ('${1}','${2}','${3}');


'''
    #
    # name_table = 'leituras'
    # usina = 'parisoto'
    # tags_UG01 = json.dumps(tags_UG01)
    # dados = db_manager.read_data(name_table)
    # valores = dados.valores[0]
    # dict_data = json.loads(valores)
    # for key, value in dict_data.items():
    #     print(key, value[0])
    # print(tags_UG01)
    # def insert_data(self, table_name, column_name, data)
    # db_manager.insert_data(name_table, ('usina','valores'), [(usina, tags_UG01) ])

# command = comandos_sql[2]["command"].replace('nome_tabela','cgh_sao_sebastiao')
#
# colunas = '(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,\n'
#
# for key, value in tags_UG01.items():
#     colunas += f'{key} {value[5]} DEFAULT NULL, \n '
#     # print(key)
#
# colunas += 'data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)'
# command = command.replace('(nome_coluna tipo configuracao)',colunas)
# print(f'\n{command}\n')

# CRIAR O BANCO DE DADOS
'''
CREATE DATABASE engesepdb;


CREATE TABLE cgh_parisoto (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
ug01_nivel_agua FLOAT DEFAULT NULL,
ug01_tensao_fase_A INT DEFAULT NULL,
ug01_tensao_fase_B INT DEFAULT NULL,
ug01_tensao_fase_C INT DEFAULT NULL,
ug01_corrente_fase_A INT DEFAULT NULL,
ug01_corrente_fase_B INT DEFAULT NULL,
ug01_corrente_fase_C INT DEFAULT NULL,
ug01_tensao_excitacao INT DEFAULT NULL,
ug01_corrente_excitacao INT DEFAULT NULL,
ug01_frequencia INT DEFAULT NULL,
ug01_potencia_ativa INT DEFAULT NULL,
ug01_potencia_reativa INT DEFAULT NULL,
ug01_potencia_aparente INT DEFAULT NULL,
ug01_fp INT DEFAULT NULL,
ug01_horimetro_e FLOAT DEFAULT NULL,
ug01_horimetro_m FLOAT DEFAULT NULL,
ug01_horimetro_UHRV FLOAT DEFAULT NULL,
ug01_distribuidor INT DEFAULT NULL,
ug01_velocidade INT DEFAULT NULL,
ug01_acumulador_energia FLOAT DEFAULT NULL,
ug01_temp_fase_A FLOAT DEFAULT NULL,
ug01_temp_fase_B FLOAT DEFAULT NULL,
ug01_temp_fase_C FLOAT DEFAULT NULL,
ug01_temp_nucleo_estator FLOAT DEFAULT NULL,
ug01_temp_casq_inf FLOAT DEFAULT NULL,
ug01_temp_man_comb FLOAT DEFAULT NULL,
ug01_temp_comb_escora FLOAT DEFAULT NULL,
ug01_temp_oleo_UHRV FLOAT DEFAULT NULL,
ug01_temp_oleo_UHLM FLOAT DEFAULT NULL,
ug01_temp_cs_u1 FLOAT DEFAULT NULL,
ug01_temp_engex FLOAT DEFAULT NULL,
ug01_status BOOLEAN DEFAULT NULL,
data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);
'''

'''
# conversa com o gerson, explicando o problema

# 1 - O que é o problema?
   O valor do acumulador de energia está sendo persistido no banco de dados com o valor 0.0, 
'''

'''
CREATE TABLE my_table (id INT AUTO_INCREMENT PRIMARY KEY, UG01_nivel_agua INT, UG01_ug01_tensao_fase_A INT, 
UG01_ug01_tensao_fase_B INT, ug01_tensao_fase_C INT, UG01_ug01_corrente_fase_A INT, UG01_ug01_corrente_fase_B INT, 
UG01_ug01_corrente_fase_C INT, UG01_ug01_corrente_excitacao INT, UG01_ug01_tensao_excitacao INT, ug01_frequencia 
FLOAT, ug01_potencia_ativa BIGINT, ug01_potencia_reativa BIGINT, ug01_potencia_aparente BIGINT, ug01_fp INT, 
ug01_distribuidor INT, data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
'''
'''
INSERT INTO my_table (UG01_nivel_agua, UG01_ug01_tensao_fase_A, UG01_ug01_tensao_fase_B, ug01_tensao_fase_C, UG01_ug01_corrente_fase_A, UG01_ug01_corrente_fase_B, UG01_ug01_corrente_fase_C, UG01_ug01_corrente_excitacao, UG01_ug01_tensao_excitacao, ug01_frequencia, ug01_potencia_ativa, ug01_potencia_reativa, ug01_potencia_aparente, ug01_fp, INT, data_hora) VALUES ('${1}', '${2}', '${3}', '${4}', '${5}', '${6}', '${7}', '${8}', '${9}', '${10}', '${11}', '${12}', '${13}', '${14}', '${15}', '${16}');
'''