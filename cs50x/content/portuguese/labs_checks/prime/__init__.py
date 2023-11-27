import check50
import check50.c


@check50.check()
def existe():
    """prime.c existe"""
    check50.exists("prime.c")


@check50.check(existe)
def compila():
    """prime.c compila"""
    check50.c.compile("prime.c", lcs50=True)


@check50.check(compila)
def ate_10():
    """Entrada de 1 e 10 retorna todos os números primos entre 1 e 10, inclusive"""
    check50.run("./prime").stdin("1").stdin("10").stdout("2\n3\n5\n7")


@check50.check(compila)
def entre_10_e_50():
    """Entrada de 10 e 25 retorna todos os números primos entre 10 e 25, inclusive"""
    check50.run("./prime").stdin("10").stdin("25").stdout("11\n13\n17\n19\n23")


@check50.check(compila)
def entre_50_e_60():
    """Entrada de 50 e 60 retorna todos os números primos entre 50 e 60, inclusive"""
    check50.run("./prime").stdin("50").stdin("60").stdout("53\n59")