import check50
import check50.c


@check50.check()
def existe():
    """substitution.c existe"""
    check50.exists("substitution.c")


@check50.check(existe)
def compila():
    """substitution.c compila"""
    check50.c.compile("substitution.c", lcs50=True)


@check50.check(compila)
def criptografa1():
    """criptografa "A" como "Z" usando ZYXWVUTSRQPONMLKJIHGFEDCBA como chave"""
    check50.run("./substitution ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("A").stdout("ciphertext:\s*Z\n", "ciphertext: Z\n").exit(0)


@check50.check(compila)
def criptografa2():
    """criptografa "a" como "z" usando ZYXWVUTSRQPONMLKJIHGFEDCBA como chave"""
    check50.run("./substitution ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("a").stdout("ciphertext:\s*z\n", "ciphertext: z\n").exit(0)


@check50.check(compila)
def criptografa3():
    """criptografa "ABC" como "NJQ" usando NJQSUYBRXMOPFTHZVAWCGILKED como chave"""
    check50.run("./substitution NJQSUYBRXMOPFTHZVAWCGILKED").stdin("ABC").stdout("ciphertext:\s*NJQ\n", "ciphertext: NJQ\n").exit(0)


@check50.check(compila)
def criptografa4():
    """criptografa "XyZ" como "KeD" usando NJQSUYBRXMOPFTHZVAWCGILKED como chave"""
    check50.run("./substitution NJQSUYBRXMOPFTHZVAWCGILKED").stdin("XyZ").stdout("ciphertext:\s*KeD\n", "ciphertext: KeD\n").exit(0)


@check50.check(compila)
def criptografa5():
    """criptografa "This is CS50" como "Cbah ah KH50" usando YUKFRNLBAVMWZTEOGXHCIPJSQD como chave"""
    check50.run("./substitution YUKFRNLBAVMWZTEOGXHCIPJSQD").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compila)
def criptografa6():
    """criptografa "This is CS50" como "Cbah ah KH50" usando yukfrnlbavmwzteogxhcipjsqd como chave"""
    check50.run("./substitution yukfrnlbavmwzteogxhcipjsqd").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compila)
def criptografa7():
    """criptografa "This is CS50" como "Cbah ah KH50" usando YUKFRNLBAVMWZteogxhcipjsqd como chave"""
    check50.run("./substitution YUKFRNLBAVMWZteogxhcipjsqd").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compila)
def criptografa8():
    """criptografa todos os caracteres alfabéticos usando DWUSXNPQKEGCZFJBTLYROHIAVM como chave"""
    check50.run("./substitution DWUSXNPQKEGCZFJBTLYROHIAVM").stdin("The quick brown fox jumps over the lazy dog").stdout("ciphertext:\s*Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n", "ciphertext: Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n").exit(0)


@check50.check(compila)
def criptografa9():
    """não criptografa caracteres não alfabéticos usando DWUSXNPQKEGCZFJBTLYROHIAVM como chave"""
    check50.run("./substitution DWUSXNPQKEGCZFJBTLYROHIAVM").stdin("Shh... Don't tell!").stdout("ciphertext:\s*Yqq... Sjf'r rxcc!\n", "ciphertext: Yqq... Sjf'r rxcc!\n").exit(0)


@check50.check(compila)
def trata_sem_argv():
    """trata falta de chave"""
    check50.run("./substitution").exit(1)


@check50.check(compila)
def trata_muitos_argumentos():
    """trata argumentos demais"""
    check50.run("./substitution abcdefghijklmnopqrstuvwxyz abc").exit(1)


@check50.check(compila)
def trata_tamanho_invalido():
    """trata tamanho de chave inválido"""
    check50.run("./substitution QTXDGMKIPV").exit(1)


@check50.check(compila)
def trata_caracteres_invalidos_chave():
    """trata caracteres inválidos na chave"""
    check50.run("./substitution ZWGKPMJ^YISHFEXQON[DLUACVT").exit(1)


@check50.check(compila)
def trata_caracteres_repetidos_maiusculo():
    """trata caracteres repetidos na chave em maiúsculas"""
    check50.run("./substitution FAZRDTMGQEJPWAXUSKVIYCLONH").exit(1)


@check50.check(compila)
def trata_caracteres_repetidos_minusculo():
    """trata caracteres repetidos na chave em minúsculas"""
    check50.run("./substitution fazrdtmgqejpwaxuskviyclonh").exit(1)


@check50.check(compila)
def trata_multiplos_caracteres_repetidos():
    """trata múltiplos caracteres repetidos na chave"""
    check50.run("./substitution MMCcEFGHIJKLMNOPqRqTUVWXeZ").exit(1)