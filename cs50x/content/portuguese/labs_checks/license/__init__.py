import check50
import check50.c


@check50.check()
def existe():
    """license.c existe"""
    check50.exists("license.c")
    check50.include("plates.txt")


@check50.check(existe)
def compila():
    """license.c compila"""
    check50.c.compile("license.c", lcs50=True)


@check50.check(compila)
def valido():
    """license imprime todas as placas."""
    check50.run("./license plates.txt").stdout("11ZT00\n1KAD21\n78ZZ01\n99ZZ11\n72ZZ21\n98ZZ31\n44ZW41\n34ZZ51")