import check50
import check50.c

@check50.check()
def existe():
    """ola.c existe"""
    check50.exists("ola.c")

@check50.check(existe)
def compila():
    """ola.c compila"""
    check50.c.compile("ola.c", lcs50=True)

@check50.check(compila)
def ramon():
    """responde ao nome Ramon"""
    check50.run("./ola").stdin("Ramon").stdout("Ramon").exit()

@check50.check(compila)
def rodrigo():
    """responde ao nome Rodrigo"""
    check50.run("./ola").stdin("Rodrigo").stdout("Rodrigo").exit()