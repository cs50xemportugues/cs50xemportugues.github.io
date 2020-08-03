# Salva nome e número em um arquivo CSV

import csv
from cs50 import get_string

# Recebe nome e número
nome = get_string("Nome: ")
numero = get_string("Número: ")

# Abre o arquivo CSV
with open("listatelefonica", "a") as arquivo:

    # Escreve no arquivo
    escritor = csv.writer(arquivo)
    escritor.writerow((nome, numero))
