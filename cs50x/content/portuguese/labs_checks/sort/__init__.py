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
    conteudo = open("answers.txt", "r").read()
    if "TODO" in conteudo:
        raise check50.Failure("Não todas as perguntas foram respondidas.")

@check50.check(existe)
def classifica():
    """classifica corretamente cada tipo de classificação"""

    check50.log("verificando se as classificações estão corretas...")

    esperado = ["classificacao1 utiliza:\s*[Bb][Uu][Bb][Bb][Ll][Ee]", "classificacao2 utiliza:\s*[Mm][Ee][Rr][Gg][Ee]", "classificacao3 utiliza:\s*[Ss][Ee][Ll][Ee][Cc][Aa][Oo]"]
    atual = open("answers.txt", "r").read()

    for e in esperado:
        if not search(e, atual):
            raise check50.Failure("Atribuição incorreta das classificações.")'