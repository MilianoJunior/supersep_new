# This is a sample Python script.
import os
import re
import pandas as pd
from libs.jasp.tags_jasp import TagsJasp
from libs.sao_sebastiao.tags_sao_sebastiao import TagsSaoSebastiao
from libs.frozza.tags_frozza import TagsFrozza
from unidecode import unidecode

'''
##############################################################################################################
Funções para o tratamento dos textos das tags
##############################################################################################################
'''
def text_to_list(text_dict: dict)-> dict:
    '''Divide o texto em uma lista de linhas, onde cada linha é um item da lista'''
    for text in text_dict.items():
        text_dict[text[0]] = text[1].splitlines()
    return text_dict

def remove_empty_lines(text_dict: dict)-> dict:
    '''Remove as linhas vazias da lista'''
    for text in text_dict.items():
        text_dict[text[0]] = [i for i in text[1] if i != '']
    return text_dict

def text_to_list_with_delimiter(text_dict: dict, delimiter: list)-> dict:
    '''Divide o texto em uma lista de linhas, onde cada linha é um item da lista'''
    padrao = "|".join(map(re.escape, delimiter))
    for text in text_dict.items():
        text_dict[text[0]] = [ re.split(padrao, i) for i in text[1]]
    return text_dict

def serach_number(text_dict: dict)-> dict:
    '''Procura por números no texto'''
    for text in text_dict.items():
        text_dict[text[0]] = [re.search(r'\(\*([^*]+)\*\)|(\d+x\d+)', i) for i in text[1]]
    return text_dict

def remove_empty_elements(text_dict: dict)-> dict:
    '''Remove os elementos vazios da lista'''
    for text in text_dict.items():
        novo_texto = []
        for i in range(len(text[1])):
            if isinstance(text[1][i], list):
                novo_texto.append([s for s in text[1][i] if s != '' and s != ' ' ])
        text_dict[text[0]] = novo_texto
    return text_dict

def transform_list_to_dict(text_dict: dict)-> dict:
    '''Transforma uma lista em um dicionário'''
    for text in text_dict.items():
        novo_texto = []
        for i in range(len(text[1])):
            if len(text[1][i]) == 4:
                novo_texto.append({
                    'type': text[1][i][0].split('x')[0],
                    'address': text[1][i][0].split('x')[1],
                    'nome': text[1][i][1],
                    'memory': text[1][i][2],
                    'format': text[1][i][3],
                })
        text_dict[text[0]] = novo_texto
    return text_dict
'''
Usar o principio de programação funcional, onde cada função tem uma responsabilidade

A solução está na reflexão do problema, em acreditar que para problemas complexos,
devemos dar um passo de cada vez. Para que futuramente essa crença de que o problema dever ser
resolvido de uma vez só, não nos impeça de resolver problemas complexos.
'''

def tratamento_tags(usina: dict, verbose=False):
    ''' leitura e tratamento dos textos das tags'''
    #
    tags = usina['tags'].copy()

    tags = text_to_list(tags) # transforma o texto em uma lista de linhas

    tags = remove_empty_lines(tags) # remove as linhas vazias da lista

    delimitadores = [" ", ",", "\t", "(", ")", ":", ";", "*"]
    tags = text_to_list_with_delimiter(tags, delimitadores) # divide o texto em uma lista de linhas, onde cada linha é um item da lista

    tags = remove_empty_elements(tags) # remove as linhas vazias da lista

    tags = transform_list_to_dict(tags) # transforma uma lista em um dicionário

    if verbose:
        cont = 0
        for tag in tags.items():
            for s in tag[1]:
                if len(s) < 5:
                    print(s)
                    raise Exception('Erro no tratamento das tags')
                cont += 1

            # [print(tag[0], i, x, len(x)) for i, x in enumerate(tag[1])]

    return tags

'''
##############################################################################################################
Funções para implementar as tags no arquivo no formato csv
##############################################################################################################
'''
def subs_names_df(df: pd.DataFrame, subs: list)-> pd.DataFrame:
    '''Substitui os nomes das colunas do dataframe'''
    df.loc[len(df)] = df.columns
    df.columns = subs
    return df

def define_format_02(format: str):
    '''convert o formato do CLP para o formato do supervisório'''
    formatos = {
        'BOOL': 'Bit',
        'INT': '16-bit Signed',
        'DINT': '16-bit Signed',
        'REAL': '32-bit Float',
        'STRING': 'String',
        'TIME': 'String',
    }
    return formatos.get(format, 'Undesignated')

def define_name_01(ug: str, funcao: str , name: str, cont: int, verbose=False):
    '''convert o nome do CLP para o nome do supervisório'''
    ug = ug.replace('_750_852','')
    # primeira letra maiuscula
    funcao = funcao.title()
    name = f'{ug}_{funcao}.{name}' #_{str(cont).zfill(4)}'
    name =unidecode(name)
    name = name.replace(' ','')
    if verbose:
        print(name)
    return name

def construct_tags(ugs: list, tags: dict, df: pd.DataFrame , verbose=False):
    cont = 0
    conta = df.shape[0]
    for funcao, value in tags.items():
        # print(funcao)
        for i in range(len(value)):
            nome = value[i]['nome']
            address = value[i]['address']
            type = value[i]['type'].replace('0', '') + 'x'
            for ug in ugs:
                cont += 1
                conta += 1
                name = define_name_01(ug, funcao, nome, cont, verbose=verbose)
                formato = define_format_02(value[i]['format'])
                df.loc[conta] = [name, ug, type, int(address), '', formato]
                print(' '*5, cont, conta,  len(df), name, ug, type, address, formato)
    return df

def implementar_tags_no_csv(usina: dict, verbose=False):
    '''Implementa as tags no arquivo no formato csv'''
    tags = usina['tags_tratadas'].copy()

    ugs = [f'UG0{i+1}' for i in range(usina['nr_ugs'])]

    print('PASTA: ', os.getcwd())
    df = pd.read_csv(usina['csv'], header=None, sep=',') # lê o arquivo csv

    df_original = df.copy() # copia o dataframe

    df = subs_names_df(df, ['tag_name','device_name','type','address','comment','format']) # substitui os nomes das colunas do dataframe

    # apagar todos os valores com os device_name igual a ugs
    for ug in ugs:
        df = df[df['device_name'] != ug ]

    # resetar o index do dataframe
    df.reset_index(drop=True, inplace=True)

    df = construct_tags(ugs, tags, df, verbose=verbose) # implementa as tags no arquivo no formato csv

    # verificar a quantidade de address duplicados por device_name
    # for ug in ugs:
    #     print('--' * 50)
    #     print(f'Duplicados: {ug}')
    #     print(df[df['device_name'] == ug]['address'].value_counts())

    df.to_csv(usina['csv_tratado'], sep=',', index=False, header=False) # salva o arquivo csv

    # print('--' * 50)
    # print(df.head(5))
    # print('--' * 50)
    # print(df.columns)
    # print('--' * 50)
    # print(df_original.values[-1])
    # print('--' * 50)
    # print(df.values[-1])
    # print('--' * 50)
    # print(df['format'].value_counts())

'''
##############################################################################################################
Funções para comparar os arquivos csv e verificar se as tags foram implementadas corretamente
##############################################################################################################
'''
# importar os arquivos csv
def importar_csv(path: str)-> pd.DataFrame:
    '''Importa o arquivo csv'''
    name_columns = ['tag_name', 'device_name', 'type', 'address', 'comment', 'format']  # define os nomes das colunas

    df = pd.read_csv(path, header=None, names= name_columns, sep=',') # lê o arquivo csv

    return df

# comparar os arquivos csv
def mainCompararCsv(path_csv_original: str, path_csv_new: str, verbose=False):
    '''Compara os arquivos csv'''

    # importar csv original
    df_original = importar_csv(path_csv_original)

    # importar csv novo
    df = importar_csv(path_csv_new)

    # verbose
    if verbose:
        print('_' * 100)
        print(df_original.columns)
        print(df.columns)
        print(df_original.values[0])
        print(df.values[0])
        print(df_original.values[-1])
        print(df.values[-1])
        print('_' * 100)


    # atribuir tamanho do dataframe
    size_df_original = df_original.shape
    size_df = df.shape
    if size_df_original != size_df:
        print('_' * 100)
        print('Tamanho do dataframe diferente')
        print(size_df_original, size_df)

    # verificar quantidade de valores diferentes
    equals = df_original.equals(df)
    if equals:
        print('_' * 100)
        print('Valores iguais')
    else:
        print('Valores diferentes')
        print(equals)

    # imprimir os valores diferentes do original
    if not equals:
        # imprimir todas as linhas diferentes
        print('_' * 100)
        def print_diff(x):
            return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)

        # contar a quantidade de valores address em cada dataframe
        count_address_original = df_original['address'].value_counts()
        count_address = df['address'].value_counts()
        print(count_address_original)
        print(count_address)
        print('"' * 100)

        # contar a quantidade de valores device_name em cada dataframe
        count_device_name_original = df_original['device_name'].value_counts()
        count_device_name = df['device_name'].value_counts()
        print(count_device_name_original)
        print(count_device_name)
        print('"' * 100)

        # loop para comparar o address e tag_name
        cont = 0
        contb = 0
        for idx, row in df_original.iterrows():
            address = row['address']
            name_device = row['device_name']
            if 'UG' in name_device:
                valida = df[(df['address'] == address) & (df['device_name'] == name_device)]
                cont += 1
                if len(valida) > 0:
                    pass
                    # if not all([row["tag_name"].upper() in name.upper() for name in valida["tag_name"].values]):
                    #     contb += 1
                    #     print('idx: ', idx, ' cont: ',cont, ' contb: ',contb)
                    #     print('address: ',address)
                    #     print('valida: ',valida["tag_name"].values)
                    #     print('name original: ',row['tag_name'].upper())
                    #     print([row["tag_name"].upper() in name.upper() for name in valida["tag_name"].values])
                    #     print('**********')
                else:
                    contb += 1
                    print(contb, 'Endereço nao encontrado: ', address, name_device, row['tag_name'])
