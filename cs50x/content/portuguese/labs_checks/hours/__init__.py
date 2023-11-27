import check50
import check50.c


@check50.check()
def existe():
    """hours.c existe"""
    check50.exists("hours.c")


@check50.check(existe)
def compila():
    """hours.c compila"""
    check50.c.compile("hours.c", lcs50=True)


@check50.check(compila)
def soma_3_semanas():
    """hours soma as horas ao longo de 3 semanas."""
    verificar_horas(tipo="T", dados=[8, 8, 10], esperado="26")


@check50.check(compila)
def soma_5_semanas():
    """hours soma as horas ao longo de 5 semanas."""
    verificar_horas(tipo="T", dados=[5, 5, 6, 7, 8], esperado="31")


@check50.check(compila)
def media_3_semanas():
    """hours calcula a média das horas ao longo de 3 semanas."""
    verificar_horas(tipo="A", dados=[8, 9, 10], esperado="9")


@check50.check(compila)
def media_5_semanas():
    """hours calcula a média das horas ao longo de 4 semanas."""
    verificar_horas(tipo="A", dados=[8, 8, 8, 6], esperado="7.5")


# Funções auxiliares
def verificar_horas(tipo: str, dados: list, esperado: str):
    programa = check50.run("./hours").stdin(str(len(dados)))
    for horas in dados:
        programa.stdin(str(horas))
    programa.stdin(tipo).stdout(esperado)