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
            'path': 'libs/jasp/',
            'tags': TagsJasp,
            'tags_tratadas': None,
            'csv': 'libs/jasp/tags_original.csv',
            'csv_tratado': 'libs/jasp/tags_tratadas.csv',
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
    # # seleciona a usina
    # usina = usinas['Frozza']
    #
    # # lê as variáveis do arquivo e trata os dados
    # usina['tags_tratadas'] = tratamento_tags(usina, verbose=False)
    #
    # # # implementa as tags no arquivo no formato csv
    # implementar_tags_no_csv(usina, verbose=True)
    #
    # # compara os arquivos csv
    # mainCompararCsv(usina['csv'], usina['csv_tratado'], verbose=True)


# problema do banco 
dict_modelo = {
    # q: preciso gerar chave valor no modelo abaixo
    '09/11/2023 23:50': 25,
    '09/11/2023 23:51': 26,
    '09/11/2023 23:52': 27,
    '09/11/2023 23:53': 0,
    '09/11/2023 23:54': 29,
    '10/11/2023 16:01': 35,
    '10/11/2023 16:02': 36,
    '10/11/2023 16:03': 37,
    '10/11/2023 16:04': 38,
    '10/11/2023 16:05': 39,
}

for data, valor in dict_modelo.items():
    print(data, valor)


# quantas bolitas foram acrescentadas hj para os dados do dict_modelo ?

# qual é formula para responde essa questão.

