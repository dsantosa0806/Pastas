import pandas as pd
import os

table = pd.read_excel('dados.xlsx')
diretorio = 'autos' 

if not os.path.exists(diretorio):
    os.mkdir(diretorio)

for i, N_Autos in enumerate(table['auto']):
    if not os.path.exists(diretorio + '\\' + str(N_Autos)):
        os.mkdir(diretorio + '\\' + str(N_Autos))
