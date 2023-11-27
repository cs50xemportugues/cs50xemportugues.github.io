import check50
import check50.c


@check50.check()
def existe():
    """no-vowels.c existe"""
    check50.exists("no-vowels.c")


@check50.check(existe)
def compila():
    """no-vowels.c compila"""
    check50.c.compile("no-vowels.c", lcs50=True)


@check50.check(compila)
def simples():
    """A entrada "hello" produz a saída "h3ll0""""
    verifica_sem_vogais(input="hello", output="h3ll0")


@check50.check(compila)
def palavra_maior():
    """A entrada "pseudocode" produz a saída "ps3ud0c0d3""""
    verifica_sem_vogais(input="pseudocode", output="ps3ud0c0d3")


@check50.check(compila)
def letras_maiusculas():
    """A entrada "Hello World" produz a saída "H3ll0 W0rld""""
    verifica_sem_vogais(input="\"Hello World\"", output="H3ll0 W0rld")


@check50.check(compila)
def numeros():
    """A entrada "This is CS50" produz a saída "Th1s 1s CS50""""
    verifica_sem_vogais(input="\"This is CS50\"", output="Th1s 1s CS50")


# Helpers
def verifica_sem_vogais(input: str, output: str):
    check50.run(f"./no-vowels {input}").stdout(output)