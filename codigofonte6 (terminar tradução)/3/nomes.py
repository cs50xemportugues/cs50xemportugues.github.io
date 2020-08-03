# Implementa pesquisa linear para uma lista de nomes

import sys

# Uma lista de nomes
nomes = ["LARA", "BRENDON", "ANDRE", "RAMON"]

# Procura LARA
if "LARA" in nomes:
    print("Encontrado")
    sys.exit(0)
print("Não encontrado")
sys.exit(1)
