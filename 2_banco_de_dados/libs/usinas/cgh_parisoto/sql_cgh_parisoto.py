
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# importando as bibliotecas
import pandas as pd
from libs.utils.sql import comandos_sql, print_tags, tags, buscar_tags, data_types, search_type, rename_columns
from tabulate import tabulate
import os

# configurações gerais
#-------------------------------------------------------------------------------
ugs = int(1)
table_usina = 'cgh_parisoto'
user = table_usina.replace('cgh_', '')
LW_DB = 400
LW_QUERY = 300
LW_CONSULT=810
reduz = False
#-------------------------------------------------------------------------------
conexoes = {
    'local': {
        'host': 'ip: 192.168.10.30',
        'user': f'{user}',
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
base_addr = 'LW-'
control = {
    'cgh_fae local': {
        'status': {'address': base_addr + str(LW_DB), '0': 'parado', '1': 'desconectado', '2': 'conectado'},
        'Error': {'address': base_addr + str(LW_DB + 1), '0': 'sem erro', '1': 'erro'},
        'Control': {'address': base_addr + str(LW_DB + 10), '0': 'None', '1': 'Start', '2': 'Stop', '3': 'update'},
        'Reserved': {'address': base_addr + str(LW_DB + 11)},
        'Port': {'address': base_addr + str(LW_DB + 15)},
        'Username': {'address': base_addr + str(LW_DB + 16)},
        'Password': {'address': base_addr + str(LW_DB + 32)},
        'Database Name': {'address': base_addr + str(LW_DB + 48)},
        'Domain name': {'address': base_addr + str(LW_DB + 64)},
        'Consulta sql local': {
            'Command ID': base_addr + str(LW_QUERY),
            'Row select': base_addr + str(LW_QUERY + 1),
            'Row status': base_addr + str(LW_QUERY + 2),
            'Error code': base_addr + str(LW_QUERY + 3),
            'Error message': base_addr + str(LW_QUERY + 4)
        },
    },
}
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
        '1': 'F50_U_FaseAB',
        '2': 13349,
        '3': 'UG-01 Tensão Fase A',
        '4': 'Undesigned',
        '5': 'INT',
    },
    'ug01_tensao_fase_B': {
        '0': 'UG01_750_862',
        '1': 'F50_U_FaseBC',
        '2': 13350,
        '3': 'UG-01 Tensão Fase B',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_tensao_fase_C': {
        '0': 'UG01_750_862',
        '1': 'F50_U_FaseCA',
        '2': 13351,
        '3': 'UG-01 Tensão Fase C',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_corrente_fase_A': {
        '0': 'UG01_750_862',
        '1': 'F50_I_INST_A',
        '2': 13355,
        '3': 'UG-01 Corrente Fase A',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_corrente_fase_B': {
        '0': 'UG01_750_862',
        '1': 'F50_I_INST_B',
        '2': 13356,
        '3': 'UG-01 Corrente Fase B',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_corrente_fase_C': {
        '0': 'UG01_750_862',
        '1': 'F50_I_INST_C',
        '2': 13357,
        '3': 'UG-01 Corrente Fase C',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_tensao_excitacao': {
        '0': 'UG01_750_862',
        '1': 'Gerador_ExcitacaoTensao',
        '2': 13380,
        '3': 'UG-01 Tensão Excitação',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_corrente_excitacao': {
        '0': 'UG01_750_862',
        '1': 'Gerador_ExcitacaoCorrente',
        '2': 13381,
        '3': 'UG-01 Corren. Excitação',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_frequencia': {
        '0': 'UG01_750_862',
        '1': 'F50_FHz_INST',
        '2': 13363,
        '3': 'UG-01 Frequência',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_potencia_ativa': {
        '0': 'UG01_750_862',
        '1': 'F50_P_INST',
        '2': 13359,
        '3': 'UG-01 Potência Ativa',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_potencia_reativa': {
        '0': 'UG01_750_862',
        '1': 'F50_Q_INST',
        '2': 13360,
        '3': 'UG-01 Potência Reativa',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_potencia_aparente': {
        '0': 'UG01_750_862',
        '1': 'F50_S_INST',
        '2': 13361,
        '3': 'UG-01 Potência Aparente',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_fp': {
        '0': 'UG01_750_862',
        '1': 'F50_PF_INST',
        '2': 13362,
        '3': 'UG-01 Fator de Potência',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_horimetro_e': {
        '0': 'UG01_750_862',
        '1': 'Horimetro_Eletrico',
        '2': 14105,
        '3': 'UG-01 Horimetro',
        '4': '32-bit Float',
        '5': 'FLOAT',
    },
    'ug01_horimetro_m': {
        '0': 'UG01_750_862',
        '1': 'Horimetro_Mecanico',
        '2': 14099,
        '3': 'UG-01 Horimetro',
        '4': '32-bit Float',
        '5': 'FLOAT',
    },
    'ug01_horimetro_UHRV': {
        '0': 'UG01_750_862',
        '1': 'Horimetro_UHRV',
        '2': 14111,
        '3': 'UG-01 Horimetro',
        '4': '32-bit Float',
        '5': 'FLOAT',
    },
    'ug01_distribuidor': {
        '0': 'UG01_750_862',
        '1': 'Turbina_PosicaoDistribuidor',
        '2': 13303,
        '3': 'UG-01 Distribuidor',
        '4': '32-bit Float',
        '5': 'INT',
    },
    'ug01_velocidade': {
        '0': 'UG01_750_862',
        '1': 'Turbina_Velocidade',
        '2': 13307,
        '3': 'UG-01 Velocidade RPM',
        '4': '16-bit Signed',
        '5': 'INT',
    },
    'ug01_acumulador_energia': {
        '0': 'UG01_750_862',
        '1': 'Gerador_EnergiaFornecidakWh',
        '2': 13385,
        '3': 'UG-01 Acum. Energia',
        '4': '32-bit Float',
        '5': 'FLOAT',
    },
    'ug01_temp_fase_A': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD1_RTD1',
        '2': 13409,
        '3': 'UG-01 Temp. Fase A',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_fase_B': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD1_RTD2',
        '2': 13411,
        '3': 'UG-01 Temp. Fase B',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_fase_C': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD1_RTD3',
        '2': 13413,
        '3': 'UG-01 Temp. Fase C',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_nucleo_estator': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD1_RTD4',
        '2': 13415,
        '3': 'UG-01 Temp. Nucleo do estator.',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_casq_inf': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD2_RTD1',
        '2': 13417,
        '3': 'UG-01 Temp. Mancal Guia casquilo radial',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_man_comb': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD2_RTD2',
        '2': 13419,
        '3': 'UG-01 Temp. Mancal Comb. Casq. Radial',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_comb_escora': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD2_RTD3',
        '2': 13421,
        '3': 'UG-01 Temp. Mancal Escora',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_oleo_UHRV': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD2_RTD4',
        '2': 13423,
        '3': 'UG-01 Temp. Óleo UHRV',
        '4': '16-bit Signed',
        '5': 'FLOAT',
    },
    'ug01_temp_oleo_UHLM': {
        '0': 'UG01_750_862',
        '1': 'RIO600_MOD3_RTD1',
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

tags_UG01 = {
    'ug01_status': ['UG01_750_862', 'RegV_TurbinaParada', 20548, 'UG-01 Turbina Parada', 'Signed', 'BOOLEAN'] ,
    'ug01_acumulador_energia': ['UG01_750_862', 'Gerador_EnergiaFornecidakWh', 13385, 'UG-01 Acum. Energia', 'Float', 'FLOAT'] ,
    'ug01_nivel_agua': ['USINA_750_862', 'NivelCamaraCarga', 13569, 'Nível Água', 'Signed', 'FLOAT'] ,
    'ug01_tensao_fase_A': ['UG01_750_862', 'U_FaseAB', 13349, 'UG-01 Tensão Fase A', 'Signed', 'INT'] ,
    'ug01_tensao_fase_B': ['UG01_750_862', 'U_FaseBC', 13350, 'UG-01 Tensão Fase B', 'Signed', 'INT'] ,
    'ug01_tensao_fase_C': ['UG01_750_862', 'U_FaseCA', 13351, 'UG-01 Tensão Fase C', 'Signed', 'INT'] ,
    'ug01_corrente_fase_A': ['UG01_750_862', 'I_INST_A', 13355, 'UG-01 Corrente Fase A', 'Signed', 'INT'] ,
    'ug01_corrente_fase_B': ['UG01_750_862', 'I_INST_B', 13356, 'UG-01 Corrente Fase B', 'Signed', 'INT'] ,
    'ug01_corrente_fase_C': ['UG01_750_862', 'I_INST_C', 13357, 'UG-01 Corrente Fase C', 'Signed', 'INT'] ,
    'ug01_tensao_excitacao': ['UG01_750_862', 'Gerador_ExcitacaoTensao', 13380, 'UG-01 Tensão Excitação', 'Signed', 'INT'] ,
    'ug01_corrente_excitacao': ['UG01_750_862', 'Gerador_ExcitacaoCorrente', 13381, 'UG-01 Corren. Excitação', 'Float', 'INT'] ,
    'ug01_frequencia': ['UG01_750_862', 'FHz_INST', 13363, 'UG-01 Frequência', 'Signed', 'INT'] ,
    'ug01_potencia_ativa': ['UG01_750_862', 'P_INST', 13359, 'UG-01 Potência Ativa', 'Unsigned', 'INT'] ,
    'ug01_potencia_reativa': ['UG01_750_862', 'Q_INST', 13360, 'UG-01 Potência Reativa', 'Signed', 'INT'] ,
    'ug01_potencia_aparente': ['UG01_750_862', 'S_INST', 13361, 'UG-01 Potência Aparente', 'Signed', 'INT'] ,
    'ug01_fp': ['UG01_750_862', 'PF_INST', 13362, 'UG-01 Fator de Potência', 'Unsigned', 'INT'] ,
    'ug01_horimetro_e': ['UG01_750_862', 'Horimetro_Eletrico', 14105, 'UG-01 Horimetro', 'Float', 'FLOAT'] ,
    'ug01_horimetro_m': ['UG01_750_862', 'Horimetro_Mecanico', 14099, 'UG-01 Horimetro', 'Float', 'FLOAT'] ,
    'ug01_horimetro_UHRV': ['UG01_750_862', 'Horimetro_UHRV', 14111, 'UG-01 Horimetro', 'Float', 'FLOAT'] ,
    'ug01_distribuidor': ['UG01_750_862', 'Turbina_PosicaoDistribuidor', 13303, 'UG-01 Distribuidor', 'Float', 'INT'] ,
    'ug01_velocidade': ['UG01_750_862', 'Turbina_Velocidade', 13307, 'UG-01 Velocidade RPM', 'Float', 'INT'] ,
    'ug01_temp_fase_A': ['UG01_750_862', 'MED_750450_AR1_RTD1', 13409, 'UG-01 Temp. Fase A', 'Float', 'FLOAT'] ,
    'ug01_temp_fase_B': ['UG01_750_862', 'MED_750450_AR1_RTD2', 13411, 'UG-01 Temp. Fase B', 'Float', 'FLOAT'] ,
    'ug01_temp_fase_C': ['UG01_750_862', 'MED_750450_AR1_RTD3', 13413, 'UG-01 Temp. Fase C', 'Float', 'FLOAT'] ,
    'ug01_temp_nucleo_estator': ['UG01_750_862', 'MED_750450_AR1_RTD4', 13415, 'UG-01 Temp. Nucleo do estator.', 'Float', 'FLOAT'] ,
    'ug01_temp_casq_inf': ['UG01_750_862', 'MED_750450_AR2_RTD1', 13417, 'UG-01 Temp. Mancal Guia casquilo radial', 'Float', 'FLOAT'] ,
    'ug01_temp_cont_escora': ['UG01_750_862', 'MED_750450_AR2_RTD2', 13419, 'UG-01 Temp. Mancal Comb. Casq. Radial', 'Float', 'FLOAT'] ,
    'ug01_temp_escora': ['UG01_750_862', 'MED_750450_AR2_RTD3', 13421, 'UG-01 Temp. Mancal Escora', 'Float', 'FLOAT'] ,
    'ug01_temp_comb_casq': ['UG01_750_862', 'MED_750450_AR2_RTD4', 13421, 'UG-01 Temp. Mancal Escora', 'Float', 'FLOAT'] ,
    'ug01_temp_oleo_UHRV': ['UG01_750_862', 'MED_750450_AR3_RTD1', 13423, 'UG-01 Temp. Óleo UHRV', 'Float', 'FLOAT'] ,
    'ug01_temp_oleo_UHLM': ['UG01_750_862', 'MED_750450_AR3_RTD2', 13425, 'UG-01 Temp. Óleo UHRV', 'Float', 'FLOAT'] ,
    'ug01_temp_cs_u1': ['UG01_750_862', 'MED_750450_AR3_RTD3', 13427, 'UG-01 Turbina Parada', 'Float', 'FLOAT'] ,
    'ug01_temp_engex': ['UG01_750_862', 'MED_750450_AR3_RTD4', 13429, 'UG-01 Turbina Parada', 'Float', 'FLOAT'] ,

}

macro_offline = f'''
sub int persistir()
//---------------------------------------------------
// Descrição: Perisistir dados .
// Data 08/08/2023
//--------------------------------------------------
    
    int status, error_code, erro, control
    int LW_control, LW_control_status, LW_query, LW_query_status
    
    LW_control = {str(LW_DB + 10)}
    LW_control_status= {str(LW_DB)}
    LW_query = {str(LW_QUERY)}
    LW_query_status = {str(LW_QUERY + 3)}
    
    GetData(status,"SuperSEP",LW,LW_control_status,1)
    
	if status == 2 then
	    control = 1
		SetData(control,"SuperSEP",LW,LW_query,1)
		DELAY(3000)
		GetData(error_code,"SuperSEP",LW,LW_query_status,1)
        if error_code == 0 then
            TRACE("SALVO com sucesso")
    		return error_code
        else
            TRACE("ERRO para salvar os dados na tabela: %d", error_code)
            return error_code
        end if
	else
		erro = 2
        SetData(erro, "SuperSEP",LW,LW_control,1)
        TRACE("Erro de conexão")
		return erro
	end if
	
end sub
macro_command main()
//---------------------------------------------------
// Descrição: Macro de conexão persistente .
// Junior 08/08/2023
//--------------------------------------------------

    int id, a, count, control
    int LW_control
    count = 0
    a = 1
    LW_control = {str(LW_DB + 10)}
    
    while a > 0 
        count = count + 1
        id = 1
        TRACE("1 - EXECUTANDO BANCO DE DADOS ONLINE, count %d", count)
        SetData(id,"SuperSEP",LW,LW_control,1)
        DELAY(8000)
        a = persistir()
        DELAY(1000)
        TRACE("A: %d", a)
    wend
    id = 2
    SetData(id,"SuperSEP",LW,LW_control,1)
    TRACE("Finalizando- PERSISTIDO DB ONLINE ")

end macro_command
'''
macro_offline_consulta = f'''
sub excecao(int status)
    
    char canal_text[20]

    FILL(canal_text[0],0x20,20)
    StringSet(canal_text[0],"SuperSEP",LW,6500,20)
    
    if status == 0 then
        TRACE("Parado DB online")
        StringCopy("Parado DB online",canal_text[0])
        StringSet(canal_text[0],"SuperSEP", LW, 6500, 20)

    else if status == 1 then
        TRACE("Desconectado DB online")
        StringCopy("Desconectado DB online",canal_text[0])
        StringSet(canal_text[0],"SuperSEP",LW,6500, 20)
    else if status == 2 then
        TRACE("Selecione as datas")
        StringCopy("Selecione as datas",canal_text[0])
        StringSet(canal_text[0],"SuperSEP",LW,6500, 20)
    else if status == 3 then
        TRACE("Erro na consulta")
        StringCopy("Erro na consulta",canal_text[0])
        StringSet(canal_text[0],"SuperSEP",LW,6500, 20)
    else
        TRACE("Sucesso DB online")
        StringCopy("Sucesso DB online",canal_text[0])
        StringSet(canal_text[0],"SuperSEP",LW,6500, 20)
    end if


end Sub

sub int consulta()

    // declaracao da variaveis
    int tipo, gerador, id, erro
    int LW_control, LW_control_status, LW_consulta, LW_consulta_status

    // ¨¨¨¨ Iniciar o banco de dados¨¨¨¨
    LW_control = {str(LW_DB + 10)}
    LW_control_status= {str(LW_DB)}
    LW_consulta = {str(LW_CONSULT)}
    LW_consulta_status = {str(LW_CONSULT + 3)}
    
    // verifica o periodo de dados
    GetData(tipo,"SuperSEP",LW,1100,1)
    GetData(gerador,"SuperSEP",LW,1400,1)
    //0 - anual, 1 - mensal, 2 - todos UG01, 3 - todos UG02
    //0 - UG01, 1 - UG02
    // 1 - anual UG01, 2 - anual UG02, 3 - mensal UG01, 4 - mensal UG02, 5 - todos UG01, 6 - todos UG02
    TRACE("TIPO: %d, GERADOR: %d", tipo, gerador)
    TRACE("TIPO: %d, GERADOR: %d", tipo, gerador)
    if tipo == 0 and gerador == 0 then
        TRACE("UG-01 ANUAL")
        id = 1
        SetData(id,"SuperSEP",LW,LW_consulta,1)
        GetData(erro,"SuperSEP",LW,LW_consulta_status,1)
        if erro > 0 then
            TRACE("UG-01 ANUAL, Erro: %d ", erro)
            id = 3
            return id
        else
            id = 100
            return id
        end if
    
    else if tipo == 1 and gerador == 0 then
        TRACE("UG-01 MENSAL")
        id = 2
        SetData(id,"SuperSEP",LW,LW_consulta ,1)
        GetData(erro,"SuperSEP",LW,LW_consulta_status,1)
        if erro > 0 then
            TRACE("UG-01 MENSAL, Erro: %d ", erro)
        	id = 3
            return id
        else
        	id = 100
            return id
        end if
        
    else if tipo == 2 and gerador == 0 then
        TRACE("UG-01 TODOS")
        id = 3
        SetData(id,"SuperSEP",LW,LW_consulta ,1)
        GetData(erro,"SuperSEP",LW,LW_consulta_status,1)
        if erro > 0 then
            TRACE("UG01 TODOS, Erro: %d ", erro)
            id = 3
            return id
        else
            id = 100
            return id
        end if
    else 
        TRACE("Não previsto")
        id = 100
        return id
    end if

end Sub

Sub int StatusConexaoDB()

// declaracao de variaveis

int status_db, control_db
int LW_control, LW_control_status, LW_consulta, LW_consulta_status

// ¨¨¨¨ Iniciar o banco de dados¨¨¨¨
LW_control = {str(LW_DB + 10)}
LW_control_status= {str(LW_DB)}
LW_consulta = {str(LW_CONSULT)}
LW_consulta_status = {str(LW_CONSULT + 3)}
// busca o status da conexão do banco de dados

GetData(status_db,"SuperSEP",LW,LW_control_status,1)

// verifica a conexão do banco de dados

if status_db == 0 or status_db == 1 then
    // conexão parada -> iniciar conexão
    TRACE("FALHA NA CONEXAO: %d", status_db)
    control_db = 1
    SetData(control_db,"SuperSEP",LW,LW_control,1)
    DELAY(3000)
    GetData(status_db,"SuperSEP",LW,LW_control_status,1)
    TRACE("RESULTADO DO AJUSTE DA CONEXAO: %d", status_db)
    return status_db
    
else if status_db == 2 then
    // conectado -> mantém a conexão
    TRACE("CONEXAO REALIZADA COM SUCESSO")
    return status_db
else 
    TRACE("FALHA NA CONEXAO COM RESULTADO INESPERADO: %d ", status_db)
    control_db = 3
    SetData(control_db,"SuperSEP",LW,LW_control,1)
    DELAY(3000)
    GetData(status_db,"SuperSEP",LW,LW_control_status,1)
    TRACE("RESULTADO DO AJUSTE DA CONEXAO: %d", status_db)
    return status_db
end if

end Sub

macro_command main()
//------------------------------------------------------------------------------------------
// Descricao: Macro que filtra as entradas e envia comandos para a consulta no banco de dados
// Data da última atualização: 19/05/2023
//-----------------------------------------------------------------------------------------------

// ¨¨¨¨ Declaração de variáveis¨¨¨¨

char canal_error[20], data_text_a[20], data_text_b[20]

int status_conexao, a, control, status_control, erro, data_length_a, data_length_b
int LW_control, LW_control_status, LW_consulta, LW_consulta_status

// ¨¨¨¨ Iniciar o banco de dados¨¨¨¨
LW_control = {str(LW_DB + 10)}
LW_control_status= {str(LW_DB)}
LW_consulta = {str(LW_CONSULT)}
LW_consulta_status = {str(LW_CONSULT + 3)}

status_conexao = StatusConexaoDB()

if status_conexao == 2 then 
    // 3 - Validação das datas
    FILL(data_text_a[0],0x20,20)
    FILL(data_text_b[0],0x20,20)
    StringGet(data_text_a[0],"SuperSEP",LW,1200, 20)
    StringGet(data_text_b[0],"SuperSEP",LW,1300, 20)
    data_length_a = StringLength(data_text_a[0])
    data_length_b = StringLength(data_text_b[0])
    
    if data_length_a < 10 or data_length_b < 10 then
        erro = 2
        excecao(erro)
    else
        erro = consulta()
        excecao(erro)
    end if
else
    excecao(status_conexao)
end if
TRACE("   ")
end macro_command
'''

querys_consulta = {
    'anual_ug01': f'''
SELECT 
    YEAR(data_hora) AS `Ano`,
    MONTH(data_hora) AS `Mês`,
    ROUND(MAX(ug01_acumulador_energia) - MIN(ug01_acumulador_energia), 2) AS `UG01 Acumulado mensal (MW)`
FROM 
    {table_usina}
WHERE
    ug01_acumulador_energia != 0
GROUP BY 
    YEAR(data_hora),
    MONTH(data_hora);
''',
    'mensal_ug01': f'''
SELECT 
    DATE(data_hora) AS `Data`,
    ROUND(MAX(ug01_acumulador_energia) - MIN(ug01_acumulador_energia), 2) AS `UG01 Energia Diária (MW)`
FROM 
    {table_usina} 
WHERE 
    DATE(data_hora) BETWEEN '${{1}}' AND '${{2}}'
    AND (ug01_acumulador_energia > 0)
GROUP BY 
    DATE(data_hora);
''',
    'todos_ug01': f'''
SELECT data_hora AS `data`,
ROUND(ug01_nivel_agua/100, 2) AS `nivel agua`,
ug01_tensao_fase_A AS `tensao fase A`,
ug01_tensao_fase_B AS `tensao fase B`,
ug01_tensao_fase_C AS `tensao fase C`,
ug01_corrente_fase_A AS `corrente fase A`,
ug01_corrente_fase_B AS `corrente fase B`,
ug01_corrente_fase_C AS `corrente fase C`,
ug01_tensao_excitacao AS `tensao excitacao`,
ug01_corrente_excitacao AS `corrente excitacao`,
ug01_frequencia AS `frequencia`,
ug01_potencia_ativa AS `potencia ativa`,
ug01_potencia_reativa AS `potencia reativa`,
ug01_potencia_aparente AS `potencia aparente`,
ROUND(ug01_fp/1000,2) AS `fp`,
ug01_horimetro_e AS `horimetro eletrico`,
ROUND(ug01_distribuidor/10,2) AS `distribuidor`,
ug01_velocidade AS `velocidade`,
ROUND(ug01_acumulador_energia,2) AS `acumulador energia`,
ug01_temp_fase_A AS `temp fase A`,
ug01_temp_fase_B AS `temp fase B`,
ug01_temp_fase_C AS `temp fase C` FROM {table_usina} WHERE data_hora >= '${{1}}' AND data_hora <= '${{2}}' ORDER BY data_hora DESC;
''',

}
# Criar o comando de criação do banco de dados Off-line
tags_list = [tags_UG01]
if ugs > 1:
    tags_UG02 = {}
    for key, value in tags_UG01.items():
        if not 'USINA' in value[0]:
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

command = comandos_sql[1]["command"].replace('nome','engesepdb')
print('_______________________________________________________________')
print(f"----> 1) Comando sql para criar database offline:")
print('_______________________________________________________________')
print(command)
print('_______________________________________________________________')
print(' ')
print('_______________________________________________________________')
print(f"----> 2) Criar usuário com privilegios no banco de dados Offline:")
print('_______________________________________________________________')
print_tags(conexoes["local"])
print('_______________________________________________________________')
print(' ')
print('_______________________________________________________________')
print(f"----> 3) Criar tabelas online e offline:")
print('_______________________________________________________________')
command = comandos_sql[2]["command"].replace('nome_tabela',table_usina)
colunas = '(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,\n'
cont = 0
for tags in tags_list:
    for key, value in tags.items():
        cont += 1
        tipo = search_type(value[4])
        if reduz:
            name = rename_columns(key)
            colunas += f'{str(cont)}{name} {tipo} DEFAULT NULL,\n '
        else:
            colunas += f'{key} {tipo} DEFAULT NULL,\n '

colunas += 'data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)'
command = command.replace('(nome_coluna tipo configuracao)',colunas)
print('Tamanho caracters: ', len(command))
print(command)
print('_______________________________________________________________')
print('_______________________________________________________________')
print(f"----> 4) Criar tabelas online e offline para o supervisorio:")
print('_______________________________________________________________')
colunas = ''
values = ''
command = comandos_sql[9]["command"].replace('nome_tabela',table_usina)
cont = 0
referencia = ''
for tags in tags_list:
    for key, value in tags.items():
        cont += 1
        if reduz:
            name = rename_columns(key)
            colunas += f'{str(cont)}{name},' + '\n'
        else:
            colunas += key + ',' + '\n'
        values += "'${"+ str(cont) + "}'," + '\n'
        referencia +=  str(cont) + ' - ' + key + ' - ' + value[4] + '\n'

colunas = colunas[:-2]
values = values[:-2]
command = command.replace('coluna',colunas)
command = command.replace('value',values)
print('Tamanho caracters: ', len(command))
print(command)
print('_______________________________________________________________')
print('_______________________________________________________________')
print(f"----> 5) Criar tabelas online e offline:")
print('_______________________________________________________________')
print_tags(control)
print(' ')
print(referencia)
cont = 0
for tags in tags_list:
    for key, value in tags.items():
        cont += 1
        print(cont,'-', key,'-',value[1],'-',value[4],'-',value[0])
        resp = buscar_tags(value[1], 'tags_parisoto.csv')
        print(tabulate(resp, headers='keys', tablefmt='psql'))
        print('_______________________________________________________________')
print('_______________________________________________________________')
print('_______________________________________________________________')
print(f"----> 6) MACRO:")
print('_______________________________________________________________')
print(macro_offline)
print('_______________________________________________________________')
print('_______________________________________________________________')
print(f"----> 7) MACRO: CONSULTA OFFLINE")
print('_______________________________________________________________')
print(macro_offline_consulta)
print('_______________________________________________________________')
print('_______________________________________________________________')
print(f"----> 8) QUERYS: CONSULTA OFFLINE")
print('_______________________________________________________________')
# if reduz:
'''substiruir os nomes na consulta query'''
def substuir_nome_query(texto):
    for key, value in lista_reducao.items():
        texto = texto.replace(key, value)
    return texto
for key, value in querys_consulta.items():
    new_query = value
    # new_query = new_query.replace("',",'`,\n')
    # new_query = new_query.replace("'","`")
    print(new_query)
    print('_______________________________________________________________')
    querys_consulta[key] = new_query
    # print(querys_consulta)

'''
Qual fone escolher:
    1) Edifier W820NB
    2) Galaxy Buds 2 Pro
    3) AirPods Pro 2ª geração
    4) Beats Studio Buds
    5) JBL Live 660NC
    6) Sony WH-1000XM4
    7) JBL Live Pro 2
    8) JBL Tune 760NC
    9) Soundcore Life Q30
    10) Sony WH-1000XM4
'''