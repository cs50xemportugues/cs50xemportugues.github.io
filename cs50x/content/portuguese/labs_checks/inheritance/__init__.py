import check50
import check50.c
import re

@check50.check()
def existe():
    """inheritance.c existe"""
    check50.exists("inheritance.c")
    check50.include("testing.c")

@check50.check(existe)
def compila():
    """inheritance.c compila"""
    check50.c.compile("inheritance.c", lcs50=True)

@check50.check(existe)
def compila_teste():
    """inheritance compila teste"""
    inheritance = re.sub("int\s+main", "int distro_main", open("inheritance.c").read())
    testing = open("testing.c").read()
    with open("inheritance_test.c", "w") as f:
        f.write(inheritance)
        f.write("\n")
        f.write(testing)
    check50.c.compile("inheritance_test.c", lcs50=True)

@check50.check(compila)
def tamanho_correto():
    """create_family cria tamanho correto da familia"""
    check50.run("./inheritance_test").stdout("size_true.*").exit(0)


@check50.check(compila)
def regras_heranca_1():
    """create_family segue regras de heranca 1"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compila)
def regras_heranca_2():
    """create_family segue regras de heranca 2"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compila)
def regras_heranca_3():
    """create_family segue regras de heranca 3"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compila)
def libera_memoria():
    """free_family resulta em nao ter vazamento de memoria"""
    check50.c.valgrind("./inheritance").exit(0)