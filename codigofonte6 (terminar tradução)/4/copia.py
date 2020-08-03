# Transforma a primeira letra da cópia de uma string em maiúscula

from cs50 import get_string

# Recebe uma string
s = get_string("s: ")

# Copia a string
t = s

# Transforma a primeira letra da cópia em maiúscula
t = t.capitalize()

# Imprime as strings
print(f"s: {s}")
print(f"t: {t}")
