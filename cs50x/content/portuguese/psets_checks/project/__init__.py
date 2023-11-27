import re
import check50

@check50.check()
def existe():
    """README.md existe"""
    check50.exists("README.md")

@check50.check(existe)
def final():
    """detalhes do projeto final"""
    texto = open("README.md").read().lower()
    if len(texto) < 2500:
        raise check50.Failure(f"A descrição não é longa o suficiente.")

    urls = re.findall('https?:\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+', texto)
    if not urls:
        raise check50.Failure(f"URL do vídeo está faltando.")