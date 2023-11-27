'import check50
from re import search
from re import findall

@check50.check()
def existe():
    """answers.txt existe"""
    check50.exists("answers.txt")

@check50.check(existe)
def respostas():
    """responde todas as perguntas"""
    content = open("answers.txt", "r").read()
    if "TODO" in content:
        raise check50.Failure("Não todas as perguntas foram respondidas.")

@check50.check(existe)
def classificacoes():
    """identifica corretamente cada classificação"""

    check50.log("verificando se as classificações são atribuídas corretamente...")

    esperado = ["sort1 usa:\s*[Bb][Uu][Bb][Bb][Ll][Ee]", "sort2 usa:\s*[Mm][Ee][Rr][Gg][Ee]", "sort3 usa:\s*[Ss][Ee][Ll][Ee][Cc][Tt][Ii][Oo][Nn]"]
    atual = open("answers.txt", "r").read()

    for e in esperado:
        if not search(e, atual):
            raise check50.Failure("Atribuição incorreta das classificações.")

'