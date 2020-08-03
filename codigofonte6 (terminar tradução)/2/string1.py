# Imprime string caractere por caractere

from cs50 import get_string

s = get_string("Entrada:  ")
print("Saída: ", end="")
for c in s:
    print(c, end="")
print()
