import check50
import check50.c
import re


@check50.check()
def existe():
    """half.c existe"""
    check50.exists("half.c")


@check50.check(existe)
def compila():
    """half.c compila"""
    check50.c.compile("half.c", lcs50=True)


@check50.check(compila)
def simples():
    """Conta de $50, com 10% de imposto e 20% de gorjeta, cria uma saída de $33.00"""
    verificar_meio(bill="50", tax="10", tip="20", expected="33.00")


@check50.check(compila)
def imposto_decimal():
    """Conta de $50, com 12.5% de imposto e 20% de gorjeta, cria uma saída de $33.75"""
    verificar_meio(bill="50", tax="12.5", tip="20", expected="33.75")


@check50.check(compila)
def arredondamento_para_cima():
    """Conta de $100, com 12.5% de imposto e 15% de gorjeta, cria uma saída de $64.69"""
    verificar_meio(bill="100", tax="12.5", tip="15", expected="64.69")


@check50.check(compila)
def arredondamento_para_baixo():
    """Conta de $96.40, com 13% de imposto e 14% de gorjeta, cria uma saída de $62.09"""
    verificar_meio(bill="96.40", tax="13", tip="14", expected="62.09")


# Auxiliares
def regex(input):
    """Combina com quaisquer caracteres não numéricos em qualquer extremidade da entrada"""
    return rf'^\D*\${re.escape(input)}\D*$'


def verificar_meio(bill: str, tax: str, tip: str, expected: str):
    check50.run("./half").stdin(bill).stdin(tax).stdin(tip).stdout(regex(expected), expected, regex=True)