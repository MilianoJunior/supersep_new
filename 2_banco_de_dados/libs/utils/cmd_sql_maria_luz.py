
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

tags_UG01 = {
    'ug01_nivel_agua':['USINA_750_862','UG01_Leitura.QTA_NivelMontante','13569','Nível Água','32-bit Signed','INT'],
    'ug01_tensao_fase_A':['UG01_750_862','UG01_Leitura.REG615_U_FaseAB','13599','UG-01 Tensão Fase A','16-bit Signed','INT'],
    'ug01_tensao_fase_B':['UG01_750_862','UG01_Leitura.REG615_U_FaseBC','13600','UG-01 Tensão Fase B','16-bit Signed','INT'],
    'ug01_tensao_fase_C':['UG01_750_862','UG01_Leitura.REG615_U_FaseCA','13601','UG-01 Tensão Fase C','16-bit Signed','INT'],
    'ug01_corrente_fase_A':['UG01_750_862','UG01_Leitura.REG615_I_INST_A','13605','UG-01 Corrente Fase A','16-bit Signed','INT'],
    'ug01_corrente_fase_B':['UG01_750_862','UG01_Leitura.REG615_I_INST_B','13606','UG-01 Corrente Fase B','16-bit Signed','INT'],
    'ug01_corrente_fase_C':['UG01_750_862','UG01_Leitura.REG615_I_INST_C','13607','UG-01 Corrente Fase C','16-bit Signed','INT'],
    'ug01_tensao_excitacao':['UG01_750_862','UG01_Leitura.Gerador_ExcitacaoTensao','13597','UG-01 Tensão Excitação','16-bit Signed','INT'],
    'ug01_corrente_excitacao':['UG01_750_862','UG01_Leitura.Gerador_ExcitacaoCorrente','13598','UG-01 Corren. Excitação','16-bit Signed','INT'],
    'ug01_frequencia':['UG01_750_862','UG01_Leitura.REG615_FHz_INST','13613','UG-01 Frequência','16-bit Signed','INT'],
    'ug01_potencia_ativa':['UG01_750_862','UG01_Leitura.REG615_P_INST','13609','UG-01 Potência Ativa','32-bit Unsigned',
                           'BIGINT'],
    'ug01_potencia_reativa':['UG01_750_862','UG01_Leitura.REG615_Q_INST','13610','UG-01 Potência Reativa','32-bit Unsigned',
                             'BIGINT'],
    'ug01_potencia_aparente':['UG01_750_862','UG01_Leitura.REG615_S_INST','13611','UG-01 Potência Aparente',
                              '32-bit Unsigned','BIGINT'],
    'ug01_fp':['UG01_750_862','UG01_Leitura.REG615_PF_INST','13612','UG-01 Fator de Potência','16-bit Signed','INT'],
    'ug01_pressao_jusante':['UG01_750_862','UG01_Leitura.Turbina_PressaoMontante','13590','UG-01 Pressão Montante','16-bit Signed','INT'],
    'ug01_distribuidor':['UG01_750_862','UG01_Leitura.Turbina_PosicaoDistribuidor','13593','UG-01 Distribuidor','16-bit Signed','INT'],
    'ug01_velocidade':['UG01_750_862','UG01_Leitura.Turbina_Velocidade','13595','UG-01 Velocidade RPM','16-bit Signed','INT'],
    'ug01_horimetro':['UG01_750_862','UG01_Setpoint.Horimetro_Eletrico','12894','UG-01 Horimetro','32-bit Float','FLOAT'],
    'ug01_acumulador_energia':['UG01_750_862','UG01_Leitura.Gerador_EnergiaFornecidakWh','12843','UG-01 Acum. Energia','32-bit Float','FLOAT'],
    'ug01_temp_mancal_ger':['UG01_750_862','UG01_Leitura.RIO600_MOD1_RTD1','13574','UG-01 Temp. Fase A','16-bit Signed',
                            'INT'],
    'ug01_temp_mancal_comb_ger':['UG01_750_862','UG01_Leitura.RIO600_MOD1_RTD1','13574','UG-01 Temp. Fase A',
                                 '16-bit Signed','INT'],
    'ug01_temp_mancal_tub':['UG01_750_862','UG01_Leitura.RIO600_MOD1_RTD1','13574','UG-01 Temp. Fase A','16-bit Signed',
                            'INT'],
    'ug01_temp_mancal_comb_tub':['UG01_750_862','UG01_Leitura.RIO600_MOD1_RTD1','13574','UG-01 Temp. Fase A',
                                 '16-bit Signed',
                                 'INT'],
    'ug01_status':['UG01_750_862','UG01_Leitura.TurbinaParada','13617','UG-01 Mancal Guia X','16-bit Signed',
                            'INT'],
    # 'ug01_temp_fase_A':['UG01_750_862','UG01_Leitura.RIO600_MOD1_RTD1','13574','UG-01 Temp. Fase A','16-bit Signed','INT'],
    # 'ug01_temp_fase_B':['UG01_750_862','UG01_Leitura.RIO600_MOD1_RTD2','13575','UG-01 Temp. Fase B','16-bit Signed','INT'],
    # 'ug01_temp_fase_C':['UG01_750_862','UG01_Leitura.RIO600_MOD1_RTD3','13576','UG-01 Temp. Fase C','16-bit Signed','INT'],
    # 'ug01_temp_nucleo_estator':['UG01_750_862','UG01_Leitura.RIO600_MOD1_RTD4','13577','UG-01 Temp. Nucleo do estator.','16-bit Signed','INT'],
    # 'ug01_temp_guia_casquilo':['UG01_750_862','UG01_Leitura.RIO600_MOD2_RTD1','13578','UG-01 Temp. Mancal Guia casquilo radial','16-bit Signed','INT'],
    # 'ug01_temp_guia_comb':['UG01_750_862','UG01_Leitura.RIO600_MOD2_RTD2','13579','UG-01 Temp. Mancal Comb. Casq. Radial','16-bit Signed','INT'],
    # 'ug01_temp_comb_escora':['UG01_750_862','UG01_Leitura.RIO600_MOD2_RTD3','13580','UG-01 Temp. Mancal Escora','16-bit Signed','INT'],
    # 'ug01_temp_oleo_UHRV':['UG01_750_862','UG01_Leitura.RIO600_MOD2_RTD4','13581','UG-01 Temp. Óleo UHRV','16-bit Signed','INT',],
    # 'ug01_temp_oleo_UHLM':['UG01_750_862','UG01_Leitura.RIO600_MOD3_RTD1','13582','UG-01 Temp. Óleo UHRV','16-bit Signed','INT',],
    # 'ug01_status':['UG01_750_862','UG01_Status.RegV_TurbinaParada','16491','UG-01 Turbina Parada','bool','BOOLEAN',],
    # 'ug01_vibracao_guia_x':['UG01_750_862','UG01_Leitura.VibracaoX_MancGuia','13617','UG-01 Mancal Guia X','16-bit Signed','INT'],
    # 'ug01_vibracao_guia_y':['UG01_750_862','UG01_Leitura.VibracaoY_MancGuia','13618','UG-01 Mancal Guia Y','16-bit Signed','INT'],
    # 'ug01_vibracao_comb_x':['UG01_750_862','UG01_Leitura.VibracaoX_MancComb','13619','UG-01 Mancal Combinado X','16-bit Signed','INT'],
    # 'ug01_vibracao_comb_y':['UG01_750_862','UG01_Leitura.VibracaoY_MancComb','13620','UG-01 Mancal Combinado Y','16-bit Signed','INT'],
    # 'ug01_vibracao_comb_z':['UG01_750_862','UG01_Leitura.VibracaoZ_MancComb','13621','UG-01 Mancal Combinado Z','16-bit Signed','INT'],
}
control = {
'maria_da_luz local': {
    'status': {
        'address': 'LW-400',
        '0': 'parado',
        '1': 'desconectado',
        '2': 'conectado',
    },
    'Error': {
        'address': 'LW-401',
        '0': 'sem erro',
        '1': 'erro'
    },
    'Control': {
        'address': 'LW-410',
        '0': 'None',
        '1': 'Start',
        '2': 'Stop',
        '3': 'update',
    },
    'Reserved': {
        'address': 'LW-411',
    },
    'Port': {
        'address': 'LW-415',
    },
    'Username': {
        'address': 'LW-416',
    },
    'Password': {
        'address': 'LW-432',
    },
    'Database Name': {
        'address': 'LW-448',
    },
    'Domain name': {
        'address': 'LW-464',
    },
    'Consulta sql local': {
        'Command ID': 'LW-300',
        'Row select': 'LW-301',
        'Row status': 'LW-302',
        'Error code': 'LW-303',
        'Error message': 'LW-304',
    },
},
}
macro = '''
sub int persistir()
//---------------------------------------------------
// Descrição: Função auxiliar .
// pagina: 49: _Eng_UG01_SetPoints
// Junior 06/06/2022
//--------------------------------------------------
    // Verifica o status da conexão com o banco de dados
	int status, control, status_control, error_code, erro
	GetData(status,"SuperSEP",LW,400,1)
    
	if status == 2 then
	    control = 1
		SetData(control,"SuperSEP",LW,300,1)
		GetData(error_code,"SuperSEP",LW,303,1)
        if error_code == 0 then
            TRACE("SALVO com sucesso")
    		return error_code
        else
            TRACE("ERRO para salvar os dados na tabela: %d", error_code)
            return error_code
        end if
	else
		erro = 2
        SetData(erro, "SuperSEP",LW,410,1)
        TRACE("Erro de conexão")
		return erro
	end if
end sub
macro_command main()
//---------------------------------------------------
// Descrição: Executa o comando de .
// pagina: 49: _Eng_UG01_SetPoints
// Junior 06/06/2022
//--------------------------------------------------
// Declaração das variáveis
int id, a, count
// 1- Iniciar o banco de dados
count = 0
a = 1
while a > 0 
    count = count + 1
    id = 1
    TRACE("1 - EXECUTANDO BANCO DE DADOS ONLINE, count %d", count)
    SetData(id,"SuperSEP",LW,410,1)
    DELAY(8000)
    a = persistir()
    DELAY(1000)
    TRACE("A: %d", a)
wend
id = 2
SetData(id,"SuperSEP",LW,410,1)
TRACE("Finalizando- PERSISTIDO DB ONLINE ")

end macro_command
'''
ugs = 1
table_usina = 'cgh_maria_luz'
conexoes = {
    'local': {
        'host': 'localhost',
        'user': 'maria_luz',
        'password': '123456',
        'database': 'engesepdb',
        'port': 3306
    },
    'railway': {
        'host': 'containers-us-west-66.railway.app',
        'user': 'root',
        'password': 'AIgi26lIFr70Rz6uGUbQ',
        'database': 'railway',
        'port': 7438
    }
}
tags_list = [tags_UG01]
if ugs > 1:
    tags_UG02 = {}
    for key, value in tags_UG01.items():
        key = key.replace('ug01','ug02')
        lista = []
        for data in value:
            data = data.replace('UG01','UG02')
            data = data.replace('UG-01','UG-02')
            lista.append(data)
        tags_UG02[key] = lista
    tags_list.append(tags_UG02)


''' COMANDOS EXECUTADOS PARA CRIAÇÃO DO BANCO DE DADOS '''

''' 1 passo: Criar banco de dadoes '''

command = comandos_sql[1]["command"].replace('nome',table_usina)

print(f'\n{command}\n')

''' 2 passo: Criar tabela com as tags escolhidas.'''


command = comandos_sql[2]["command"].replace('nome_tabela',table_usina)


colunas = '(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,\n'
cont = 0
for tags in tags_list:
    for key, value in tags.items():
        colunas += f'{key} {value[5]} DEFAULT NULL, \n '
        cont += 1
        print(cont, '-', key, '-', value[4])

colunas += 'data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)'
command = command.replace('(nome_coluna tipo configuracao)',colunas)
print(f'\n{command}\n')

''' 3 passo: Criar o insert com as tags escolhidas.'''
print('\n')
colunas = ''
values = ''
command = comandos_sql[9]["command"].replace('nome_tabela',table_usina)
cont = 0
for tags in tags_list:
    for key, value in tags.items():
        cont += 1
        colunas += f'{key},\n '
        values += "'${"+ str(cont) + "}',\n "
        # print(key)
colunas = colunas[:-3]
values = values[:-3]
command = command.replace('coluna',colunas)
command = command.replace('value',values)
print(f'\n{command}\n')

