# Operadores lógicos, usando expressões regulares

import re
from cs50 import get_string

# Pergunta ao usuário se ele concorda
resposta = get_string("Você concorda?\n")

# Checa se concordou

if re.search("^s(im)?$", resposta, re.IGNORECASE):
    print("Concordou.")
elif re.search("^não?$", resposta, re.IGNORECASE):
    print("Não concordou.")
