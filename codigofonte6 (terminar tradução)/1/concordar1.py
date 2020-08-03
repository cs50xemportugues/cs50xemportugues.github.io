# Operadores lógicos, usnado listas

from cs50 import get_string

# Pergunta ao usuário se ele concorda
resposta = get_string("Você concorda?\n")

# Checa se concordou
if resposta.lower() in ["s", "sim"]:
    print("Concordou.")
elif resposta.lower() in ["n", "não"]:
    print("Não concordou.")
