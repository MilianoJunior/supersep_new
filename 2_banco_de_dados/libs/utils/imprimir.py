
import pandas as pd
from typing import Union
from tabulate import tabulate

class Imprimir:
    def __init__(self, texto):
        self.texto = texto

    def pr(self, text = None):
        if text is None:
            text = self.texto
        if isinstance(text, str):
            print(text)
            print('----------------------------------------')

        elif isinstance(text, pd.DataFrame):
            print(tabulate(text, headers='keys', tablefmt='psql'))

        elif isinstance(text, pd.Series):
            print(tabulate(text.to_frame(), headers='keys', tablefmt='psql'))

        elif isinstance(text, list):
            for i in text:
                print(i)
            print('----------------------------------------')
        elif isinstance(text, dict):
            for i in text:
                print(f'{i} : {text[i]}')
            print('----------------------------------------')

pr = Imprimir('teste')
if __name__ == '__main__':
    # df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    df = [i for i in range(10)]
    Imprimir(df).pr()