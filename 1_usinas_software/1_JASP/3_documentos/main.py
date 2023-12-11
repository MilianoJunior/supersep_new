'''
Description: Arquivo de configuração do supervisório
'''
funcoes = {
    1: 'tomada de água',
    2: 'turbinas',
    3: 'geradores',
    4: 'subestação',
    5: 'linha de transmissão',
}

paginas = {
    # 1: 'menu principal',
    1: 'Autenticação',
    2: 'Unifilar',
    3: 'Comandos manuais',
    4: 'Controle automático',
    5: 'Subestação',
    6: 'Serviços auxiliares',
    7: 'Proteções',
    8: 'Setpoints',
    9: 'Histórico de alarmes',
    10: 'Histórico de eventos',
    11: 'Matriz de sinais',
    12: 'Gráficos',
    13: 'Relatórios',
    14: 'Configurações',
}
import os
import sys
import unidecode

# print(os.path.dirname(os.path.abspath(__file__)))
#
# # criar arquivos .py para cada página
# for i in paginas.keys():
#     name = unidecode.unidecode(paginas[i]).lower().replace(' ', '_')
#     print(name)
#     with open(f'paginas/{str(i)}_{name}.py', 'w') as f:
#         f.write(f''' ''')
    # os.system(f'echo paginas/pag{i}.py')
''' 
Corrente de Linha - A:
Corrente de Linha - B:
Corrente de Linha - C:
Corrente de Neutro - Io:
Corrente de Seq. Positiva:
Corrente de Seq. Negativa:
Corrente de Seq. Zero:
Tensão de Fase - AB:
Tensão de Fase - BC:
Tensão de Fase - CA:
Tensão de Neutro - Vo
Tensão Barra - Vb:
Tensão Sincronismo - U12B:
Tensão de Seq. Positiva:
Tensão de Seq. Negativa:
Tensão de Seq. Zero:
Frequência:
Potência Ativa:
Potência Reativa:
Potência Aparente:
Fator de Potência:
'''

'''
1- Miliano, + 3 adultos + 1 criança = 5
2- feliphe + 1 adulto = 2
3- Arlindo + 1 adulto = 2
4- Jussara e suas filharadas 🤭🤣( + 3)😊😎😜😅 = 4
5- Adriano + esposa + filho = 3
6- Juliano + esposa + 2 filhos = 4
7 - Dewis = 1
8 - Bruno + esposa = 2
9 - Clóvis = 1
10- Fell = 1
11 - Juzemar + 2 adultos = 3
12 - Matheus = 1
13 - Catia = 1
14 - Rogel = 1


Total = 32 pessoas

24 adultos + 8 crianças

Quem toma Choop:
1- Miliano
2- Feliphe
3- Dewis
4- Bruno
5- Clóvis
6- Fell
7- Juzemar
8- Matheus
9- Catia
10- Rogel

Gastos

Salão: 250,00
Choop 30 litros: 537,00
Costela para 19 Kg: (0.6 * 32) = 19,20 * 30 = 576,00
Aguá e Refri: 100,00
Pão: 30,00
Salada: 20,00
Madioca: 20,00
Arroz: 20,00
Guardanapo: 10,00

Total: 1543,00

Miliano Choop: 20 * 17,00 = 340,00

Total: 1543 - 340 = 1203,00 

custo: 1203,00/24 = 50,12

'''
