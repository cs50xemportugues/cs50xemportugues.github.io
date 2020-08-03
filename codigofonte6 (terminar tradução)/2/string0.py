# Imprime string caractere por caractere, usando os índices dos caracteres da string

from cs50 import get_string

s = get_string("Entrada:  ")
print("Saída: ", end="")
for i in range(len(s)):
    print(s[i], end="")
print()
