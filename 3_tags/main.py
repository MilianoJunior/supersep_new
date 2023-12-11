from libs.funcoes import *
import sys
import os

# current_path = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(current_path, "libs"))



if __name__ == '__main__':

    print("Diretório atual:", os.getcwd())
    current_path = os.path.dirname(os.path.abspath(__file__))
    print('Psta: ',os.path.join(current_path, "libs"))
    abs_path = os.path.join(current_path, "libs")
    usinas = {
        'JASP': {
            'path': os.path.join(current_path, "libs","jasp"),
            'tags': TagsJasp,
            'tags_tratadas': None,
            'csv': os.path.join(current_path, "libs","jasp","tags_original.csv"),
            'csv_tratado': os.path.join(current_path, "libs","jasp","tags_tratadas.csv"),
            'nr_ugs': 4
        },
        'SaoSebastiao': {
            'path': 'libs/sao_sebastiao/',
            'tags': TagsSaoSebastiao,
            'tags_tratadas': None,
            'csv': 'libs/sao_sebastiao/tags_modificadas_2.csv',
            'csv_tratado': 'libs/sao_sebastiao/tags_tratadas.csv',
            'nr_ugs': 2
        },
        'Frozza':{
            'path': os.path.join(current_path, "libs","frozza"),
            'tags': TagsFrozza,
            'tags_tratadas': None,
            'csv': os.path.join(current_path, "libs","frozza","tags_modificadas.csv"),
            'csv_tratado': os.path.join(current_path, "libs","frozza","tags_tratadas.csv"),
            'nr_ugs': 1
        }

    }

    # seleciona a usina
    usina = usinas['JASP']

    # lê as variáveis do arquivo e trata os dados
    usina['tags_tratadas'] = tratamento_tags(usina, verbose=False)

    # # implementa as tags no arquivo no formato csv
    implementar_tags_no_csv(usina, verbose=True)
    #
    # # compara os arquivos csv
    mainCompararCsv(usina['csv'], usina['csv_tratado'], verbose=True)


# problema do banco 
# dict_modelo = {
#     # q: preciso gerar chave valor no modelo abaixo
#     '09/11/2023 23:50': 25,
#     '09/11/2023 23:51': 26,
#     '09/11/2023 23:52': 27,
#     '09/11/2023 23:53': 0,
#     '09/11/2023 23:54': 29,
#     '10/11/2023 16:01': 35,
#     '10/11/2023 16:02': 36,
#     '10/11/2023 16:03': 37,
#     '10/11/2023 16:04': 38,
#     '10/11/2023 17:05': 0,
#     '11/11/2023 16:01': 39,
#     '11/11/2023 16:02': 40,
#     '11/11/2023 16:03': 41,
#     '11/11/2023 16:04': 42,
#     '11/11/2023 16:05': 49,
#     '25/11/2023 17:05': 89,
#     '25/11/2023 16:01': 90,
#     '25/11/2023 16:02': 91,
#     '25/11/2023 16:03': 92,
#     '25/11/2023 16:04': 93,
#     '25/11/2023 16:05': 0,
# }
#
# # mostrar os dados do dict_modelo
# for key, value in dict_modelo.items():
#     print(key, value)
#
# # mostrar os valores do dict_modelo
# for value in dict_modelo.values():
#     print(value)
#
# # mostrar as chaves do dict_modelo
# for key in dict_modelo.keys():
#     print(key)
#
# # quantas bolitas foram acrescentadas hj para os dados do dict_modelo ?
#
#
# # Formula: A diferença entre o valor atual e o valor anterior
# import pandas as pd
#
# df = pd.DataFrame(dict_modelo.items(), columns=['data', 'valor'])
#
# # a última linha do dia atual
# # tem que ser diferente de zero
# valor1 = df['valor'].iloc[-1]
# cont = 0
# while valor1 == 0:
#     cont -= 1
#     valor1 = df['valor'].iloc[cont]
#     print(valor1)
# print(f'Esse é o último valor do dia atual: {valor1}')
#
# # a última linha do dia anterior
# # tem que ser diferente de zero
# data_atual = df['data'].iloc[-1].split(' ')[0]
# data_anterior = df['data'].iloc[-2].split(' ')[0]
#
# while data_atual == data_anterior:
#     cont -= 1
#     data_anterior = df['data'].iloc[cont].split(' ')[0]
#     print(data_atual, data_anterior, cont)








# qual é formula para responde essa questão.

