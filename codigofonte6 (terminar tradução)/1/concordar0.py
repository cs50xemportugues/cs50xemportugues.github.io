# Operadores lógicos

from cs50 import get_string

# Pergunta ao usuário se ele concordar
resposta = get_string("Você concorda?\n")

# Checa se concordou
if resposta == "S" or resposta == "s":
    print("Concordou.")
elif resposta == "N" or resposta == "n":
    print("Não concordou.")
