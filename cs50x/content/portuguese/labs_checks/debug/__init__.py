import check50
import check50.c


@check50.check()
def existe():
    """debug.c existe"""
    check50.exists("debug.c")


@check50.check(existe)
def compila():
    """debug.c compila"""
    check50.c.compiler("debug.c", lcs50=True)


@check50.check(compila)
def harry():
    """A entrada de "Harry" e "Godrick's Hollow" produz a saída "Olá, Harry, de Godrick's Hollow!" """
    verificar_debug(nome="Harry", local="Godrick's Hollow")


@check50.check(compila)
def dumbledore():
    """A entrada de "Dumbledore" e "Mould-on-the-Wold" produz a saída "Olá, Dumbledore, de Mould-on-the-Wold!" """
    verificar_debug(nome="Dumbledore", local="Mould-on-the-Wold")


# Funções auxiliares
def verificar_debug(nome: str, local: str):
    check50.run("./debug").entrada(nome).entrada(local).saida(f"Olá, {nome}, de {local}!")