# Abstração e escopo

from cs50 import get_int


def main():
    i = receber_inteiro_positivo()
    print(i)


# Pede ao usuário para informar um inteiro positivo
def receber_inteiro_positivo():
    while True:
        n = get_int("Inteiro positivo: ")
        if n > 0:
            break
    return n


main()
