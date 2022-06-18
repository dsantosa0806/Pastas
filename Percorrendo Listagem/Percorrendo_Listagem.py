# Necessário utilizar a biblioteca Pandas
# Usar o compando Pip install pandas no terminal do Python para a instalação Caso o Pycharm não importe a biblioteca
# Nome da Planilha dados


import pandas as pd

## Instanciando a Tabela
## Listagem dos Ait's
table = pd.read_excel('dados.xlsx')

for i, autos in enumerate(table['auto']):
    print(f'''percorri o auto {autos}''') # Percorrendo todos os elementos da variável auto

