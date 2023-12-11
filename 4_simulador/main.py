classes = {
    1: 'Painel controle',
    2: 'Modo automático',
    3: 'Controle automático',
    4: 'Controle automático',
    5: 'UHLM',
    6: 'UHRV',
    7: 'SFA',
    8: 'Turbina',
    9: 'Regulador velocidade',
    10: 'Regulador tensão',
    11: 'Sincronismo',
    12: 'Reles bloqueio',
    13: 'Analógicos',
    14: 'Disjuntor_52G',
    15: 'Minidisjuntores',
    16: 'Vibracao',
    17: 'Reles proteção',
    18: 'Reset alarmes',
    19: 'Totalizador Potência',
    20: 'Temperaturas',
    21: 'Barragem',
    22: 'Horímetro',
    23: 'Comunicação',
}



import argparse
from pyModbusTCP.server import ModbusServer, DataHandler
from pyModbusTCP.constants import EXP_ILLEGAL_FUNCTION
from pyModbusTCP.client import ModbusClient
import multiprocessing



# some const
ALLOW_R_L = ['127.0.0.1', '192.168.0.10']
ALLOW_W_L = ['127.0.0.1']


# a custom data handler with IPs filter
class MyDataHandler(DataHandler):
    def read_coils(self, address, count, srv_info):
        if srv_info.client.address in ALLOW_R_L:
            return super().read_coils(address, count, srv_info)
        else:
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)

    def read_d_inputs(self, address, count, srv_info):
        if srv_info.client.address in ALLOW_R_L:
            return super().read_d_inputs(address, count, srv_info)
        else:
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)

    def read_h_regs(self, address, count, srv_info):
        if srv_info.client.address in ALLOW_R_L:
            return super().read_h_regs(address, count, srv_info)
        else:
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)

    def read_i_regs(self, address, count, srv_info):
        if srv_info.client.address in ALLOW_R_L:
            return super().read_i_regs(address, count, srv_info)
        else:
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)

    def write_coils(self, address, bits_l, srv_info):
        if srv_info.client.address in ALLOW_W_L:
            return super().write_coils(address, bits_l, srv_info)
        else:
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)

    def write_h_regs(self, address, words_l, srv_info):
        if srv_info.client.address in ALLOW_W_L:
            return super().write_h_regs(address, words_l, srv_info)
        else:
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)

def cliente():

    c = ModbusClient(host="localhost", auto_open=False, auto_close=False)

    # open the socket for 2 reads then close it.
    if c.open():
        # escrever nos registros
        regs_list_1 = c.write_multiple_registers(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        regs_list_2 = c.write_multiple_registers(55, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        regs_list_1 = c.read_holding_registers(0, 10)
        regs_list_2 = c.read_holding_registers(55, 10)
        print('Lista de registros 1: ', regs_list_1)
        print('Lista de registros 2: ', regs_list_2)
        c.close()

def server():
    server = ModbusServer(host='localhost', port=502, data_hdl=MyDataHandler())
    server.start()

if __name__ == '__main__':
    # Cria processos para o cliente e o servidor
    processo_cliente = multiprocessing.Process(target=cliente)
    processo_servidor = multiprocessing.Process(target=server)

    # Inicia os processos
    processo_cliente.start()
    processo_servidor.start()

    # Aguarde a conclusão dos processos (opcional)
    processo_cliente.join()
    processo_servidor.join()















# import os
# import sys
# import unidecode
#
# # print(os.path.dirname(os.path.abspath(__file__)))
# #
# # criar arquivos .py para cada página
# for i in classes.keys():
#     name = unidecode.unidecode(classes[i]).lower().replace(' ', '_')
#     print(name)
#     with open(f'libs/{str(i)}_{name}.py', 'w') as f:
#         f.write(f''' ''')
#     # os.system(f'echo paginas/pag{i}.py')


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
