import os
import pandas as pd
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

data_types = {
    1: {'16-bit BCD': 'TINYINT'},
    2: {'32-bit BCD': 'TINYINT'},
    3: {'16-bit HEX': 'SMALLINT'},
    4: {'32-bit HEX': 'SMALLINT'},
    5: {'16-bit Binary': 'MEDIUMINT'},
    6: {'32-bit Binary': 'MEDIUMINT'},
    7: {'16-bit Signed': 'INT'},
    8: {'32-bit Signed': 'INT'},
    9: {'16-bit Unsigned': ['INT', 'BIT']},
    10: {'32-bit Unsigned': ['INT', 'BIT']},
    11: {'32-bit Float': ['FLOAT','DOUBLE','DECIMAL']},
    12: {'Undesignated': 'INT'},
    13: {'String': ['DATETIME','CHAR', 'BINARY', 'VARCHAR', 'VARBINARY', 'TINYBLOB', 'TINYTEXT', 'BLOB', 'TEXT', 'MEDIUMBLOB',
                   'MEDIUMTEXT', 'LONGBLOB', 'LONGTEXT']},
}

def search_type(valor):
    for key, value in data_types.items():
        for k, v in value.items():
            if valor in k:
                if isinstance(v, list):
                    return v[0]
                return v

# imprimindo as tags
def print_tags(control, nivel=0):
    space = '---' * nivel
    for key, value in control.items():
        if isinstance(value, dict):
            print(f'{space} {key} ->')
            print_tags(value, nivel + 1)
        else:
            print(f'{space} {key}: {value}')

def tags(name_path):
    # caminho do arquivo tags.csv
    tags_path = os.path.join(os.path.dirname(__file__),'..','assets', name_path)
    # importando tags
    tags = pd.read_csv(tags_path)
    # alterando nome das colunas
    tags.columns = ['nome', 'device','tipo', 'endereco', 'descricao', 'unidade']
    return tags

def buscar_tags(nome_tag, name_path='tags.csv'):
    # buscando tags semelhantes
    tags_similares = tags(name_path)[tags(name_path)['nome'].str.contains(nome_tag, case=False, na=False)]
    # retornando tags semelhantes
    return tags_similares

'''
Tenho uma função "rename_columns" que recebe um texto e retorna um novo texto abreviado.
Mas agora preciso criar outra função que recebe o texto abrevidado e retorna o texto original.
'''
def rename_columns(text):
    new_name = text.split('_')
    new_name = ''.join([part[2::] if ('ug01' in part or 'ug02' in part) else part[0] for part in new_name])
    return new_name

def reverse_rename(abbr):
    mapping = {
        's': 'status',
        'ae': 'acumulador_energia',
        'na': 'nivel_agua',
        'tf': 'tensao_fase_',
        'cf': 'corrente_fase_',
        'te': 'tensao_excitacao',
        'ce': 'corrente_excitacao',
        'f': 'frequencia',
        'pa': 'potencia_ativa',
        'pr': 'potencia_reativa',
        'd': 'distribuidor',
        'v': 'velocidade',
        'hm': 'horimetro_mecanico',
        'he': 'horimetro_eletrico',
        'tme': 'temp_mancal_estat',
        'tmc': 'temp_mancal_comb',
        'tou': 'temp_oleo_u',
        'tc': 'temp_csu2',
        'vmg': 'vibr_mancal_guia_',
        'vmc': 'vibr_mancal_comb_',
        'cl': 'corrente_linha_',
        'cs': 'corrente_seq_',
        'tb': 'tensao_barra',
        'tt': 'tensao_te',
    }

    prefix = abbr[:4]
    rest = abbr[4:]

    # For those abbreviations that end with A, B, C, X, Y, Z
    if rest[-1] in ['A', 'B', 'C', 'X', 'Y', 'Z']:
        suffix = rest[-1]
        rest = rest[:-1]
    else:
        suffix = ''

    return prefix + '_' + mapping[rest] + suffix

# Test
# print(reverse_rename('101s'))  # Expected 'ug01_status'


