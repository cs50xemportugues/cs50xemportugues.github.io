import check50
import check50.c

@check50.check()
def existe():
    """caesar.c existe."""
    check50.exists("caesar.c")

@check50.check(existe)
def compila():
    """caesar.c compila."""
    check50.c.compile("caesar.c", lcs50=True)

@check50.check(compila)
def criptografa_a_como_b():
    """criptografa "a" como "b" usando 1 como chave"""
    check50.run("./caesar 1").stdin("a").stdout("[Cc]iphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compila)
def criptografa_barfoo_como_yxocll():
    """criptografa "barfoo" como "yxocll" usando 23 como chave"""
    check50.run("./caesar 23").stdin("barfoo").stdout("[Cc]iphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(compila)
def criptografa_BARFOO_como_EDUIRR():
    """criptografa "BARFOO" como "EDUIRR" usando 3 como chave"""
    check50.run("./caesar 3").stdin("BARFOO").stdout("[Cc]iphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(compila)
def criptografa_BaRFoo_como_FeVJss():
    """criptografa "BaRFoo" como "FeVJss" usando 4 como chave"""
    check50.run("./caesar 4").stdin("BaRFoo").stdout("[Cc]iphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(compila)
def criptografa_barfoo_como_onesbb():
    """criptografa "barfoo" como "onesbb" usando 65 como chave"""
    check50.run("./caesar 65").stdin("barfoo").stdout("[Cc]iphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)

@check50.check(compila)
def verifica_tratamento_de_caractere_nao_alfa():
    """criptografa "world, say hello!" como "iadxp, emk tqxxa!" usando 12 como chave"""
    check50.run("./caesar 12").stdin("world, say hello!").stdout("[Cc]iphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)

@check50.check(compila)
def trata_falta_de_argv():
    """trata falta de argv[1]"""
    check50.run("./caesar").exit(1)

@check50.check(compila)
def trata_argv_nao_numerico():
    """trata chave não numérica"""
    check50.run("./caesar 2x").exit(1)

@check50.check(compila)
def muitos_argumentos():
    """trata excesso de argumentos"""
    check50.run("./caesar 1 2").exit(1)