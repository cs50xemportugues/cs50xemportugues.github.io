import check50
import check50.c


@check50.check()
def existe():
    """max.c existe"""
    check50.exists("max.c")


@check50.check(existe)
def compila():
    """max.c compila"""
    check50.c.compiler("max.c", lcs50=True)


@check50.check(compila)
def simples():
    """Retorna 3 de 0, 1, 3"""
    check_max(elementos=[0, 1, 3])


@check50.check(compila)
def negativo():
    """Retorna 4 de -10, 4, 2"""
    check_max(elementos=[-10, 4, 2])


@check50.check(compila)
def negativo_max():
    """Retorna -10 de -10, -50, -100"""
    check_max(elementos=[-10, -50, -100])


# Funções de auxílio
def check_max(elementos: lista):
    programa = check50.run("./max")
    programa.stdin(str(len(elementos)))
    for numero in elementos:
        print(programa.stdin(str(numero)))
    programa.stdout(str(max(elementos)))