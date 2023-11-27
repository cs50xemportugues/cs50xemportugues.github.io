'import os
import re
import check50
import check50.py

CHAVEIRO2 = [
    {"time": "Uruguai", "classificação": 976},
    {"time": "Portugal", "classificação": 1306},
]
CHAVEIRO4 = [
    {"time": "Uruguai", "classificação": 976},
    {"time": "Portugal", "classificação": 1306},
    {"time": "França", "classificação": 1166},
    {"time": "Argentina", "classificação": 1254},
]
CHAVEIRO8 = [
    {"time": "Uruguai", "classificação": 976},
    {"time": "Portugal", "classificação": 1306},
    {"time": "França", "classificação": 1166},
    {"time": "Argentina", "classificação": 1254},
    {"time": "Brasil", "classificação": 1384},
    {"time": "México", "classificação": 1008},
    {"time": "Bélgica", "classificação": 1346},
    {"time": "Japão", "classificação": 528},
]
CHAVEIRO16 = [
    {"time": "Uruguai", "classificação": 976},
    {"time": "Portugal", "classificação": 1306},
    {"time": "França", "classificação": 1166},
    {"time": "Argentina", "classificação": 1254},
    {"time": "Brasil", "classificação": 1384},
    {"time": "México", "classificação": 1008},
    {"time": "Bélgica", "classificação": 1346},
    {"time": "Japão", "classificação": 528},
    {"time": "Espanha", "classificação": 1162},
    {"time": "Rússia", "classificação": 493},
    {"time": "Croácia", "classificação": 975},
    {"time": "Dinamarca", "classificação": 1054},
    {"time": "Suécia", "classificação": 889},
    {"time": "Suíça", "classificação": 1179},
    {"time": "Colômbia", "classificação": 989},
    {"time": "Inglaterra", "classificação": 1040},
]
PERGUNTAS = [
    "Quais previsões, se houver, se provaram incorretas ao aumentar o número de simulações?",
    'Suponha que você seja cobrado uma taxa por cada segundo de tempo de computação que seu programa usa.\nApós quantas simulações você chamaria as previsões de "suficientemente boas"?',
]
SIMULACOES = [
    "10",
    "100",
    "1000",
    "10000",
    "100000",
    "1000000",
]


@check50.check()
def existe():
    """tournament.py existe"""
    check50.exists("tournament.py", "answers.txt")
    check50.include("2018m.csv", "2019w.csv")


@check50.check(existe)
def importacoes():
    """tournament.py importa"""
    check50.py.import_("tournament.py")


@check50.check(importacoes)
def simula_torneio_2():
    """simulate_tournament manipula um chaveiro de tamanho 2"""
    check_tournament(CHAVEIRO2)


@check50.check(importacoes)
def simula_torneio_4():
    """simulate_tournament manipula um chaveiro de tamanho 4"""
    check_tournament(CHAVEIRO4)


@check50.check(importacoes)
def simula_torneio_8():
    """simulate_tournament manipula um chaveiro de tamanho 8"""
    check_tournament(CHAVEIRO8)


@check50.check(importacoes)
def simula_torneio_16():
    """simulate_tournament manipula um chaveiro de tamanho 16"""
    check_tournament(CHAVEIRO16)


@check50.check(importacoes)
def contagem():
    """rastreia corretamente as vitórias"""
    atual = check50.run("python3 tournament.py 2018m.csv").stdout()
    porcentagens = re.findall("[0-9]*\.[0-9]", atual)
    porcentagens = [float(x) for x in porcentagens]
    if sum(porcentagens) < 99 or sum(porcentagens) > 101:
        raise check50.Failure("falha em rastrear as vitórias")


@check50.check(importacoes)
def times_corretos1():
    """reporta corretamente as informações do time para a Copa do Mundo Masculina"""
    atual = check50.run("python3 tournament.py 2018m.csv").stdout()
    esperado = ["Bélgica", "Brasil", "Portugal", "Espanha"]
    inesperado = ["Alemanha"]
    for time in esperado:
        if time not in atual:
            raise check50.Failure(f"não encontrou o time {time}")
    for time in inesperado:
        if time in atual:
            raise check50.Failure(f"encontrou incorretamente o time {time}")


@check50.check(importacoes)
def times_corretos2():
    """reporta corretamente as informações do time para a Copa do Mundo Feminina"""
    atual = check50.run("python3 tournament.py 2019w.csv").stdout()
    esperado = ["Alemanha", "Estados Unidos", "Inglaterra"]
    inesperado = ["Bélgica"]
    for time in esperado:
        if time not in atual:
            raise check50.Failure(f"não encontrou o time {time}")
    for time in inesperado:
        if time in atual:
            raise check50.Failure(f"encontrou incorretamente o time {time}")

    porcentagens = re.findall("[0-9]*\.[0-9]", atual)
    porcentagens = [float(x) for x in porcentagens]
    if sum(porcentagens) < 99 or sum(porcentagens) > 101:
        raise check50.Failure("falha em rastrear as vitórias")


@check50.check(importacoes)
def verifica_respostas():
    """answers.txt está completo"""
    with open("answers.txt") as f:
        conteudo = f.read()

        # Verifica temporizações
        for simulacoes in SIMULACOES:
            match = re.search(
                rf"(?i){re.escape(simulacoes)} simulações:\s*(\d+m\d+\.\d\d\ds)(?<!0m0\.000s)",
                conteudo,
            )
            if not match:
                raise check50.Failure(
                    "answers.txt não inclui tempo para cada número de simulações",
                    help="Você colocou todas as suas respostas no formato 0m0.000s?",
                )

        # Verifica resposta livre
        num_perguntas = len(PERGUNTAS)
        for i, pergunta in enumerate(PERGUNTAS):

            # Procura pela pergunta, com pelo menos 3 palavras depois
            if i + 1 < num_perguntas:

                # Regex inclui pergunta sendo feita, resposta e próxima pergunta
                regex = (
                    rf"(?i){re.escape(pergunta)}"
                    + r":\s*(\S+\s+){3,}"
                    + rf"{re.escape(PERGUNTAS[i + 1])}"
                )
            else:

                # Último regex inclui pergunta sendo feita e resposta
                regex = rf"(?i){re.escape(pergunta)}" + r":\s*(\S+\s+){3,}"

            match = re.search(regex, conteudo)
            if not match:
                raise check50.Failure(
                    "answers.txt não inclui respostas às perguntas de resposta livre",
                    help="Você escreveu uma resposta suficiente para cada pergunta?",
                )


# Auxiliares


def check_round(*args):
    torneio = check50.py.import_("tournament.py")
    atual = torneio.simulate_round(args[0])

    for i in range(len(atual)):
        esperado = [args[0][2 * i], args[0][2 * i + 1]]
        if not (atual[i] in esperado):
            raise check50.Failure(
                "simulate_round não consegue determinar os vencedores em uma rodada"
            )


def check_tournament(*args):
    torneio = check50.py.import_("tournament.py")
    atual = torneio.simulate_tournament(args[0])
    times = [x["time"] for x in args[0]]

    if not atual in times:
        raise check50.Failure(
            "simulate_tournament não retorna o nome de 1 time vencedor"
        )
'