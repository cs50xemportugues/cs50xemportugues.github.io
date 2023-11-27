import check50
import check50.c
import os


@check50.check()
def existe():
    """dictionary.c existe"""
    check50.exists("dictionary.c")


@check50.check(existe)
def compila():
    """speller compila"""
    check50.inclui("speller.c", "Makefile")
    se não os.path.exists("dictionary.h"):
        check50.inclui("dictionary.h")
    check50.run("make").exit(0)


@check50.check(compila)
def básico():
    """lida corretamente com palavras mais básicas"""
    check50.inclui("basic")
    check50.run("./speller basic/dict basic/text").stdout(open("basic/out")).exit(0)


@check50.check(compila)
def comprimento_mínimo():
    """lida corretamente com palavras de comprimento mínimo (1 caractere)"""
    check50.inclui("min_length")
    check50.run("./speller min_length/dict min_length/text").stdout(open("min_length/out")).exit(0)


@check50.check(compila)
def comprimento_máximo():
    """lida corretamente com palavras de comprimento máximo (45 caracteres)"""
    check50.inclui("max_length")
    check50.run("./speller max_length/dict max_length/text").stdout(open("max_length/out")).exit(0)


@check50.check(compila)
def apóstrofo():
    """lida corretamente com palavras com apóstrofos"""
    check50.inclui("apostrophe")
    check50.run("./speller apostrophe/without/dict apostrophe/with/text").stdout(open("apostrophe/outs/without-with")).exit(0)
    check50.run("./speller apostrophe/with/dict apostrophe/without/text").stdout(open("apostrophe/outs/with-without")).exit(0)
    check50.run("./speller apostrophe/with/dict apostrophe/with/text").stdout(open("apostrophe/outs/with-with")).exit(0)


@check50.check(compila)
def caixa():
    """verificação ortográfica é case-insensitive"""
    check50.inclui("case")
    check50.run("./speller case/dict case/text").stdout(open("case/out")).exit(0)


@check50.check(compila)
def substring():
    """lida corretamente com substrings"""
    check50.inclui("substring")
    check50.run("./speller substring/dict substring/text").stdout(open("substring/out")).exit(0)


@check50.check(substring)
def memória():
    """programa não contém erros de memória"""
    check50.c.valgrind("./speller substring/dict substring/text").stdout(open("substring/out"), timeout=10).exit(0)