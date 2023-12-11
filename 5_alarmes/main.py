# Autor: Miliano Fernandes de Oliveira Junior (MFOJ) - 17/0/2023
# importar biblioteca#
import os
import re
import time
import numpy as np
import xlrd
import pandas as pd
import openpyxl
import math
# from libs.SaoSebastiao.texto_alarme import lista_modos_psa
from libs.ponteSerrada.texto_alarme import lista_modos_psa
poo = 0

def extrair_numeros(cadeia):
    ''' Função para extrair o valor de uma cadeia de caracteres'''
    padrao = r"\[(\d+)\].*(\[\d+\]\.\d+).*\(\*(.*)\*\)"
    resultado = re.search(padrao, cadeia)
    if resultado:
        return resultado
    else:
        return None

def get_alarm_input(frase):
    regex = r"input:=\s*(\S+),"
    match = re.search(regex, frase)
    if match:
        return match.group(1)
    else:
        return None
def filtra_dados(texto_alarmes, texto_enderecos, categoria, device):
    global poo
    padrao_content = r"input:=([^\s,]+)"
    padrao_numero = r"\[(\d+)\].*(\[\d+\]\.\d+)"
    mensagem = r"\[(\d+)\].*(\[\d+\]\.\d+).*\(\*(.*)\*\)"
    lista_alarmes = []
    lista_final = []
    try:
        line_cont = 0
        for text in texto_alarmes.splitlines():
            line_cont += 1
            if len(text) < 50:
                # print('################################')
                # print('Linha: ',line_cont,' - ',text)
                # print('################################')
                continue
            # print('Linha: ',line_cont,' - ',text, ' - ', len(text))
            novo = extrair_valor(text, mensagem)
            if novo is None:
                text += '(*Mensagem - Reserva*)'
                novo = extrair_valor(text, mensagem)
            msg = novo.group(3) if novo.group(3) else 'Mensagem - Reserva'
            numer = novo.group(1)
            numer = numer if numer[0] != '0' else numer[1::]
            category = novo.group(2)
            lista_alarmes.append(
                {'content': msg, 'numeros': numer, 'id': category, 'address': None})
    except Exception as e:
        raise Exception('\nErro na função filtra_dados 1, Linha : {}\n    {}'.format(line_cont, e))
    # print(' Primeiro: --------------------------------------')
    # for line in enumerate(lista_alarmes):
    #     print(line)
    # print('--------------------------------------')
    inicio = time.time()
    try:
        line_cont = 0
        column_cont = 0
        chave = True
        for item in lista_alarmes:
            line_cont += 1
            # print('Linha: ',line_cont,' - ',item)
            if chave == False:
                print('Não encontrado: ', item['numeros'])
            chave = False
            for value in texto_enderecos:

                column_cont += 1
                # print('Coluna: ',column_cont,' - ',value)
                busca = f'Alarme_{item["numeros"]}'
                # print('Buscando: ',busca, value['name'])
                if busca == value['name']:
                    # print(value,'---', busca)
                    # print(item)
                    chave = True
                    content = f"{item['id'].replace(']', '')}]: {device[0:5]} - {item['content'].replace('.', ' ')}"
                    # print(content)
                    lista_final.append({
                        'Category': categoria,
                        'PLC Name (Read)': device,
                        'Address (Read)': value['address'][2::],
                        'Content': content,
                        'Address (Condition)': value['address'][2::],
                        'Sound Index': 1,
                        'PLC Name (Condition)': device})
                    break

    except Exception as e:
        raise Exception('\n   Erro na função filtra_dados 2, Linha: {},{},\n{}'.format(line_cont, column_cont,e))
    print('--------------------------------------')
    print('Fim da função filtra_dados')
    print('--------------------------------------')
    for line in enumerate(lista_final):
        print(line)
    print('--------------------------------------')
    print('Tempo de execução: ',round(time.time() - inicio,7))
    poo += 1
    if poo == 100:
        raise Exception('Finalizando o programa')
    # raise Exception('Finalizando o programa')

    return lista_final
def extrair_valor(cadeia, padrao):
    ''' Função para extrair o valor de uma cadeia de caracteres'''
    resultado = re.search(padrao, cadeia)
    if resultado:
        return resultado
    else:
        return None

def alarmes_tratamento(texto_enderecos, verbose=False):
    ''' Função para tratar os alarmes do arquivo xls'''
    try:
        print(texto_enderecos)
        padrao_address = r'\(\*\s*(\w+)\s*\*\)\s+(\w+)\s+'
        lista_enderecos = []
        texto_enderecos = [text for text in texto_enderecos.splitlines() if text != '']
        for text in enumerate(texto_enderecos):
            value = extrair_valor(text[1], padrao_address)
            if verbose:
                print(text)
                print(value.group(1), value.group(2))
            lista_enderecos.append({'name':value.group(2), 'address':value.group(1)})
        print('--------------------------------------')
        print('Fim da função alarmes_tratamento')
        return lista_enderecos
    except Exception as e:
        print('Erro da função de tratamento de alarmes: ', e)

def acrescentado_alarme(df, valores):
    indice_atual = len(df)
    nova_linha = []
    for name_01 in df.columns:
        valor = valores.get(name_01, False)
        if valor:
            nova_linha.append(valor)
        else:
            nova_linha.append(df[name_01].values[indice_atual-1])
    df.loc[indice_atual] = nova_linha
    return df

def validar_alarmes(df, ref):
    ''' Função para validar os alarmes do arquivo xls'''
    coluna = ref['coluna']
    address = ref['address']
# alterando colunas NULL
def colunas_null(df):
    print('--------------------------------------')
    print('Iniciando colunas NULL: ',df.shape)
    colunas_null = ['Index (Read)', 'Index (Notification)', 'Index (WATCH1)', 'Index (WATCH2)', 'Index (WATCH3)',
                    'Index (WATCH4)', 'Index (WATCH5)', 'Index (WATCH6)', 'Address (String ID)', 'Index (WATCH7)',
                    'Index (Occurrence)', 'Address (String ID)', 'Index (Condition)', 'Index (Elapsed Time)',
                    'Index (Enable/Disable)']

    # Criando um novo DataFrame com as colunas desejadas e valores 'null'
    df_null = pd.DataFrame('null', index=df.index, columns=colunas_null)

    print('--------------------------------------')
    print('Iniciando concatenação: ',df_null.shape)
    # Concatenando o DataFrame original com o novo DataFrame
    df_final = pd.concat([df, df_null], axis=1)
    print('--------------------------------------')
    print('Finalizando concatenação: ',df_final.shape)

    return df_final

def gerar_lista_alarmes(lista_modos_psa, colunas, df):
    ''' Função para gerar uma lista com os alarmes do arquivo xls'''
    inicio = time.time()
    lista_alarme = alarmes_tratamento(lista_modos_psa['enderecos_alarmes'][0])
    cont = 0
    lista_final = []
    for key, value in lista_modos_psa.items():
        if value[1]:
            cont += 1
            ug_name = 'UG02_750_852'
            lista_x = filtra_dados(value[0], lista_alarme, value[1], ug_name)
            # lista_final.append(lista_x)
            for linha in lista_x:
                print(linha)
                df = acrescentado_alarme(df, linha)
    df_final = colunas_null(df)
    print('--------------------------------------')
    print('Finalizando: ',df.shape)
    # for s in enumerate(lista_final):
    #     print(s)
    # print(df.head())
    filename = "libs\\SaoSebastiao\\novo_alarme.xlsx"
    df.to_excel(filename, index=False)

    print('--------------------------------------')
    print('Fim da função gerar_lista_alarmes')
    print('Tempo de execução: ', round(time.time() - inicio, 7))

'''
    2 - Criar uma lista com os alarmes em data frame
'''

contador = 0
contador_01 = 0

def content_alarmes_041(text):
    ''' Função para tratar os conteudos alarmes do texto'''
    mensagem = r"\[(\d+)\].*(\[\d+\]\.\d+).*\(\*(.*)\*\)"
    return re.search(mensagem, text)

def numeros_alarmes_042(text):
    ''' Função para tratar os conteudos alarmes do texto'''
    numero = r"\[(\d+)\].*(\[\d+\]\.\d+)"
    return re.search(numero, text)

def tratar_alarmes_04(alarmes, modo, categoria, verbose=True):
    ''' Função para tratar os conteudos alarmes do texto'''

    if verbose:
        print('--------------------------------------')
        print('Iniciando a função tratar_alarmes_04 - {}'.format(modo))
        print('--------------------------------------')

    # contador de alarmes registrados
    global contador

    # lista para armazenar os conteudos dos alarmes
    lista_alarmes = {}

    # remover linhas vazias
    texto_alarmes = [text for text in alarmes.splitlines() if text != '']

    # percorrer as linhas dos conteudos dos alarmes
    for i, text in enumerate(texto_alarmes):

            # extrair o conteudo dos alarmes
            value_content = content_alarmes_041(text)

            # extrair o numero dos alarmes
            value_numeros = numeros_alarmes_042(text)

            # verbose
            if verbose:
                print(i, ' : ')

            if value_content:
                # print(' '*5, value_content.groups())
                index = value_content.groups()[0]
                indice = value_content.groups()[1].replace(']', '')
                mensagem = f'{indice}]: <UG> - {value_content.groups()[2]}'
                if verbose:
                    print(' '*5,index, mensagem)
                if lista_alarmes.get(index, True):
                    lista_alarmes[index] = {'Category': categoria,
                                            'PLC Name (Read)': None,
                                            'Address (Read)': None,
                                            'Content': mensagem,
                                            'Address (Condition)': None,
                                            'PLC Name (Condition)': None}
                else:
                    print('Possível erro, valor preenchido: ', index, mensagem, lista_alarmes.get(index, False))

            if value_numeros and not value_content:
                contador += 1
                index = value_numeros.groups()[0]
                indice = value_numeros.groups()[1].replace(']', '')
                mensagem = f'{indice}]: <UG> - Reserva - {contador}'
                if verbose:
                    print(' '*5, index, mensagem)

                if lista_alarmes.get(index, True):
                    lista_alarmes[index] = {'Category': categoria,
                                            'PLC Name (Read)': None,
                                            'Address (Read)': None,
                                            'Content': mensagem,
                                            'Address (Condition)': None,
                                            'PLC Name (Condition)': None}
                else:
                    print('Possível erro, valor preenchido: ', index, mensagem, lista_alarmes.get(index, False))
    return lista_alarmes



def tratar_address_03(address, verbose=True):
    ''' Função para tratar os address dos alarmes'''

    if verbose:
        print('--------------------------------------')
        print('Iniciando a função tratar_address_03')
        print('--------------------------------------')
        print(address)
        print('--------------------------------------')

    # padrão regex para seperar o address dos alarmes
    padrao_address = r'\(\*\s*(\w+)\s*\*\)\s+(\w+)\s+'

    # lista para armazenar os address dos alarmes
    lista_enderecos = {}

    # remover linhas vazias
    texto_enderecos = [text for text in address.splitlines() if text != '']

    # percorrer as linhas dos endereços dos alarmes
    for i, text in enumerate(texto_enderecos):

        # extrair o address dos alarmes
        value = re.search(padrao_address, text)

        # verificar se o address foi encontrado
        if value:
            # separar o numero, tipo e address
            numero = value.group(2).split('_')[1].zfill(3)
            tipo = value.group(1)[0:2]
            address = value.group(1)[2::]

            if verbose:
                print(i,f'numero: {numero}, tipo: {tipo}, address: {address}')

            # adicionar o address na lista em formato de dicionário
            lista_enderecos[numero] = {'tipo': tipo, 'address': address}
        else:
            if verbose:
                print('Não encontrado: ', text)
    if verbose:
        print('--------------------------------------')
        print('Fim da função tratar_address_03')
        print('--------------------------------------')

    return lista_enderecos




def info_df_02(df, line=0, nan=False, verbose=False):
    ''' Função para contar a quantidade de valores nulos'''

    if verbose:
        print('--------------------------------------')
        print('Iniciando a função info_df_02')
        print('--------------------------------------')
        # imprimir o cabeçalho do arquivo xls
        print('-'*40)
        print('Info df - Shape: ',df.shape)
        cont = 0  # contador de valores nulos

        # percorrer as colunas do arquivo xls
        for i, s in enumerate(df.values[line]):

            # verificar se existe algum valor nulo e imprimir
            if not isinstance(s, float) and not nan:
                cont += 1
                print(i,' : ', cont, '  ', space_string_021(df.columns[i],40),space_string_021(s,15) ,' : ',type(s))
            else:
                cont += 1
                print(i,' : ', cont, '  ', space_string_021(df.columns[i],40),space_string_021(s,15) ,' : ',type(s))

        # imprimir o rodapé do arquivo xls
        print('-'*40)

def space_string_021(string, size):
    ''' Função para preencher com espaços uma string'''

    # converter para string
    string = str(string)

    # verificar o tamanho da string e preencher com espaços
    return string + ' '*(size - len(string))



def associar_address_alarmes_05(address, alarmes, ugs, verbose=False):
    ''' Função para associar os address aos alarmes'''

    if verbose:
        print('--------------------------------------')
        print('Iniciando a função associar_address_alarmes_05')
        print('--------------------------------------')

    # dicionário para armazenar os alarmes com os address
    dict_final = {}

    # contador de alarmes registrados
    global contador_01

    # lista para armazenar os alarmes com os address
    for modos in alarmes:
        for ug in ugs:
            for key, value in modos.items():
                if verbose:
                    print('Modo: ', key)
                for key_01, value_01 in value.items():

                    info_address = address.get(key_01, False)

                    ug_ = ug[0:4]

                    if not info_address:
                        raise Exception(f'Não encontrado: {key_01}')


                    if verbose:
                        print(' '*5, contador_01, key_01, ' : ', value_01)
                        print(' '*5, ug_)
                        print(' '*5, info_address)
                        print(' ')

                    dict_final[contador_01] = {'Category': value_01['Category'],
                                               'PLC Name (Read)': ug,
                                               'Address (Read)': info_address['address'],
                                               'Content': value_01['Content'].replace('<UG>', ug_),
                                               'Address (Condition)': info_address['address'],
                                               'PLC Name (Condition)': ug}

                    contador_01 += 1

    if verbose:
        print('--------------------------------------')
        print('Fim da função associar_address_alarmes_05')

    return dict_final

def substituir_por_null(df, verbose=False):
    ''' Função para substituir os valores por null'''

    if verbose:
        print('--------------------------------------')
        print('Iniciando a função substituir_por_null')
        print('--------------------------------------')

    # dict com os valores default null para algumas colunas
    dict_default = {'Index (Read)': 'null',
                    'Index (Notification)': 'null',
                    'Index (WATCH1)': 'null',
                    'Index (WATCH2)': 'null',
                    'Index (WATCH3)': 'null',
                    'Index (WATCH4)': 'null',
                    'Index (WATCH5)': 'null',
                    'Index (WATCH6)': 'null',
                    'Address (String ID)': 'null',
                    'Index (WATCH7)': 'null',
                    'Index (Occurrence)': 'null',
                    'Address (String ID)': 'null',
                    'Index (Condition)': 'null',
                    'Index (Elapsed Time)': 'null',
                    'Index (Enable/Disable)': 'null'}

    # percorrer as colunas do dataframe
    for key, value in dict_default.items():
        # substituir os valores por null
        df[key] = value
        print(' '*5, key, ' : ', value)

    return df

def transformar_dicionario_dataframe_06(dict_final, df_tratado, verbose=False):
    ''' Função para transformar o dicionário em um dataframe com valores default'''

    if verbose:
        print('--------------------------------------')
        print('Iniciando a função transformar_dicionario_dataframe_06')
        print('--------------------------------------')

    inicio = time.time()

    index = len(df_tratado)

    # criar um dataframe com os valores default
    for key, value in dict_final.items():
        index += 1
        for column in df_tratado.columns:
            if value.get(column, False):
                df_tratado.loc[index, column] = value[column]
                if index < 3:
                    print('Encontrado: ', column, value[column])
            else:
                df_tratado.loc[index, column] = df_tratado[column].values[0]
                if index < 3:
                    print('Não encontrado: ', column, df_tratado[column].values[0])

    if verbose:
        print('--------------------------------------')
        print('Fim da função transformar_dicionario_dataframe_06')
        print('Tempo de execução: ', round(time.time() - inicio, 7))

    return df_tratado


def comparar_tipos_dados(df, df_tratado, line=0, verbose=False):
    ''' Função para comparar os tipos de dados de cada coluna da linha passada como argumento'''

    if verbose:
        print('--------------------------------------')
        print('Iniciando a função comparar_tipos_dados')
        print('--------------------------------------')

    # percorrer as colunas do dataframe
    for column in df.columns:
        # verificar se o tipo de dado é diferente
        if type(df[column].values[line]) != type(df_tratado[column].values[line]):
            print(' '*5, column, ' : ', type(df[column].values[line]), ' : ', type(df_tratado[column].values[line]))

            # converter o tipo de dado
            try:
                df_tratado[column] = df_tratado[column].astype(type(df[column].values[line]))
                print(' ' * 5, column, ' : ', type(df[column].values[line]), ' : ', type(df_tratado[column].values[line]))
            except Exception as e:
                print('Erro: ', e)
        # else:
            # print(' '*5, column, ' : ', type(df[column].values[line]), ' : ', type(df_tratado[column].values[line]))

def main_tratamento_alarmes_01(usina):
    ''' Função principal para tratar os alarmes do arquivo xls'''

    inicio = time.time()

    # abrir o arquivo xls com o modelo do xls de alarmes
    df = pd.read_excel(usina['xls'], header=1)

    # verificar a quantidade de valores nulos e informacoes do arquivo xls
    info_df_02(df, line=0, nan=False, verbose=False)

    # prepara o dataframe para receber os dados tratados
    df_tratado = pd.DataFrame( columns=df.columns)

    # acrescenta 1 linha no dataframe do arquivo original
    df_tratado.loc[0] = df.loc[0].values
    df_tratado.loc[1] = df.loc[1].values

    # tratar os address dos alarmes
    address_tratado = tratar_address_03(usina['alarmes']['enderecos_alarmes'][0], verbose=True)

    # raise Exception('Finalizando o programa')

    # tratar os alarmes
    alarmes_tratados =[{ key: tratar_alarmes_04(value[0], key, value[1], verbose=True) for key, value in usina['alarmes'].items() if value[1]}]

    # raise Exception('Finalizando o programa')
    # Declarar as unidades geradoras
    ugs = [f'UG0{i+1}_750_862' for i in range(usina['nr_ugs'])]

    # Associar os address aos alarmes
    dict_final = associar_address_alarmes_05(address_tratado, alarmes_tratados, ugs, verbose=True)


    cont = 0
    print('--------------------------------------')
    print('Alarmes registrados no CLP e não encontrados no arquivo no Supervisorio')
    cont2 = 0
    for key2, value2 in dict_final.items():
        chave = True
        cont2 = 0
        for key1, value1 in df.iterrows():
            # print(key1, ' : ', value1)
            # print(key2, ' : ', type(value2['Address (Read)']), ' : ', type(value1['Address (Read)']))
            if int(value1['Address (Read)']) == int(value2['Address (Read)']):
                chave = False
                cont2 += 1
                numero_01 = value1['Content'].split(':')[0].split('[')[1].split(']')[0]
                numero_02 = value2['Content'].split(':')[0].split('[')[1].split(']')[0]
                print(' '*5, key1, ' 1 : ', value2['Address (Read)'],' : ', value1['Content'])
                if numero_02 != numero_01:
                    print(' '*5, key1, ' 1 : ', value1['Content'], ' : ', value2['Content'])
                    print(type(numero_01), ' : ', type(numero_02))
                # if cont2 > 1:
                #     print(' '*5, key1, ' 1 : ', value1['Content'], ' : ', value2['Content'])
                # print(key1, ' 1 : ',cont2, value1['Content'], ' : ', value2['Content'])
        if chave and not 'Reserva'.upper() in value2['Content'].upper():
            cont += 1
            print(cont, value2['Content'], ' : ', value2['Address (Read)'])
    # print('--------------------------------------')
    # print('Alarmes registrados no supervisorio e não encontrados no arquivo no CLP')
    #
    # for key2, value2 in df.iterrows():
    #     chave = True
    #     for key1, value1 in dict_final.items():
    #         # print(key1, ' : ', value1)
    #         # print(key2, ' : ', type(value2['Address (Read)']), ' : ', type(value1['Address (Read)']))
    #         if int(value1['Address (Read)']) == int(value2['Address (Read)']):
    #             chave = False
    #             # print(key1, ' 1 : ', value1['Content'], ' : ', value2['Content'])
    #     if chave and not 'Reserva'.upper() in value2['Content'].upper():
    #         cont += 1
    #         print(cont, value2['Content'], ' : ', value2['Address (Read)'])

    raise Exception('Finalizando o programa')

    # Transformar o dicionário em um dataframe
    df_tratado = transformar_dicionario_dataframe_06(dict_final, df_tratado, verbose=True)


    # # Visualizar o dataframe
    info_df_02(df_tratado, line=2, nan=False, verbose=False)

    info_df_02(df, line=1, nan=False, verbose=False)

    # função para comparar os tipos de dados de cada coluna da linha passada como argumento
    comparar_tipos_dados(df, df_tratado, line=5, verbose=True)

    # raise Exception('Finalizando o programa')

    # acrescentar ao dataframe tratado valores da coluna PLC Name (Read) diferentes das ugs declaradas
    # df_add = df[(df['PLC Name (Read)'] != ugs[0]) & (df['PLC Name (Read)'] != ugs[1])]
    df_add = df[(df['PLC Name (Read)'] != ugs[0])]

    # print('--------------------------------------')
    # print('Interno - PLC Name (Read): ', df_add['PLC Name (Read)'].value_counts())
    # # acrescentar ao dataframe tratado valores da coluna PLC Name (Read) diferentes das ugs declaradas
    df_tratado = pd.concat([df_tratado, df_add], axis=0)

    # reindexar o dataframe tratado
    df_tratado = df_tratado.reset_index(drop=True)

    # substituir os valores por null
    df_tratado = substituir_por_null(df_tratado, verbose=False)
    print('Final: --------------------------------------')
    print(df_tratado.head())
    print(df_tratado.shape)

    # Acrescentar ao dataframe 1 linha com os valores default
    linha = ['VERSION', str(3), 'HARDWARE_VERSION', str(70)]
    linha += [''] * (len(df_tratado.columns) - len(linha))
    df_tratado.loc[0] = linha

    # Acrescentar ao dataframe na 2 linha com os valores das colunas sem eliminar os valores anteriores
    df_tratado.loc[1] = df_tratado.columns

    # Salvar o dataframe em um arquivo xls
    df_tratado.to_excel(usina['xls_tratado'], index=False, header=False)

    # Visualizar a quantidade  de valores da coluna PLC Name (Read) 24289
    print('--------------------------------------')
    print('2 - PLC Name (Read): ', df['PLC Name (Read)'].value_counts())

    # Visualizar a quantidade  de valores da coluna PLC Name (Read)
    print('--------------------------------------')
    print('3 - PLC Name (Read): ', df_tratado['PLC Name (Read)'].value_counts())


    print('--------------------------------------')
    print('Fim da função main_tratamento_alarmes_01')
    print('Tempo de execução: ', round(time.time() - inicio, 7))

    # objetivo: gerar uma lista com os alarmes em data frame e salvar em um arquivo xls



if __name__ == '__main__':

    # definir interface de escolha da usina
    usinas = {
        'SaoSebastiao': {
            'path': 'libs/SaoSebastiao/',
            'alarmes': lista_modos_psa,
            'alarmes_tratados': None,
            'xls': r'libs/SaoSebastiao/saosebastiao_original.xls',
            'xls_tratado': r'libs/SaoSebastiao/saosebastiao_tratado.xlsx',
            'nr_ugs': 2
        },
        'PonteSerrada': {
            'path': 'libs/ponteSerrada/',
            'alarmes': lista_modos_psa,
            'alarmes_tratados': None,
            'xls': r'libs/ponteSerrada/ponteSerrada_original.xls',
            'xls_tratado': r'libs/ponteSerrada/ponteSerrada_tratado.xlsx',
            'nr_ugs': 1,
        },
    }

    # escolher a usina
    usina = usinas['PonteSerrada']

    # Tratar os alarmes
    alarmes_tratados = main_tratamento_alarmes_01(usina)

    # Comparar alarmes
    df = pd.read_excel(usina['xls'], header=1)

    df_t = pd.read_excel(usina['xls_tratado'], header=1)

    print('--------------------------------------')
    print('1 - PLC Name (Read): ', df['PLC Name (Read)'].value_counts())

    print('--------------------------------------')
    print('2 - PLC Name (Read): ', df_t['PLC Name (Read)'].value_counts())

    # for in lista_modos_psa

'''
------------------------------------------------------------------------
Alarmes registrados no supervisorio e não encontrados no arquivo no CLP
-----------------------------------------------------------------------
1 [04.00]: UG01 - UHLM - Temperatura Óleo Alta - TRIP  :  28691
2 [04.01]: UG01 - UHLM - Filtro Sujo - ALARME  :  28692
3 [04.02]: UG01 - UHLM - Trocador de Calor - ALARME  :  28693
4 [04.03]: UG01 - UHLM - Nível Mínimo de Óleo - ALARME  :  28694
5 [04.04]: UG01 - UHLM - Nível Máximo de Óleo - ALARME  :  28695
6 [04.05]: UG01 - UHLM - Linha Lubrificação - Falha Pressostato  :  28696
7 [04.06]: UG01 - UHLM - Falha Acionamento Bomba 01  :  28697
8 [04.07]: UG01 - UHLM -  Bomba 01 - TRIP  :  28698
9 [04.08]: UG01 - Trocador de Calor - Falha Acionamento Bomba 01  :  28699
10 [04.09]: UG01 - Trocador de Calor -  Bomba 01 - TRIP  :  28700
11 [04.10]: UG01 - UHLM -  Falta de Fluxo de Óleo  :  28701
12 [04.11]: UG01 - UHLM - Linha Lubrificação - Falta de Fluxo de Óleo Guia Escora LA  :  28702
13 [04.12]: UG01 - UHLM - Linha Lubrificação - Falta de Fluxo de Óleo Combinado LA  :  28703
14 [06.00]: UG01 - UHRV REXROTH - Falha Pressurização  :  28716
15 [06.01]: UG01 - UHRV REXROTH - Pressão Óleo Baixa - ALARME  :  28717
16 [06.02]: UG01 - UHRV REXROTH - Pressão Óleo Baixa - TRIP  :  28718
17 [06.03]: UG01 - UHRV REXROTH - Filtro de  Óleo Sujo - ALARME  :  28719
18 [06.04]: UG01 - UHRV REXROTH - Falha Acionamento Bomba  :  28720
19 [06.05]: UG01 - UHRV REXROTH - Nível Óleo Minimo - TRIP  :  28721
20 [06.06]: UG01 - UHRV REXROTH - Bomba 01 -TRIP  :  28722
21 [06.07]: UG01 - UHRV REXROTH - Bomba 02 -TRIP  :  28723
22 [06.08]: UG01 - UHRV REXROTH - Filtro de Saída Óleo Sujo - TRIP  :  28724
23 [06.09]: UG01 - UHRV REXROTH - Filtro de Saída Óleo Sujo - ALARME  :  28725
24 [06.10]: UG01 - UHRV REXROTH - Filtro de Retorno Óleo Sujo - TRIP  :  28726
25 [06.11]: UG01 - UHRV REXROTH - Filtro de Retorno Óleo Sujo - ALARME  :  28727
26 [06.12]: UG01 - UHRV REXROTH - Pressão Crítica - TRIP  :  28728
27 [07.00]: UG01 - TURBINA - Falha de Fechamento By-Pass  :  28730
28 [07.01]: UG01 - TURBINA - Falha de Abertura By-Pass  :  28731
29 [08.00]: UG01 - TURBINA - Falha de Abertura Borboleta  :  28732
30 [08.01]: UG01 - TURBINA - Falha de Fechamento Borboleta  :  28733
31 [08.02]: UG01 - TURBINA - Falha de Reposição Borboleta  :  28734
32 [08.03]: UG01 - TURBINA - Falha de Fins de Cursos  Borboleta  :  28735
33 [09.00]: UG01 - TURBINA - Falha Equalização  :  28736
34 [09.01]: UG01 - TURBINA - Falha de Sensores  :  28737
35 [09.02]: UG01 - TURBINA - Falha de Abertura do Rotor  :  28738
36 [09.03]: UG01 - Regulador Velocidade - Falha na Leitura do Encoder  :  28739
37 [03.00]: USINA - DisjQ380_01: Disjuntor Aberto  :  28676

Todos os alarmes registrados no CLP estão no arquivo do supervisorio

Todos os alarmes estão conferidos e registrados com address correto
'''
