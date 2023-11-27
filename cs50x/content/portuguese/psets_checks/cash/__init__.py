import check50
import check50.c


@check50.check()
def existe():
    """cash.c existe"""
    check50.exists("cash.c")


@check50.check(exists)
def compila():
    """cash.c compila"""
    check50.c.compile("cash.c", lcs50=True)


@check50.check(compiles)
def teste041():
    """entrada de 41 resulta em saída de 4"""
    check50.run("./cash").stdin("41").stdout(moedas(4), "4\n").exit(0)


@check50.check(compiles)
def teste001():
    """entrada de 1 resulta em saída de 1"""
    check50.run("./cash").stdin("1").stdout(moedas(1), "1\n").exit(0)


@check50.check(compiles)
def teste015():
    """entrada de 15 resulta em saída de 2"""
    check50.run("./cash").stdin("15").stdout(moedas(2), "2\n").exit(0)


@check50.check(compiles)
def teste160():
    """entrada de 160 resulta em saída de 7"""
    check50.run("./cash").stdin("160").stdout(moedas(7), "7\n").exit(0)


@check50.check(compiles)
def teste230():
    """entrada de 2300 resulta em saída de 92"""
    check50.run("./cash").stdin("2300").stdout(moedas(92), "92\n").exit(0)


@check50.check(compiles)
def teste_rejeita_negativo():
    """rejeita uma entrada negativa como -1"""
    check50.run("./cash").stdin("-1").reject()


@check50.check(compiles)
def teste_rejeita_foo():
    """rejeita uma entrada não-numérica como "foo" """
    check50.run("./cash").stdin("foo").reject()


@check50.check(compiles)
def teste_rejeita_vazio():
    """rejeita uma entrada não-numérica vazia "" """
    check50.run("./cash").stdin("").reject()


def moedas(num):
    # regex que combina `num` não seguido por nenhum outro número (para que moedas(2) não combine por exemplo 123)
    return fr"(?<!\d){num}(?!\d)"