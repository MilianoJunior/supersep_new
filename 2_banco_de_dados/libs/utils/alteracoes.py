'''
1: configurar as leituras: velocidade, acumulador de energia, horimetro.

        (Tem que ser na usina)
        velocidade 13629 - INT - 16 bit signed
        acumulador de energia 13617 - REAL - 32 bit float - 495311.4375 - 495311 4.95311
        horimetro 14105 -

2: Tela do banco capacitivo: criar as tags dos 4 banco capacitivos e as tags dos modos de operação

    tags
        1: CtrlQ_ModoVARLigar, 01x12342 -> feito OK
        2: CtrlQ_ModoVARDesligar, 01x12343 -> feito OK
        3: (*01x12368*) Banco01_Ligar - UG01_Comando.Banco01_Ligar -> feito OK
        4: (*01x12369*) Banco01_Desligar - UG01_Comando.Banco01_Desligar -> feito OK
        5: (*01x12370*) Banco02_Ligar - UG01_Comando.Banco02_Ligar  -> feito OK
        6: (*01x12371*) Banco02_Desligar - UG01_Comando.Banco02_Desligar -> feito OK
        7: (*01x12372*) Banco03_Ligar - UG01_Comando.Banco03_Ligar -> feito OK
        8: (*01x12373*) Banco03_Desligar - UG01_Comando.Banco03_Desligar -> feito OK
        9: (*01x12374*) Banco04_Ligar - UG01_Comando.Banco04_Ligar -> feito OK
        10: (*01x12375*) Banco04_Desligar - UG01_Comando.Banco04_Desligar -> feito OK
        11: (*01x16529*) BancoCapacitores_ModoAutomatico -> UG01_Status.BancoCapacitores_ModoAutomatico -> feito OK
		12: (*01x16530*) BancoCapacitores_ModoManual -> UG01_Status.BancoCapacitores_ModoManual -> feito OK
		13: (*01x16556*) Status_ModoManual -> UG01_Status.Status_ModoManual -> feito OK
		14: (*01x16557*) Status_ModoAutomatico -> UG01_Status.Status_ModoAutomatico -> feito OK


Fazer as telas das comportas
conferir os alarmes das temperaturas (Mudar Nome)
criar as tags do Crtl_Modo_manual_habilitado, ctrl_modo_manual_desabilitado das comportas
criar as tags do Crtl_Modo_manual_habilitado, ctrl_modo_manual_desabilitado dos bancos capacitivos
'''
'''
macro_command main()
// Macro inverte o sinal do comando manual
// declaracao de variaveis
short statusModoManual
short statusModoaAutomatico
short modo

// leitura do status do comando manual
GetData(statusModoManual, "UG01_750_862", "UG01_Status.Status_ModoManual", 1)
GetData(statusModoaAutomatico, "UG01_750_862", "UG01_Status.Status_ModoAutomatico", 1)

// se o comando automatico estiver ligado, desliga
if (statusModoManual == 1) then
    modo = 1
    SetData(modo, "UG01_750_862", "UG01_Comando.Ctrl_Modo_Manual_Desabilitado", 1)
else
    modo = 0
    SetData(modo, "UG01_750_862", "UG01_Comando.Ctrl_Modo_Manual_Desabilitado", 1)
end if

// se o comando automatico estiver desligado, liga

if (statusModoaAutomatico == 1) then
    modo = 1
    SetData(modo, "UG01_750_862", "UG01_Comando.Ctrl_Modo_Manual_Habilitado", 1)
else
    modo = 0
    SetData(modo, "UG01_750_862", "UG01_Comando.Ctrl_Modo_Manual_Habilitado", 1)
    
end if
end macro_command


'''