'''
Sincronizaçao do banco de dados.

Tenho um banco de dados onffline no wampserver, e um banco de dados online no servidor da railway.
O banco de dados online é uma cópia do banco de dados offline, os dados da tabela vai ser exclusivamneto do banco offline.
Quais as melhores formas de sincronizar os dois bancos de dados?
1- Backup e Restauração Manual;
2- Ferramentas de Sincronização de Banco de Dados;
3- Triggers e Log Shipping;
4- APIs e Webhooks;
5- Replicação;
# -------------------------------
# soluçao:
        # criar uma tabela online com os mesmos dados da tabela offline;
        # criar um script em python que sincroniza os dados da tabela offline com a tabela online;
        # criar um agendador de tarefas para executar o script de sincronizaçao no windows
'''
# 1 - passo: criar uma tabela online com as mesmas colunas da tabela offline; -> ok
'''
CREATE TABLE cgh_maria_luz (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
ug01_nivel_agua INT DEFAULT NULL,
ug01_tensao_fase_A INT DEFAULT NULL,
ug01_tensao_fase_B INT DEFAULT NULL,
ug01_tensao_fase_C INT DEFAULT NULL,
ug01_corrente_fase_A INT DEFAULT NULL,
ug01_corrente_fase_B INT DEFAULT NULL,
ug01_corrente_fase_C INT DEFAULT NULL,
ug01_tensao_excitacao INT DEFAULT NULL,
ug01_corrente_excitacao INT DEFAULT NULL,
ug01_frequencia INT DEFAULT NULL,
ug01_potencia_ativa BIGINT DEFAULT NULL,
ug01_potencia_reativa BIGINT DEFAULT NULL,
ug01_potencia_aparente BIGINT DEFAULT NULL,
ug01_fp INT DEFAULT NULL,
ug01_pressao_jusante INT DEFAULT NULL,
ug01_distribuidor INT DEFAULT NULL,
ug01_velocidade INT DEFAULT NULL,
ug01_horimetro FLOAT DEFAULT NULL,
ug01_acumulador_energia FLOAT DEFAULT NULL,
ug01_temp_mancal_ger INT DEFAULT NULL,
ug01_temp_mancal_comb_ger INT DEFAULT NULL,
ug01_temp_mancal_tub INT DEFAULT NULL,
ug01_temp_mancal_comb_tub INT DEFAULT NULL,
ug01_status INT DEFAULT NULL,
data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);
'''
# 2 - passo: criar um script em python que sincroniza os dados da tabela offline com a tabela online;
    # CRIAR UMA CLASSE QUE SE CONECTA AO BANCO DE DADOS;