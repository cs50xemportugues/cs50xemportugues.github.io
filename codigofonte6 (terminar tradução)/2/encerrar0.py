# Encerra com um valor explícito, importando argv e exit

from sys import argv, exit

if len(argv) != 2:
    print("falta um argumento de linha de comando")
    exit(1)
print(f"olá, {argv[1]}")
exit(0)
