import check50
import check50.c

@check50.check()
def existe():
    """hello.c existe"""
    check50.exists("hello.c")

@check50.check(existe)
def compila():
    """hello.c compila"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compila)
def mundo():
    """hello.c imprime \"hello, world\""""
    check50.run("./hello").stdout("hello, world").exit()