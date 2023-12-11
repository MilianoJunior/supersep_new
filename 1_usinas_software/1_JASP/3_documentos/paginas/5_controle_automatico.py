
entradas = {
    'RegV_TurbinaParada': True,
    'TurbinaFechada': True,
    'ModoAuto_UPGM': False,
    'ModoAuto_UMD': False,
    'ModoAuto_UPS': False,
    'ModoAuto_US': False,
    'UHRV_Operacional': False,
    'UHRV_Desligado': True,
    'UHLM_Operacional': False,
    'UHLM_Desligado': True,
    'SFA_Operacional': True,
    'SFA_Desligado': False,

    'UHLM_Operacional': True,
    'URV_Operacional': True,
    'SFA_Operacional': True,
    'Turbina_Operacional': True,
    'RegV_Habilitado': False,
    'ModoAuto_UMD': False,
    'ModoAuto_UPS': False,
    'ModoAuto_US': False
}




class ModoAutomatico:

    def __init__(self, UP, UPGM, UMD, UPS, US):
        self.UP = UP
        self.UPGM = UPGM
        self.UMD = UMD
        self.UPS = UPS
        self.US = US

        self.ModoAuto_UP = self.Ativa_Modo_Auto_UP()
        self.ModoAuto_UPGM = self.Ativa_Modo_Auto_UPGM()
        # self.ModoAuto_UMD = self.Ativa_Modo_Auto_UMD()

    def __str__(self):
        '''Retorna o estado atual do modo automático'''
        return f'UP: {self.UP}, UPGM: {self.UPGM}, UMD: {self.UMD}, UPS: {self.UPS}, US: {self.US}'

    def Ativa_Modo_Auto_UP(self):
        '''Ativa o modo automático UP'''

        # Condição para ativação do modo automático UP
        sequencia_esperada = {
                    'RegV_TurbinaParada': True,
                    'TurbinaFechada': True,
                    'ModoAuto_UPGM': False,
                    'ModoAuto_UMD': False,
                    'ModoAuto_UPS': False,
                    'ModoAuto_US': False,
                    'UHRV_Operacional': False,
                    'UHRV_Desligado': True,
                    'UHLM_Operacional': False,
                    'UHLM_Desligado': True,
                    'SFA_Operacional': True,
                    'SFA_Desligado': True
                }

        # Verifica se a sequência esperada é igual a sequência atual
        if sequencia_esperada == entradas:
            return True

        return False

    def Ativa_Modo_Auto_UPGM(self):
        '''Ativa o modo automático UPGM'''

        # Condição para ativação do modo automático UP
        sequencia_esperada = {
                    'UHLM_Operacional': True,
                    'UHRV_Operacional': True,
                    'SFA_Operacional': True,
                    'Turbina_Operacional': True,
                    'RegV_Habilitado': False,
                    'ModoAuto_UMD': False,
                    'ModoAuto_UPS': False,
                    'ModoAuto_US': False
                }

        # Verifica se a sequência esperada é igual a sequência atual
        if sequencia_esperada == entradas:
            return True

        return False





if __name__ == '__main__':
    modo = ModoAutomatico(True, False, False, False, False)
    print(modo)
    print(modo.Ativa_Modo_Auto_UP())
    print(modo.Ativa_Modo_Auto_UPGM())
    print(' ')




















'''
 Sobre o controle automático
 
 O controle automático é feito através de um bloco de função (FB) que recebe os seguintes parâmetros:
    Entradas:
        ModoAuto_SelecionaAlvoUP: bool = [ True, Reset, False ]     # UP = Unidade Parada
        ModoAuto_SelecionaAlvoUPGM: bool = [ True, Reset, False ]   # UPGM = Unidade Pronta para Giro Meccânico
        ModoAuto_SelecionaAlvoUMD: bool = [ True, Reset, False ]    # UMD = Unidade Marcha desexcitada
        ModoAuto_SelecionaAlvoUPS: bool = [ True, Reset, False ]    # UPS = Unidade Pronta para Sincronismo
        ModoAuto_SelecionaAlvoUS: bool = [ True, Reset, False ]     # US = Unidade Sincronizada

    Condições dos contatos para ativação do controle automático:

         1 - ModoAuto_UP (Condição da máquina parada) Bobina de saída
            RegV_TurbinaParada: bool = True
            TurbinaFechada: bool = True
            ModoAuto_UPGM: bool = False
            ModoAuto_UMD: bool = False
            ModoAuto_UPS: bool = False
            ModoAuto_US: bool = False
            UHRV_Operacional: bool = False
            UHRV_Desligado: bool = True
            UHLM_Operacional: bool = False
            UHLM_Desligado: bool = True
            SFA_Operacional: bool = True
            SFA_Desligado: bool = True

         2 - ModoAuto_UPGM (Condição da máquina pronta para giro mecânico) Bobina de saída
            UHLM_Operacional: bool = True
            URV_Operacional: bool = True
            SFA_Operacional: bool = True
            Turbina_Operacional: bool = True
            RegV_Habilitado: bool = False
            ModoAuto_UMD: bool = False
            ModoAuto_UPS: bool = False
            ModoAuto_US: bool = False

        3 - ModoAuto_UMD (Condição da máquina marcha desexcitada) Bobina de saída
            RegV_Habilitado: bool = True
            RegV_RPM090: bool = True
            RegT_Habilitado: bool = False
            ModoAuto_UPS: bool = False
            ModoAuto_US: bool = False

        4 - ModoAuto_UPS (Condição da máquina pronta para sincronismo) Bobina de saída
            RegT_Habilitado: bool = True
            RegT_TensaoEstabilizada: bool = True
            Disj52G_Fechado: bool = False
            ModoAuto_US: bool = False

        5 - ModoAuto_US (Condição da máquina sincronizada) Bobina de saída
            Disj52G_Fechado: bool = True


        
    Saídas:

 
 '''
'''
FUNCTION_BLOCK FB_Modo_Automatico
VAR_INPUT

	UP,
	UPGM,
	UMD,
	UPS,
	US									: BOOL;

END_VAR
VAR_OUTPUT

	ENO								: BOOL;
	StartResAquecUHLM,
	StartResAquecUHRV,
	StartUHLM,
	StartUHRV,
	StartSFA,
	StartByPass,
	StartBorboleta,
 	StartComporta,
	StartRegV,
	StartRegT,
	StartSincro						: BOOL;

	StopResAquecUHLM,
	StopResAquecUHRV,
	StopSincro,
	StopUnload,
	StopDisj52G,
	StopRegT,
	StopRegV,
	StopTurbina,
	StopComporta,
	StopSFA,
	StopUHRV,
	StopUHLM							: BOOL;

	Falha_UPtoUPGM,
	Falha_UPGMtoUMD,
	Falha_UMDtoUPS,
	Falha_UPStoUS,
	Falha_UStoUPS,
	Falha_UPStoUMD,
	Falha_UMDtoUPGM,
	Falha_UPGMtoUP				: BOOL;

	Falha_SequenciaIncompleta		: BOOL;

END_VAR
VAR

	Pulso_StartResAquecUHLM,
	Pulso_StartResAquecUHRV,
	Pulso_StartUHLM,
	Pulso_StartUHRV,
	Pulso_StartSFA,
	Pulso_StartByPass,
	Pulso_StartBorboleta,
 	Pulso_StartComporta,
	Pulso_StartRegV,
	Pulso_StartRegT,
	Pulso_StartSincro					: R_TRIG;

	Pulso_StopResAquecUHLM,
	Pulso_StopResAquecUHRV,
	Pulso_StopSincro,
	Pulso_StopUnload,
	Pulso_StopDisj52G,
	Pulso_StopRegT,
	Pulso_StopRegV,
	Pulso_StopTurbina,
	Pulso_StopComporta,
	Pulso_StopSFA,
	Pulso_StopUHRV,
	Pulso_StopUHLM					: R_TRIG;

	TON_StartResAquecUHLM,
	TON_StartResAquecUHRV,
	TON_StartUHLM,
	TON_StartUHRV,
	TON_StartSFA,
	TON_StartByPass,
	TON_StartBorboleta,
	TON_StartComporta,
	TON_StartRegV,
	TON_StartRegT,
	TON_StartSincro					: TON;

	TON_StopResAquecUHLM,
	TON_StopResAquecUHRV,
	TON_StopSincro,
	TON_StopUnload,
	TON_StopDisj52G,
	TON_StopRegT,
	TON_StopRegV,
	TON_StopTurbina,
      TON_StopComporta,
	TON_StopSFA,
	TON_StopUHRV,
	TON_StopUHLM					: TON;

	TON_EtapaUP,
	TON_EtapaUPGM,
	TON_EtapaUMD,
	TON_EtapaUPS,
	TON_EtapaUS					: TON;

	TON_FalhaUPtoUPGM,
	TON_FalhaUPGMtoUMD,
	TON_FalhaUMDtoUPS,
	TON_FalhaUPStoUS,

	TON_FalhaUStoUPS,
	TON_FalhaUPStoUMD,
	TON_FalhaUMDtoUPGM,
	TON_FalhaUPGMtoUP			: TON;

	TON_SequenciaIncompleta		: TON;

	SequenciaOperacao				: FB_Sequencia_Operacao;

END_VAR
'''
'''
self.ENO = False
self.StartResAquecUHLM = False
self.StartResAquecUHRV = False
self.StartUHLM = False
self.StartUHRV = False
self.StartSFA = False
self.StartByPass = False
self.StartBorboleta = False
self.StartComporta = False
self.StartRegV = False
self.StartRegT = False
self.StartSincro = False

self.StopResAquecUHLM = False
self.StopResAquecUHRV = False
self.StopSincro = False
self.StopUnload = False
self.StopDisj52G = False
self.StopRegT = False
self.StopRegV = False
self.StopTurbina = False
self.StopComporta = False
self.StopSFA = False
self.StopUHRV = False
self.StopUHLM = False

self.Falha_UPtoUPGM = False
self.Falha_UPGMtoUMD = False
self.Falha_UMDtoUPS = False
self.Falha_UPStoUS = False
self.Falha_UStoUPS = False
self.Falha_UPStoUMD = False
self.Falha_UMDtoUPGM = False
self.Falha_UPGMtoUP = False

self.Falha_SequenciaIncompleta = False

self.Pulso_StartResAquecUHLM = False
self.Pulso_StartResAquecUHRV = False
self.Pulso_StartUHLM = False
self.Pulso_StartUHRV = False
self.Pulso_StartSFA = False
self.Pulso_StartByPass = False
self.Pulso_StartBorboleta = False
self.Pulso_StartComporta = False

'''