# criar uma tabela online com os mesmos dados da tabela offline;
# criar um script em python que sincroniza os dados da tabela offline com a tabela online;
# criar um agendador de tarefas para executar o script de sincronizaçao no windows

# 1 - passo: criar uma tabela online com as mesmas colunas da tabela offline e criar tabela de sincronização offline; -> ok
'''
CREATE TABLE cgh_granada (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
ug01_status INT DEFAULT NULL,
 ug01_acumulador_energia FLOAT DEFAULT NULL,
 ug01_nivel_agua INT DEFAULT NULL,
 ug01_tensao_fase_A INT DEFAULT NULL,
 ug01_tensao_fase_B INT DEFAULT NULL,
 ug01_tensao_fase_C INT DEFAULT NULL,
 ug01_corrente_fase_A INT DEFAULT NULL,
 ug01_corrente_fase_B INT DEFAULT NULL,
 ug01_corrente_fase_C INT DEFAULT NULL,
 ug01_tensao_excitacao BIGINT DEFAULT NULL,
 ug01_corrente_excitacao BIGINT DEFAULT NULL,
 ug01_frequencia INT DEFAULT NULL,
 ug01_potencia_ativa BIGINT DEFAULT NULL,
 ug01_potencia_reativa BIGINT DEFAULT NULL,
 ug01_potencia_aparente BIGINT DEFAULT NULL,
 ug01_fp INT DEFAULT NULL,
 ug01_distribuidor FLOAT DEFAULT NULL,
 ug01_velocidade FLOAT DEFAULT NULL,
 ug01_horimetro_eletrico FLOAT DEFAULT NULL,
 ug01_temp_enrol_A FLOAT DEFAULT NULL,
 ug01_temp_enrol_B FLOAT DEFAULT NULL,
 ug01_temp_enrol_C FLOAT DEFAULT NULL,
 ug01_temp_nucl_estator FLOAT DEFAULT NULL,
 ug01_temp_cs FLOAT DEFAULT NULL,
 ug01_temp_manc_LNA_Ger FLOAT DEFAULT NULL,
 ug01_temp_manc_esc_LA FLOAT DEFAULT NULL,
 ug01_temp_Gax_LNA_Ger FLOAT DEFAULT NULL,
 ug01_temp_manc_LNA FLOAT DEFAULT NULL,
 ug01_temp_Gax_LNA_Turb FLOAT DEFAULT NULL,
 ug02_status INT DEFAULT NULL,
 ug02_acumulador_energia FLOAT DEFAULT NULL,
 ug02_tensao_fase_A INT DEFAULT NULL,
 ug02_tensao_fase_B INT DEFAULT NULL,
 ug02_tensao_fase_C INT DEFAULT NULL,
 ug02_corrente_fase_A INT DEFAULT NULL,
 ug02_corrente_fase_B INT DEFAULT NULL,
 ug02_corrente_fase_C INT DEFAULT NULL,
 ug02_tensao_excitacao BIGINT DEFAULT NULL,
 ug02_corrente_excitacao BIGINT DEFAULT NULL,
 ug02_frequencia INT DEFAULT NULL,
 ug02_potencia_ativa BIGINT DEFAULT NULL,
 ug02_potencia_reativa BIGINT DEFAULT NULL,
 ug02_potencia_aparente BIGINT DEFAULT NULL,
 ug02_fp INT DEFAULT NULL,
 ug02_distribuidor FLOAT DEFAULT NULL,
 ug02_velocidade FLOAT DEFAULT NULL,
 ug02_horimetro_eletrico FLOAT DEFAULT NULL,
 ug02_temp_enrol_A FLOAT DEFAULT NULL,
 ug02_temp_enrol_B FLOAT DEFAULT NULL,
 ug02_temp_enrol_C FLOAT DEFAULT NULL,
 ug02_temp_nucl_estator FLOAT DEFAULT NULL,
 ug02_temp_cs FLOAT DEFAULT NULL,
 ug02_temp_manc_LNA_Ger FLOAT DEFAULT NULL,
 ug02_temp_manc_esc_LA FLOAT DEFAULT NULL,
 ug02_temp_Gax_LNA_Ger FLOAT DEFAULT NULL,
 ug02_temp_manc_LNA FLOAT DEFAULT NULL,
 ug02_temp_Gax_LNA_Turb FLOAT DEFAULT NULL,
 data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE sincronizacao_cgh_sebastiao_paz_almeida(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
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

# 2.2 - passo: criar uma conexão com o banco de dados offline;
from libs.connection import DatabaseManager

try:
    with DatabaseManager(HOST_LOCAL, USER_LOCAL, PASSWORD_LOCAL, DATABASE_LOCAL, PORT_LOCAL) as db:
        print("2.3 - passo: verificar a ultima sincronização na tabela de sincronização offline- (ultimo ID sincronizado); \n")
        ultimo_id_sincronizado = db.read_data(TABLE_SINCRONIZACAO)
        if ultimo_id_sincronizado.empty:
            ultimo_id_sincronizado = 1
        else:
            ultimo_id_sincronizado = ultimo_id_sincronizado['id_sincronizado'].values[-1]
        print("Ultimo ID sincronizado: ", ultimo_id_sincronizado)
        print("2.4 - passo: ler os dados da tabela offline a partir do ultimo ID sincronizado; \n")
        dados_offline = db.read_where(TABLE, ultimo_id_sincronizado)
        print("Dados offline: ", dados_offline)
except Exception as e:
    logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
    raise



try:
    print("2.5 - passo: criar uma conexão com o banco de dados online;\n")
    with DatabaseManager(HOST_REMOTE, USER_REMOTE, PASSWORD_REMOTE, DATABASE_REMOTE, PORT_REMOTE) as db:
        dados_online = db.las_index(TABLE)
        if not dados_offline.empty:
            print("2.6 - passo: inserir os dados da tabela offline na tabela online;")
            db.insert_data(TABLE, dados_offline.columns.tolist(), dados_offline.values.tolist())
            print("Ultimo ID sincronizado online: ", dados_online)

except Exception as e:
    logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
    raise


try:
    print("2.7 - passo: atualizar a tabela de sincronização offline com o ultimo ID sincronizado e a quantidade de registros sincronizados;\n")
    with DatabaseManager(HOST_LOCAL, USER_LOCAL, PASSWORD_LOCAL, DATABASE_LOCAL, PORT_LOCAL) as db:
        if dados_offline.empty:
            print("Ultimo ID sincronizado online: ", dados_online)
            print("Ultimo ID sincronizado offline: ", ultimo_id_sincronizado)
        else:
            ultimo_id_sincronizado = dados_offline['id'].values[-1]
            qtd_registros_sincronizados = dados_offline.shape[0]
            print("Ultimo ID sincronizado: ", ultimo_id_sincronizado)
            print("Quantidade de registros sincronizados: ", qtd_registros_sincronizados)
            db.insert_sincronizacao(TABLE_SINCRONIZACAO,(ultimo_id_sincronizado, qtd_registros_sincronizados))
except Exception as e:
    logging.error(f'Erro ao conectar com o banco de dados offline: {e}')
    raise

