
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# importando as bibliotecas
import pandas as pd
from libs.utils.sql import comandos_sql, print_tags, tags, buscar_tags, data_types, search_type, rename_columns
from tabulate import tabulate
import os

# configurações gerais
#-------------------------------------------------------------------------------
ugs = int(2)
table_usina = 'cgh_sebastiao_paz_almeida'
user = table_usina.replace('cgh_', '')
LW_DB = 400
LW_QUERY = 2000
LW_CONSULT = 810
reduz = False
#-------------------------------------------------------------------------------
# Função que importar as tags
def importar_csv(path: str)-> pd.DataFrame:
    '''Importa o arquivo csv'''
    name_columns = ['tag_name', 'device_name', 'type', 'address', 'comment', 'format']  # define os nomes das colunas

    df = pd.read_csv(path, header=None, names= name_columns, sep=',') # lê o arquivo csv

    return df

#-------------------------------------------------------------------------------
conexoes = {
    'local': {
        'host': '192.168.10.30',
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

# [14:42:52] [ID 018, Line 6] Ug01_status, 20548: 0
# [14:42:52] [ID 018, Line 10] Ug01_acumulador_energia, 13491: 12.731415
# [14:42:52] [ID 018, Line 14] Ug01_nivel_agua, 13569: 473
# [14:42:52] [ID 018, Line 18] Ug01_tfase_a, 13349: 45220531
# [14:42:52] [ID 018, Line 22] Ug01_tfase_b, 13350: 45286066
# [14:42:52] [ID 018, Line 26] Ug01_tfase_c, 13351: 691
# [14:42:52] [ID 018, Line 30] Ug01_ifase_a, 13355: 0
# [14:42:52] [ID 018, Line 34] Ug01_ifase_b, 13356: 0
# [14:42:53] [ID 018, Line 38] Ug01_ifase_c, 13357: 0
# [14:42:53] [ID 018, Line 42] Ug01_texcitacao, 13383: 327706
# [14:42:53] [ID 018, Line 46] Ug01_iexcitacao, 13384: 5
# [14:42:53] [ID 018, Line 50] Ug01_freq, 13366: 0
# [14:42:53] [ID 018, Line 54] Ug01_pativa, 13359: 0
# [14:42:53] [ID 018, Line 58] Ug01_preativa, 13361: 0
# [14:42:53] [ID 018, Line 62] Ug01_paparente, 13363: 0
# [14:42:53] [ID 018, Line 66] Ug01_fp, 13365: 0
# [14:42:53] [ID 018, Line 70] Ug01_dist, 13303: 12.902832
# [14:42:53] [ID 018, Line 74] Ug01_veloc, 13307: 720.000000
# [14:42:53] [ID 018, Line 78] Ug01_horimetro_eletrico, 14105: 12.900013
# [14:42:53] [ID 018, Line 82] Ug01_pjusante, 13301: 17891602
# [14:42:53] [ID 018, Line 86] Ug01_pmontante, 13302: 1912602897
# [14:42:53] [ID 018, Line 90] Ug01_poleo_uhlm, 13289: 0
# [14:42:53] [ID 018, Line 94] Ug01_poleo_uhrv, 13295: 144
# [14:42:53] [ID 018, Line 98] Ug01_teenrol_a, 13409: 50.000000
# [14:42:53] [ID 018, Line 102] Ug01_teenrol_b, 13411: 51.000000
# [14:42:53] [ID 018, Line 106] Ug01_teenrol_c, 13413: 50.000000
# [14:42:54] [ID 018, Line 110] Ug01_temancal_nucleo, 13415: 52.000000
# [14:42:54] [ID 018, Line 114] Ug01_temancal_guia, 13417: 24.000000
# [14:42:54] [ID 018, Line 118] Ug01_temancal_escora, 13419: 25.000000
# [14:42:54] [ID 018, Line 122] Ug01_tecsu2, 13431: 0.000000
# [14:42:54] [ID 018, Line 126] Ug01_vmancal_g_x, 13329: 0
# [14:42:54] [ID 018, Line 130] Ug01_vmancal_g_y, 13330: 0
# [14:42:54] [ID 018, Line 134] Ug01_vmancal_c_x, 13331: 0
# [14:42:54] [ID 018, Line 138] Ug01_vmancal_c_y, 13332: 0
# [14:42:54] [ID 018, Line 142] Ug01_vmancal_c_z, 13333: 0
# [14:42:54] [ID 018, Line 146] Ug01_ilinha_a, 13600: 0
# [14:42:54] [ID 018, Line 150] Ug01_ilinha_b, 13601: 0
# [14:42:54] [ID 018, Line 154] Ug01_ilinha_c, 13602: 0
# [14:42:54] [ID 018, Line 158] Ug01_tbarra, 13603: 0
# [14:42:54] [ID 018, Line 162] Ug01_pconduto, 13617: 0
# [14:42:55] [ID 018, Line 166] Ug01_ac_energia_u, 13614: 0

tags_UG01 = {
    'ug01_status':['UG01_750_852','UG01_Status.RegV_TurbinaParada','20548','TurbinaParada', '16-bit Signed','INT'],
    'ug01_acumulador_energia':['UG01_750_852','UG01_Leituras.Gerador_EnergiaFornecidaMWh','13491','EnergiaFornecidaMWh', '32-bit Float','FLOAT'],
    'ug01_nivel_agua':['USINA_750_852','NivelCamaraCarga','13569','NivelCamaraCarga', '16-bit Signed','INT'],
    'ug01_Tfase_A':['UG01_750_852','UG01_Leituras.F50_U_FaseAB','13349','FaseAB', '16-bit Signed','INT'],
    'ug01_Tfase_B':['UG01_750_852','UG01_Leituras.F50_U_FaseBC','13350','FaseBC', '16-bit Signed','INT'],
    'ug01_Tfase_C':['UG01_750_852','UG01_Leituras.F50_U_FaseCA','13351','FaseCA', '16-bit Signed','INT'],
    'ug01_Ifase_A':['UG01_750_852','UG01_Leituras.F50_I_FaseA','13355','I_FaseA', '16-bit Signed','INT'],
    'ug01_Ifase_B':['UG01_750_852','UG01_Leituras.F50_I_FaseB','13356','I_FaseB', '16-bit Signed','INT'],
    'ug01_Ifase_C':['UG01_750_852','UG01_Leituras.F50_I_FaseC','13357','I_FaseC', '16-bit Signed','INT'],
    'ug01_Texcitacao':['UG01_750_852','UG01_Leituras.Gerador_ExcitacaoTensao','13383','ExcitacaoTensao', '16-bit Signed','INT'],
    'ug01_Iexcitacao':['UG01_750_862','UG01_Leituras.Gerador_ExcitacaoCorrente','13384','ExcitacaoCorrente', '16-bit Signed','INT'],
    'ug01_freq':['UG01_750_862','UG01_Leituras.F50_FHz_INST','13366','FHz_INST', '16-bit Signed','INT'],
    'ug01_Pativa':['UG01_750_862','UG01_Leituras.F50_P_INST','13359','P_INST', '32-bit Unsigned','BIGINT'],
    'ug01_Preativa':['UG01_750_862','UG01_Leituras.F50_Q_INST','13361','Q_INST', '32-bit Unsigned','BIGINT'],
    'ug01_Paparente':['UG01_750_862','UG01_Leituras.F50_S_INST','13363','S_INST', '32-bit Unsigned','BIGINT'],
    'ug01_fp':['UG01_750_862','UG01_Leituras.F50_PF_INST','13365','UG01_Leituras.F50_PF_INST', '16-bit Unsigned','BIGINT'],
    'ug01_dist':['UG01_750_862','UG01_Leituras.Turbina_PosicaoDistribuidor','13303','PosicaoDistribuidor', '32-bit Float','FLOAT'],
    'ug01_veloc': ['UG01_750_862','UG01_Leituras.Turbina_Velocidade','13307','Turbina_Velocidade', '32-bit Float','FLOAT'],
    'ug01_horimetro_eletrico':['UG01_750_862','UG01_Setpoint.Horimetro_Eletrico_Total','14105','Horimetro_Eletrico', '32-bit Float','FLOAT'],
    'ug01_Pjusante':['UG01_750_862','UG01_Leituras.Turbina_Pressao_JusanteBorboleta','13301','Turbina_Pressao_JusanteBorboleta', '16-bit Signed','INT'],
    'ug01_Pmontante':['UG01_750_862','UG01_Leituras.Turbina_Pressao_MontanteBorboleta','13302','Turbina_Pressao_MontanteBorboleta', '16-bit Signed','INT'],
    'ug01_Poleo_uhlm':['UG01_750_862','UG01_Leituras.UHLM_PressaoOleo','13289','UHLM_PressaoOleo', '16-bit Signed','INT'], # até aqui
    'ug01_Poleo_uhrv':['UG01_750_862','UG01_Leituras.UHRV_PressaoOleo','13295','UHRV_PressaoOleo', '16-bit Signed','INT'],
    'ug01_TEenrol_A':['UG01_750_862','UG01_Leituras.MED_750450_AR1_RTD1','13409','MED_750450_AR1_RTD1', '32-bit Float','FLOAT'],
    'ug01_TEenrol_B':['UG01_750_862','UG01_Leituras.MED_750450_AR1_RTD2','13411','MED_750450_AR1_RTD2', '32-bit Float','FLOAT'],
    'ug01_TEenrol_C':['UG01_750_862','UG01_Leituras.MED_750450_AR1_RTD3','13413','MED_750450_AR1_RTD3', '32-bit Float','FLOAT'],
    'ug01_TEmancal_nucleo':['UG01_750_862','UG01_Leituras.MED_750450_AR1_RTD4','13415','MED_750450_AR1_RTD4', '32-bit Float','FLOAT'],
    'ug01_TEmancal_guia':['UG01_750_862','UG01_Leituras.MED_750450_AR2_RTD1','13417','MED_750450_AR2_RTD1', '32-bit Float','FLOAT'],
    'ug01_TEmancal_escora':['UG01_750_862','UG01_Leituras.MED_750450_AR2_RTD2','13419','MED_750450_AR2_RTD2', '32-bit Float','FLOAT'],
    'ug01_TEcsu2':['UG01_750_862','UG01_Leituras.MED_750450_AR3_RTD4','13431','MED_750450_AR3_RTD4', '32-bit Float','FLOAT'], # até aqui
    'ug01_Vmancal_g_x':['UG01_750_862','UG01_Leituras.Turbina_Vibracao01','13329','Turbina_Vibracao01', '16-bit Signed','INT'],
    'ug01_Vmancal_g_y':['UG01_750_862','UG01_Leituras.Turbina_Vibracao02','13330','Turbina_Vibracao02', '16-bit Signed','INT'],
    'ug01_Vmancal_c_x':['UG01_750_862','UG01_Leituras.Turbina_Vibracao03','13331','Turbina_Vibracao03', '16-bit Signed','INT'],
    'ug01_Vmancal_c_y':['UG01_750_862','UG01_Leituras.Turbina_Vibracao04','13332','Turbina_Vibracao04', '16-bit Signed','INT'],
    'ug01_Vmancal_c_z':['UG01_750_862','UG01_Leituras.Turbina_Vibracao05','13333','Turbina_Vibracao05', '16-bit Signed','INT'],
    'ug01_Ilinha_A':['USINA_750_862','USINA_Leituras.REF615_I_INST_A','13600','I_INST_A', 'Undesignated','INT'],
    'ug01_Ilinha_B':['USINA_750_862','USINA_Leituras.REF615_I_INST_B','13601','I_INST_B', 'Undesignated','INT'],
    'ug01_Ilinha_C':['USINA_750_862','USINA_Leituras.REF615_I_INST_C','13602','I_INST_C', 'Undesignated','INT'],
    'ug01_Tbarra':['USINA_750_862','USINA_Leituras.REF615_U_FaseAN','13603','USINA_Leituras.REF615_U_FaseAN', 'Undesignated','INT'],
    'ug01_Pconduto':['USINA_750_862','USINA_Leituras.TurbinaPressaoConduto_UG01','13607','U_FaseBC', 'Undesignated','INT'],
    'ug01_ac_energia_u':['USINA_750_862','USINA_Leituras.Usina_EnergiaFornecidakWh','13607','U_FaseBC', 'Undesignated','INT']
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
        TRACE("UG-1 MENSAL")
        id = 3
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
        id = 6
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
        
    else if tipo == 0 and gerador == 1 then
        TRACE("UG02 ANUAL")
        id = 2
        SetData(id,"SuperSEP",LW,LW_consulta ,1)
        GetData(erro,"SuperSEP",LW,LW_consulta_status,1)
        if erro > 0 then
            TRACE("UG02 ANUAL, Erro: %d ", erro)
            id = 3
            return id
        else
            id = 100
            return id
        end if
        
    else if tipo == 1 and gerador == 1 then
        TRACE("UG02 MENSAL")
        id = 4
        SetData(id,"SuperSEP",LW,LW_consulta ,1)
        GetData(erro,"SuperSEP",LW,LW_consulta_status,1)
        if erro > 0 then
            TRACE("UG02 MENSAL, Erro: %d ", erro) 
            id = 3
            return id
        else
            id = 100
            return id
        end if
        
    else if tipo == 2 and gerador == 1 then
        TRACE("UG02 TODOS")
        id = 6
        SetData(id,"SuperSEP",LW,LW_consulta ,1)
        GetData(erro,"SuperSEP",LW,LW_consulta_status,1)       
        if erro > 0 then
            TRACE("UG02 TODOS, Erro: %d ", erro)
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
    ROUND((MAX(ug01_acumulador_energia) - MIN(ug01_acumulador_energia))/1000, 2) AS `UG01 Acumulado mensal (MW)`
FROM 
    {table_usina}
WHERE
    ug01_acumulador_energia != 0
GROUP BY 
    YEAR(data_hora),
    MONTH(data_hora);
''',
    'anual_ug02': f'''
SELECT 
    YEAR(data_hora) AS `Ano`,
    MONTH(data_hora) AS `Mês`,
    ROUND((MAX(ug02_acumulador_energia) - MIN(ug02_acumulador_energia))/1000, 2) AS `UG02 Acumulado mensal (MW)`
FROM 
    {table_usina}
WHERE
    ug02_acumulador_energia != 0
GROUP BY 
    YEAR(data_hora),
    MONTH(data_hora);
''',
    'mensal_ug01': f'''
SELECT 
    DATE(data_hora) AS `Data`,
    ROUND((MAX(ug01_acumulador_energia) - MIN(ug01_acumulador_energia))/1000, 2) AS `UG01 Energia Diária (MW)`
FROM 
    {table_usina} 
WHERE 
    DATE(data_hora) BETWEEN '${{1}}' AND '${{2}}'
    AND (ug01_acumulador_energia > 0)
GROUP BY 
    DATE(data_hora);
''',
    'mensal_ug02': f'''
SELECT 
    DATE(data_hora) AS `Data`,
    ROUND((MAX(ug02_acumulador_energia) - MIN(ug02_acumulador_energia))/1000, 2) AS `UG02 Energia Diária (MW)`
FROM 
    {table_usina}
WHERE 
    DATE(data_hora) BETWEEN '${{1}}' AND '${{2}}'
    AND (ug02_acumulador_energia > 0)
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
ug01_horimetro_eletrico AS `horimetro eletrico`,
ROUND(ug01_distribuidor/10,2) AS `distribuidor`,
ug01_velocidade AS `velocidade`,
ROUND(ug01_acumulador_energia,2) AS `acumulador energia`,
ug01_temp_enrol_A AS `temp fase A`,
ug01_temp_enrol_B AS `temp fase B`,
ug01_temp_enrol_C AS `temp fase C` FROM {table_usina} WHERE data_hora >= '${{1}}' AND data_hora <= '${{2}}' ORDER BY data_hora DESC;
''',
    'todos_ug02': f'''
SELECT data_hora AS `data`,
ROUND(ug01_nivel_agua/100, 2) AS `nivel agua`,
ug02_tensao_fase_A AS `tensao fase A`,
ug02_tensao_fase_B AS `tensao fase B`,
ug02_tensao_fase_C AS `tensao fase C`,
ug02_corrente_fase_A AS `corrente fase A`,
ug02_corrente_fase_B AS `corrente fase B`,
ug02_corrente_fase_C AS `corrente fase C`,
ug02_tensao_excitacao AS `tensao excitacao`,
ug02_corrente_excitacao AS `corrente excitacao`,
ug02_frequencia AS `frequencia`,
ug02_potencia_ativa AS `potencia ativa`,
ug02_potencia_reativa AS `potencia reativa`,
ug02_potencia_aparente AS `potencia aparente`,
ROUND(ug02_fp/1000,2) AS `fp`,
ug02_horimetro_eletrico AS `horimetro eletrico`,
ROUND(ug02_distribuidor/10,2) AS `distribuidor`,
ug02_velocidade AS `velocidade`,
ROUND(ug02_acumulador_energia,2) AS `acumulador energia`,
ug02_temp_enrol_A AS `temp fase A`,
ug02_temp_enrol_B AS `temp fase B`,
ug02_temp_enrol_C AS `temp fase C` FROM {table_usina} WHERE data_hora >= '${{1}}' AND data_hora <= '${{2}}' ORDER BY data_hora DESC;

''',

}

'''Fluxo de execução do programa'''
fluxo = {
    'importar_tags': True,
    'criar_banco_de_dados': True,
    'criar_tabelas': True,
    'criar_comando_insert_supervisorio': True,
    'configurar_supervisorio': True,
    'criar_macro_peristir': False,
    'criar_macro_consulta_db': False,
    'criar_querys_consulta_diversas': False,

}

valores_setdata = {
    'ug01_status': 0,
    'ug01_acumulador_energia': 12.731415,
    'ug01_nivel_agua': 473,
    'ug01_Tfase_A': 45220531,
    'ug01_Tfase_B': 45286066,
    'ug01_Tfase_C': 691,
    'ug01_Ifase_A': 0,
    'ug01_Ifase_B': 0,
    'ug01_Ifase_C': 0,
    'ug01_Texcitacao': 327706,
    'ug01_Iexcitacao': 5,
    'ug01_freq': 0,
    'ug01_Pativa': 0,
    'ug01_Preativa': 0,
    'ug01_Paparente': 0,
    'ug01_fp': 0,
    'ug01_dist': 12.902832,
    'ug01_veloc': 720.000000,
    'ug01_horimetro_eletrico': 12.900013,
    'ug01_Pjusante': 17891602,
    'ug01_Pmontante': 1912602897,
    'ug01_Poleo_uhlm': 0,
    'ug01_Poleo_uhrv': 144,
    'ug01_TEenrol_A': 50.000000,
    'ug01_TEenrol_B': 51.000000,
    'ug01_TEenrol_C': 50.000000,
    'ug01_TEmancal_nucleo': 52.000000,
    'ug01_TEmancal_guia': 24.000000,
    'ug01_TEmancal_escora': 25.000000,
    'ug01_TEcsu2': 0.000000,
    'ug01_Vmancal_g_x': 0,
    'ug01_Vmancal_g_y': 0,
    'ug01_Vmancal_c_x': 0,
    'ug01_Vmancal_c_y': 0,
    'ug01_Vmancal_c_z': 0,
    'ug01_Ilinha_A': 0,
    'ug01_Ilinha_B': 0,
    'ug01_Ilinha_C': 0,
    'ug01_Tbarra': 0,
    'ug01_Pconduto': 0,
    'ug01_ac_energia_u': 0,
}
# [14:42:52] [ID 018, Line 6] Ug01_status, 20548: 0
# [14:42:52] [ID 018, Line 10] Ug01_acumulador_energia, 13491: 12.731415
# [14:42:52] [ID 018, Line 14] Ug01_nivel_agua, 13569: 473
# [14:42:52] [ID 018, Line 18] Ug01_tfase_a, 13349: 45220531
# [14:42:52] [ID 018, Line 22] Ug01_tfase_b, 13350: 45286066
# [14:42:52] [ID 018, Line 26] Ug01_tfase_c, 13351: 691
# [14:42:52] [ID 018, Line 30] Ug01_ifase_a, 13355: 0
# [14:42:52] [ID 018, Line 34] Ug01_ifase_b, 13356: 0
# [14:42:53] [ID 018, Line 38] Ug01_ifase_c, 13357: 0
# [14:42:53] [ID 018, Line 42] Ug01_texcitacao, 13383: 327706
# [14:42:53] [ID 018, Line 46] Ug01_iexcitacao, 13384: 5
# [14:42:53] [ID 018, Line 50] Ug01_freq, 13366: 0
# [14:42:53] [ID 018, Line 54] Ug01_pativa, 13359: 0
# [14:42:53] [ID 018, Line 58] Ug01_preativa, 13361: 0
# [14:42:53] [ID 018, Line 62] Ug01_paparente, 13363: 0
# [14:42:53] [ID 018, Line 66] Ug01_fp, 13365: 0
# [14:42:53] [ID 018, Line 70] Ug01_dist, 13303: 12.902832
# [14:42:53] [ID 018, Line 74] Ug01_veloc, 13307: 720.000000
# [14:42:53] [ID 018, Line 78] Ug01_horimetro_eletrico, 14105: 12.900013
# [14:42:53] [ID 018, Line 82] Ug01_pjusante, 13301: 17891602
# [14:42:53] [ID 018, Line 86] Ug01_pmontante, 13302: 1912602897
# [14:42:53] [ID 018, Line 90] Ug01_poleo_uhlm, 13289: 0
# [14:42:53] [ID 018, Line 94] Ug01_poleo_uhrv, 13295: 144
# [14:42:53] [ID 018, Line 98] Ug01_teenrol_a, 13409: 50.000000
# [14:42:53] [ID 018, Line 102] Ug01_teenrol_b, 13411: 51.000000
# [14:42:53] [ID 018, Line 106] Ug01_teenrol_c, 13413: 50.000000
# [14:42:54] [ID 018, Line 110] Ug01_temancal_nucleo, 13415: 52.000000
# [14:42:54] [ID 018, Line 114] Ug01_temancal_guia, 13417: 24.000000
# [14:42:54] [ID 018, Line 118] Ug01_temancal_escora, 13419: 25.000000
# [14:42:54] [ID 018, Line 122] Ug01_tecsu2, 13431: 0.000000
# [14:42:54] [ID 018, Line 126] Ug01_vmancal_g_x, 13329: 0
# [14:42:54] [ID 018, Line 130] Ug01_vmancal_g_y, 13330: 0
# [14:42:54] [ID 018, Line 134] Ug01_vmancal_c_x, 13331: 0
# [14:42:54] [ID 018, Line 138] Ug01_vmancal_c_y, 13332: 0
# [14:42:54] [ID 018, Line 142] Ug01_vmancal_c_z, 13333: 0
# [14:42:54] [ID 018, Line 146] Ug01_ilinha_a, 13600: 0
# [14:42:54] [ID 018, Line 150] Ug01_ilinha_b, 13601: 0
# [14:42:54] [ID 018, Line 154] Ug01_ilinha_c, 13602: 0
# [14:42:54] [ID 018, Line 158] Ug01_tbarra, 13603: 0
# [14:42:54] [ID 018, Line 162] Ug01_pconduto, 13617: 0
# [14:42:55] [ID 018, Line 166] Ug01_ac_energia_u, 13614: 0

# importar as tags
if fluxo['importar_tags']:
    def search_address(df_tags, tags_UG01):
        results = {}
        cont = 0
        # for nome_var, path_tag, address in tags:

        for key, value in tags_UG01.items():
            cont += 1
            matches = df_tags[df_tags['tag_name'].str.contains(value[1], case=False, na=False)]
            results[key] = matches

            if len(matches) > 0:
                for i in range(len(matches)):
                    addr = matches.iloc[i]['address']
                    address = matches.iloc[i]['tag_name']
                    device_name = matches.iloc[i]['device_name']
                    nome_var = key
                    tipo_var = value[5].lower()
                    tipo_var = 'int' if tipo_var == 'bigint' else tipo_var
                    tipo = 'i' if tipo_var == 'int' else 'f'
                    print(f"{tipo_var} {nome_var}")
                    print(f'GetData({nome_var}, "{device_name}", "{address}", 1)')
                    print(f'TRACE("{nome_var.capitalize()}, {addr}: %{tipo}", {nome_var})\n')
                    print(f"{nome_var} = {valores_setdata[nome_var]}")
                    print(f'SetData({nome_var}, "{device_name}", "{address}", 1)')
                    print(f'TRACE("{nome_var.capitalize()}, {addr}: %{tipo}", {nome_var})\n')
                    # print(' '*5, cont, key,':',f"{matches.iloc[i]['tag_name']}',{value[0]}, ")
                                   # f"'{matches.iloc[i]['address'], cont}'")
                    # print(' '*5, cont, key,':',f"['UG01_750_862','{matches.iloc[i]['tag_name']}',"
                    #                f"'{matches.iloc[i]['address']}','{value[1]}', "
                    #                f"'{matches.iloc[i]['format']}','{search_type(matches.iloc[i]['format'])}'],")
            else:
                print(cont, key, ': ',value[0], value[1])
            # print('_'*100)
        return results

    df_tags = importar_csv('tags_modificadas_2.csv')
    search_address(df_tags, tags_UG01)
    print('_______________________________________________________________')
    # print(df_tags.head(10))


# Criar o comando de criação do banco de dados Off-line
if fluxo['criar_banco_de_dados']:
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
    print('DROP TABLE cgh_sao_sebastiao;')
    print('_______________________________________________________________')
    print(' ')

if fluxo['criar_tabelas']:
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
                colunas += f'{name} {tipo} DEFAULT NULL,\n'
            else:
                colunas += f'{key} {tipo} DEFAULT NULL,\n'

    colunas += 'data_hora TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)'
    command = command.replace('(nome_coluna tipo configuracao)',colunas)
    print('Tamanho caracters: ', len(command))
    print(command)
    print('_______________________________________________________________')

if fluxo['criar_comando_insert_supervisorio']:
    print('_______________________________________________________________')
    print(f"----> 4) Criar insert para o supervisorio:")
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

# Configuração do supervisorio para o banco de dados
if fluxo['configurar_supervisorio']:
    print('_______________________________________________________________')
    print('_______________________________________________________________')
    print(f"----> 5) Configuração do supervisorio para o banco de dados:")
    print('_______________________________________________________________')
    print_tags(control)
    print(' ')
    # print(referencia)
    cont = 0
    for tags in tags_list:
        for key, value in tags.items():
            cont += 1
            print(cont,'-', key,'-',value[1],'-',value[4],'-',value[0])
            resp = buscar_tags(value[1])
            print(tabulate(resp, headers='keys', tablefmt='psql'))
            print('_______________________________________________________________')
    print('_______________________________________________________________')

if fluxo['criar_macro_peristir']:
    print('_______________________________________________________________')
    print(f"----> 6) MACRO:")
    print('_______________________________________________________________')
    print(macro_offline)
    print('_______________________________________________________________')

if fluxo['criar_macro_consulta_db']:
    print('_______________________________________________________________')
    print(f"----> 7) MACRO: CONSULTA OFFLINE")
    print('_______________________________________________________________')
    print(macro_offline_consulta)
    print('_______________________________________________________________')

if fluxo['criar_querys_consulta_diversas']:
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
        print(new_query)
        print('_______________________________________________________________')
        querys_consulta[key] = new_query
        # print(querys_consulta)

'''
considerando o PDF e os seguintes dados:

tag = 'UG01_Leituras.Gerador_EnergiaFornecidaMWh'
device_name = 'UG01_750_862'

preciso criar uma macro que lê a tag no dispositivo, verifica o tipo de dado, converte para float e imprime com trace 
o valor, pode me ajudar? 

macro_command main()

// esse é um exemplo de como ler uma tag e imprimir o valor com trace
// mas preciso saber o tipo de dado para converter para float

int ug01_Ifase_B
GetData(ug01_Ifase_B, "UG01_750_852", "UG01_Leituras.F50_I_FaseB", 1)
TRACE("Ug01_ifase_b, 13356: %i", ug01_Ifase_B)

int ug01_Ifase_C
GetData(ug01_Ifase_C, "UG01_750_852", "UG01_Leituras.F50_I_FaseC", 1)
TRACE("Ug01_ifase_c, 13357: %i", ug01_Ifase_C)

end macro_command
'''