# Encerra com um valor explícito, importando o módulo sys

import sys

if len(sys.argv) != 2:
    sys.exit("falta um argumento de linha de comando")
print(f"olá, {sys.argv[1]}")
sys.exit(0)
