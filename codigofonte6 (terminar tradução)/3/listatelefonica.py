# Implementa uma lista telefônica

import sys

pessoas = {
    "LARA": "98765-0100",
    "BRENDON": "98765-0101",
    "ANDRE": "98765-0102",
    "RAMON": "98765-0103"
}

# Procura por LARA
if "LARA" in pessoas:
    print(f"Encontrado {pessoas['LARA']}")
    sys.exit(0)
print("Não encontrado")
sys.exit(1)
