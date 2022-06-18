# importar biblioteca os

import os

diretorio = 'autos' # Instaciando o Nome da pasta que será criada no projeto atual

if not os.path.exists(diretorio): # Verifica a existencia da pasta
    os.mkdir(diretorio)

# Criação das pastas, o tamanho é passado nos argumentos do range do laço 
for i in range(1,11): 
    if not os.path.exists(diretorio + '\\pasta_' + str(i)): # Verifica a existência da pasta
        os.mkdir(diretorio + '\\pasta_' + str(i)) #
