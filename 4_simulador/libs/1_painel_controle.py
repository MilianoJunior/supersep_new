

class Emergencia:
    def __init__(self):
        self.Local = False
        self.SuperSEP = False
        self.UHRV = False
        self.UHLM = False
        self.Reset = False

class Modo:
    def __init__(self):
        self.Manual_Habilitado = False
        self.Automatico_Habilitado = False

class PainelControle:
    def __init__(self):
        self.Emergencia = Emergencia()
        self.Modo = Modo()
        self.Religamento = False
        self.Status_Disj52G = False
        self.Falta_DAgua = False
        self.Trip_Eletrico = False
        self.Trip_Mecanico = False
        self.Trip_Hidraulico = False
        self.Comando_Abertura = False
        self.ENO = False
        self.Eve_Parada = {
            'FaltadAgua': False,
            'Eletrica': False,
            'Mecanica': False,
            'Hidraulica': False,
            'Normal': False,
            'EmergenciaLocal': False,
            'EmergenciaSuperSEP': False,
            'EmergenciaUHRV': False,
            'EmergenciaUHLM': False,
            'Abertura52G': False,
            'InformacaoValida': False,
        }
        self.Eve_Bloqueio = False
        self.TRG_Partida_Religamento = False
        self.TRG_Partida_OperacaoManual = False
        self.TRG_Parada = {
            'FaltadAgua': False,
            'Eletrica': False,
            'Mecanica': False,
            'Parada_Hidraulica': False,
            'EmergenciaLocal': False,
            'EmergenciaSuperSEP': False,
            'EmergenciaUHRV': False,
            'EmergenciaUHLM': False,
            'Abertura52G': False,
            'Normal': False,
        }
        self.Bloqueio = False