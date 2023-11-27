import check50
import check50.c

@check50.check()
def existe():
    """populacao.c existe"""
    check50.exists("populacao.c")

@check50.check(existe)
def compilar():
    """populacao.c compila"""
    check50.c.compile("populacao.c", lcs50=True)

@check50.check(compilar)
def inicio_menor():
    """lida com valores iniciais menores que 9"""
    check50.run("./populacao").stdin("8").stdin("8").reject()

@check50.check(compilar)
def fim_menor():
    """lida com valores de término menores que os valores iniciais"""
    check50.run("./populacao").stdin("50").stdin("49").reject()

@check50.check(compilar)
def truncamento_decimal():
    """lida com um número decimal de lhamas"""
    check50.run("./populacao").stdin("1100").stdin("1192").stdout("Anos: 2").exit(0)

@check50.check(compilar)
def mesmo_valor():
    """lida com tamanhos iniciais e finais iguais"""
    check50.run("./populacao").stdin("100").stdin("100").stdout("Anos: 0").exit(0)

@check50.check(compilar)
def teste1():
    """lida com uma população inicial de 1200"""
    check50.run("./populacao").stdin("1200").stdin("1300").stdout("Anos: 1").exit(0)

@check50.check(compilar)
def teste2():
    """rejeita populações inválidas e então lida com uma população de 9"""
    check50.run("./populacao").stdin("-5").stdin("3").stdin("9").stdin("5").stdin("18").stdout("Anos: 8").exit(0)

@check50.check(compilar)
def teste3():
    """rejeita populações inválidas e então lida com uma população de 20"""
    check50.run("./populacao").stdin("20").stdin("1").stdin("10").stdin("100").stdout("Anos: 20").exit(0)

@check50.check(compilar)
def teste4():
    """lida com uma população inicial de 100"""
    check50.run("./populacao").stdin("100").stdin("1000000").stdout("Anos: 115").exit(0)