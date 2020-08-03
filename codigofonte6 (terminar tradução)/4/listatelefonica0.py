# Salva nomes e número em um arquivo CSV

import csv
from cs50 import get_string

# Abre o arquivo CSV
arquivo = open("listatelefonica.csv", "a")

# Recebe nome e número
nome = get_string("Nome: ")
numero = get_string("Número: ")

# Escreve no arquivo
escritor = csv.writer(arquivo)
escritor.writerow((nome, numero))

# Fecha o arquivo
arquivo.close()
