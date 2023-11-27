import re

import check50


@check50.verifique()
def existe():
    """log.sql e answers.txt existem"""
    check50.exists("log.sql", "answers.txt")

@check50.verifique(exists)
def arquivo_de_log():
    """o arquivo de log contém consultas SELECT"""

    log = open("log.sql").read().lower()
    if "select" not in log:
        raise check50.Falha(f"consultas SELECT ausentes no log.sql")

@check50.verifique(exists)
def resolvido():
    """mistério resolvido"""

    respostas = open("answers.txt").read().lower()

    ladrão = "6272756365"
    cidade = "6e657720796f726b"
    cúmplice = "726f62696e"

    for q in ["o ladrão é", "fugiu para", "o cúmplice é"]:
        if respostas.count(q) > 1:
            raise check50.Falha("formato inválido em answers.txt")

    identificar_ladrão = re.search(f"o ladrão\s*é\s*:?\s*{bytes.fromhex(ladrão).decode('utf-8')}", respostas)
    identificar_cidade = re.search(f"fugiu\s*para\s*:?\s*{bytes.fromhex(cidade).decode('utf-8')}", respostas)
    identificar_cúmplice = re.search(f"o cúmplice\s*é\s*:?\s*{bytes.fromhex(cúmplice).decode('utf-8')}", respostas)
    if not identificar_ladrão or not identificar_cidade or not identificar_cúmplice:
        raise check50.Falha(f"answers.txt não resolve corretamente o mistério")