# Condições e operadores relacionais

from cs50 import get_int

# Pede ao usuário para informar x
x = get_int("x: ")

# Pede ao usuário para informar y
y = get_int("y: ")

# Compara x e y
if x < y:
    print("x é menor do que y")
elif x > y:
    print("x é maior do que y")
else:
    print("x é igual à y")
