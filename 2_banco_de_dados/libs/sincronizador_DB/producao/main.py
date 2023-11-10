# criar uma tabela online com os mesmos dados da tabela offline;
# criar um script em python que sincroniza os dados da tabela offline com a tabela online;
# criar um agendador de tarefas para executar o script de sincronizaçao no windows

# 1 - passo: criar uma tabela online com as mesmas colunas da tabela offline e criar tabela de sincronização offline; -> ok
'''
# gerar o script de criação da tabela offline;

CREATE TABLE sincronizacao_cgh_sebastiao_paz_almeida (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_sincronizado INT DEFAULT NULL,
qtd_registros_sincronizados INT DEFAULT NULL,
data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);
'''
# 2 - passo: criar um script em python que sincroniza os dados da tabela offline com a tabela online;
# 2.1 - passo: importar as credenciais do banco de dados offline e online;
import logging  # debug(), info(), warning(), error() and critical().
from dotenv import load_dotenv
import os
import warnings
from datetime import datetime

# Suprimir os avisos do pandas sobre conexões DBAPI2
warnings.simplefilter(action='ignore', category=UserWarning)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv()
logging.basicConfig(filename='sincronizacao.log', encoding='utf-8', level=logging.DEBUG)

HOST_LOCAL = os.getenv('HOST_LOCAL')
USER_LOCAL = os.getenv('USER_LOCAL')
PASSWORD_LOCAL = os.getenv('PASSWORD_LOCAL')
DATABASE_LOCAL = os.getenv('DATABASE_LOCAL')
PORT_LOCAL = os.getenv('PORT_LOCAL')
TABLE = os.getenv('TABLE')
TABLE_SINCRONIZACAO = os.getenv('TABLE_SINCRONIZACAO_LOCAL')

HOST_REMOTE = os.getenv('HOST_REMOTE')
USER_REMOTE = os.getenv('USER_REMOTE')
PASSWORD_REMOTE = os.getenv('PASSWORD_REMOTE')
DATABASE_REMOTE = os.getenv('DATABASE_REMOTE')
PORT_REMOTE = os.getenv('PORT_REMOTE')

scape = True


from libs.connection import DatabaseManager

data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# try:
#     with DatabaseManager(HOST_LOCAL, USER_LOCAL, PASSWORD_LOCAL, DATABASE_LOCAL, PORT_LOCAL) as db:
#         print("verificar os nomes das colunas da tabela offline; \n")
#         colunas_offline = db.get_columns(TABLE)
#         dados_offline = db.read_data(TABLE)
#         # print(colunas_offline)
#         colunas_reverse = []
#         for coluna in colunas_offline:
#             name = db.reverse_rename(coluna[0])
#             name = coluna[0] if name is None else name
#             colunas_reverse.append((name, coluna[1], coluna[2], coluna[3], coluna[4], coluna[5]))
#             # print(coluna)
#         print(colunas_reverse)
#
#         # print("2.3 - passo: verificar a ultima sincronização na tabela de sincronização offline- (ultimo ID sincronizado); \n")
#         # ultimo_id_sincronizado = db.read_data(TABLE_SINCRONIZACAO)
#         # if ultimo_id_sincronizado.empty:
#         #     ultimo_id_sincronizado = 1
#         # else:
#         #     ultimo_id_sincronizado = ultimo_id_sincronizado['id_sincronizado'].values[-1]
#         # print("Ultimo ID sincronizado: ", ultimo_id_sincronizado)
#         # print("2.4 - passo: ler os dados da tabela offline a partir do ultimo ID sincronizado; \n")
#         # dados_offline = db.read_where(TABLE, ultimo_id_sincronizado)
#         # logging.info(f'Última sincronização captada: {ultimo_id_sincronizado}')
# except Exception as e:
#     logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
#     raise


try:
    print("2.5 - passo: criar uma conexão com o banco de dados online;\n")
    with DatabaseManager(HOST_REMOTE, USER_REMOTE, PASSWORD_REMOTE, DATABASE_REMOTE, PORT_REMOTE) as db:
        colunas_online = db.get_columns(TABLE)
        # dados_online = db.read_where(TABLE, 6000)
        dados_online = db.read_data(TABLE)
        dados_online.to_csv('cgh_fae.csv', index=False)

        # print(colunas_online)
        # dados_online = db.las_index(TABLE)
        # if not dados_offline.empty:
        #     print("2.6 - passo: inserir os dados da tabela offline na tabela online;")
        #     db.insert_data(TABLE, dados_offline.columns.tolist(), dados_offline.values.tolist())
        #     print("Ultimo ID sincronizado online: ", dados_online)
except Exception as e:
    logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
    raise

'''
# verificar os tipos de dados das colunas da tabela offline;
dtypes_off = dados_offline.dtypes.to_dict()
print(dtypes_off)
# verificar os tipos de dados das colunas da tabela online;
dtypes_on = dados_online.dtypes.to_dict()
print(dtypes_on)



# for new, antigo in novo.items():
#     if antigo is None:
#         insercao[new] = 0
#     else:
#         insercao[new] = dados_online[antigo].values[i]
novo = {
    'id':'id',
    'ug01_status':'ug01_status',
    'ug01_acumulador_energia':'ug01_acumulador_energia',
    'ug01_nivel_agua':'ug01_nivel_agua',
    'ug01_tensao_fase_A':'ug01_tensao_fase_A',
    'ug01_tensao_fase_B':'ug01_tensao_fase_B',
    'ug01_tensao_fase_C':'ug01_tensao_fase_C',
    'ug01_corrente_fase_A':'ug01_corrente_fase_A',
    'ug01_corrente_fase_B':'ug01_corrente_fase_B',
    'ug01_corrente_fase_C':'ug01_corrente_fase_C',
    'ug01_tensao_excitacao':'ug01_tensao_excitacao',
    'ug01_corrente_excitacao':'ug01_corrente_excitacao',
    'ug01_frequencia':'ug01_frequencia',
    'ug01_potencia_ativa':'ug01_potencia_ativa',
    'ug01_potencia_reativa':'ug01_potencia_reativa',
    'ug01_potencia_aparente':'ug01_potencia_aparente',
    'ug01_fp':'ug01_fp',
    'ug01_distribuidor':'ug01_distribuidor',
    'ug01_velocidade':'ug01_velocidade',
    'ug01_horimetro_mecanico': None,
    'ug01_horimetro_eletrico': 'ug01_horimetro',
    'ug01_temp_enrol_A': 'ug01_tensao_fase_A',
    'ug01_temp_enrol_B': 'ug01_tensao_fase_B',
    'ug01_temp_enrol_C': 'ug01_tensao_fase_C',
    'ug01_temp_mancal_estat': 'ug01_temp_nucleo_estator',
    'ug01_temp_mancal_comb': 'ug01_temp_guia_comb',
    'ug01_temp_mancal_escora': 'ug01_temp_comb_escora',
    'ug01_temp_oleo_uhrv': 'ug01_temp_oleo_UHRV',
    'ug01_temp_oleo_uhlm': 'ug01_temp_oleo_UHLM',
    'ug01_temp_csu2': None,
    'ug01_temp_excitatriz': None,
    'ug01_vibr_mancal_guia_x': 'ug01_vibracao_guia_x',
    'ug01_vibr_mancal_guia_Y': 'ug01_vibracao_guia_y',
    'ug01_vibr_mancal_comb_X': 'ug01_vibracao_comb_x',
    'ug01_vibr_mancal_comb_Y': 'ug01_vibracao_comb_y',
    'ug01_vibr_mancal_comb_Z': 'ug01_vibracao_comb_z',
    'ug01_corrente_linha_A': None,
    'ug01_corrente_linha_B': None,
    'ug01_corrente_linha_C': None,
    'ug01_corrente_seq_P': None,
    'ug01_corrente_seq_N': None,
    'ug01_corrente_seq_Z': None,
    'ug01_tensao_barra': None,
    'ug01_tensao_te': None,
    'ug02_status':'ug02_status',
    'ug02_acumulador_energia':'ug02_acumulador_energia',
    'ug02_tensao_fase_A':'ug02_tensao_fase_A',
    'ug02_tensao_fase_B':'ug02_tensao_fase_B',
    'ug02_tensao_fase_C':'ug02_tensao_fase_C',
    'ug02_corrente_fase_A':'ug02_corrente_fase_A',
    'ug02_corrente_fase_B':'ug02_corrente_fase_B',
    'ug02_corrente_fase_C':'ug02_corrente_fase_C',
    'ug02_tensao_excitacao':'ug02_tensao_excitacao',
    'ug02_corrente_excitacao':'ug02_corrente_excitacao',
    'ug02_frequencia':'ug02_frequencia',
    'ug02_potencia_ativa':'ug02_potencia_ativa',
    'ug02_potencia_reativa':'ug02_potencia_reativa',
    'ug02_potencia_aparente':'ug02_potencia_aparente',
    'ug02_fp':'ug02_fp',
    'ug02_distribuidor':'ug02_distribuidor',
    'ug02_velocidade':'ug02_velocidade',
    'ug02_horimetro_mecanico': None,
    'ug02_horimetro_eletrico': 'ug02_horimetro',
    'ug02_temp_enrol_A': 'ug02_tensao_fase_A',
    'ug02_temp_enrol_B': 'ug02_tensao_fase_B',
    'ug02_temp_enrol_C': 'ug02_tensao_fase_C',
    'ug02_temp_mancal_estat': 'ug02_temp_nucleo_estator',
    'ug02_temp_mancal_comb': 'ug02_temp_guia_comb',
    'ug02_temp_mancal_escora': 'ug02_temp_comb_escora',
    'ug02_temp_oleo_uhrv': 'ug02_temp_oleo_UHRV',
    'ug02_temp_oleo_uhlm': 'ug02_temp_oleo_UHLM',
    'ug02_temp_csu2': None,
    'ug02_temp_excitatriz': None,
    'ug02_vibr_mancal_guia_x': 'ug02_vibracao_guia_x',
    'ug02_vibr_mancal_guia_Y': 'ug02_vibracao_guia_y',
    'ug02_vibr_mancal_comb_X': 'ug02_vibracao_comb_x',
    'ug02_vibr_mancal_comb_Y': 'ug02_vibracao_comb_y',
    'ug02_vibr_mancal_comb_Z': 'ug02_vibracao_comb_z',
    'data_hora':'data_hora',
}
valores = list(dtypes_off.values())
keys = list(dtypes_on.keys())
cont = 0
for key, value in novo.items():

    print(cont, key, valores[cont])
    cont += 1
#     else:
#         print(cont, key, dtypes_on[value].dtype)
        # print(dir(dtypes_on[value]))
dados_online['ug01_status'] = dados_online['ug01_status'].values.astype(np.int64)
dados_online['ug02_status'] = dados_online['ug02_status'].values.astype(np.int64)
if scape:
    import pandas as pd
    print(pd.__version__)
    insercao = {}
    print('Antes: ',dados_offline.shape)
    print(type(dados_offline))
    dados_a_adicionar = []

    for i in range(dados_online.shape[0]):
        insercao = {}
        if i % 1000 == 0:
            print(i)
        cont = 0
        for new, antigo in novo.items():
            tipo = valores[cont]
            if antigo is None:
                conversao = 0
                insercao[new] = conversao
            else:
                conversao = dados_online[antigo].values[i]
                insercao[new] = conversao
        # Adicionar o dicionário insercao à lista
        # print(insercao)
        dados_a_adicionar.append(insercao)
    # Converta a lista de dicionários em um DataFrame
    df_insercao = pd.DataFrame(dados_a_adicionar)
    print(dados_offline.columns)
    print(df_insercao.columns)
    # mas recebi o seguinte erro, pode me ajudar?
    df_insercao.columns = dados_offline.columns
    # print('    ')
    # print(dados_offline.columns)
    # print(df_insercao.columns)
    dados_offline = pd.concat([dados_offline, df_insercao], ignore_index=True)
    # print(dados_offline.shape)
    # print(df_insercao.shape)

    # dados_offline = pd.concat([dados_offline, df_insercao], ignore_index=True)
    print('Depois: ',dados_offline.shape)
    dados_offline ['data_hora'] = pd.to_datetime(dados_offline ['data_hora'])
    df_sorted = dados_offline.sort_values(by='data_hora')
    df_sorted = df_sorted.reset_index(drop=True)
    df_sorted = df_sorted.drop(columns=['id'])
    print('Depois 2: ',df_sorted.shape)
    print(df_sorted.columns)
    print(df_sorted.head())
    print(df_sorted.dtypes)
    del dtypes_off['id']

    tipos = df_sorted.dtypes.to_dict()
    chaves_off = list(dtypes_off.keys())
    chaves_on = list(tipos.keys())
    val_off = list(dtypes_off.values())
    val_on = list(tipos.values())
    print('    ')
    print('Valores diferentes: ')
    for s in range(0,len(dtypes_off)):
        if val_off[s] != val_on[s]:
            print(chaves_off[s], val_off[s], chaves_on[s], val_on[s])

    print(df_sorted.values[0])
    print(df_sorted.values[-1])
        # print(chaves_off[s], val_off[s], chaves_on[s], val_on[s])
    try:
        with DatabaseManager(HOST_LOCAL, USER_LOCAL, PASSWORD_LOCAL, DATABASE_LOCAL, PORT_LOCAL) as db:
            print("verificar os nomes das colunas da tabela offline; \n")
            colunas_offline = db.get_columns(TABLE)
            db.delete_data(TABLE)
            colunas = []
            for coluna in colunas_offline:
                if coluna[0] != 'id':
                    colunas.append(coluna[0])

            print(colunas)
            db.insert_data(TABLE, colunas, df_sorted.values.tolist())
    except Exception as e:
        logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
        raise


# # 2.2 - passo: criar uma conexão com o banco de dados offline;
# from libs.connection import DatabaseManager
#
# data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# try:
#     with DatabaseManager(HOST_LOCAL, USER_LOCAL, PASSWORD_LOCAL, DATABASE_LOCAL, PORT_LOCAL) as db:
#         print("2.3 - passo: verificar a ultima sincronização na tabela de sincronização offline- (ultimo ID sincronizado); \n")
#         ultimo_id_sincronizado = db.read_data(TABLE_SINCRONIZACAO)
#         if ultimo_id_sincronizado.empty:
#             ultimo_id_sincronizado = 1
#         else:
#             ultimo_id_sincronizado = ultimo_id_sincronizado['id_sincronizado'].values[-1]
#         print("Ultimo ID sincronizado: ", ultimo_id_sincronizado)
#         print("2.4 - passo: ler os dados da tabela offline a partir do ultimo ID sincronizado; \n")
#         dados_offline = db.read_where(TABLE, ultimo_id_sincronizado)
#         logging.info(f'Última sincronização captada: {ultimo_id_sincronizado}')
# except Exception as e:
#     logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
#     raise
#
#
# try:
#     print("2.5 - passo: criar uma conexão com o banco de dados online;\n")
#     with DatabaseManager(HOST_REMOTE, USER_REMOTE, PASSWORD_REMOTE, DATABASE_REMOTE, PORT_REMOTE) as db:
#         dados_online = db.las_index(TABLE)
#         if not dados_offline.empty:
#             print("2.6 - passo: inserir os dados da tabela offline na tabela online;")
#             db.insert_data(TABLE, dados_offline.columns.tolist(), dados_offline.values.tolist())
#             print("Ultimo ID sincronizado online: ", dados_online)
# except Exception as e:
#     logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
#     raise
#
# try:
#     print("2.7 - passo: atualizar a tabela de sincronização offline com o ultimo ID sincronizado e a quantidade de registros sincronizados;\n")
#     with DatabaseManager(HOST_LOCAL, USER_LOCAL, PASSWORD_LOCAL, DATABASE_LOCAL, PORT_LOCAL) as db:
#         if dados_offline.empty:
#             print("Ultimo ID sincronizado online: ", dados_online)
#             print("Ultimo ID sincronizado offline: ", ultimo_id_sincronizado)
#         else:
#             ultimo_id_sincronizado = dados_offline['id'].values[-1]
#             qtd_registros_sincronizados = dados_offline.shape[0]
#             print("Ultimo ID sincronizado: ", ultimo_id_sincronizado)
#             print("Quantidade de registros sincronizados: ", qtd_registros_sincronizados)
#             db.insert_sincronizacao(TABLE_SINCRONIZACAO,(ultimo_id_sincronizado, qtd_registros_sincronizados))
# except Exception as e:
#     logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
#     raise
# logging.info(f'Sincronização realizada com sucesso: {data_hora}')
'''