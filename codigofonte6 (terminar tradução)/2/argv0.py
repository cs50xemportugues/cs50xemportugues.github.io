# Imprime os argumentos da linha de comando, usando os índices de argv

from sys import argv

for i in range(len(argv)):
    print(argv[i])
