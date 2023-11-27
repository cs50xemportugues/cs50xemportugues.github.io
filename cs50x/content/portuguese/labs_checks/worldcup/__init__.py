import os
import re
import check50
import check50.py

BRACKET2 = [
    {"equipe": "Uruguai", "classificação": 976},
    {"equipe": "Portugal", "classificação": 1306},
]
BRACKET4 = [
    {"equipe": "Uruguai", "classificação": 976},
    {"equipe": "Portugal", "classificação": 1306},
    {"equipe": "França", "classificação": 1166},
    {"equipe": "Argentina", "classificação": 1254},
]
BRACKET8 = [
    {"equipe": "Uruguai", "classificação": 976},
    {"equipe": "Portugal", "classificação": 1306},
    {"equipe": "França", "classificação": 1166},
    {"equipe": "Argentina", "classificação": 1254},
    {"equipe": "Brasil", "classificação": 1384},
    {"equipe": "México", "classificação": 1008},
    {"equipe": "Bélgica", "classificação": 1346},
    {"equipe": "Japão", "classificação": 528},
]
BRACKET16 = [
    {"equipe": "Uruguai", "classificação": 976},
    {"equipe": "Portugal", "classificação": 1306},
    {"equipe": "França", "classificação": 1166},
    {"equipe": "Argentina", "classificação": 1254},
    {"equipe": "Brasil", "classificação": 1384},
    {"equipe": "México", "classificação": 1008},
    {"equipe": "Bélgica", "classificação": 1346},
    {"equipe": "Japão", "classificação": 528},
    {"equipe": "Espanha", "classificação": 1162},
    {"equipe": "Rússia", "classificação": 493},
    {"equipe": "Croácia", "classificação": 975},
    {"equipe": "Dinamarca", "classificação": 1054},
    {"equipe": "Suécia", "classificação": 889},
    {"equipe": "Suíça", "classificação": 1179},
    {"equipe": "Colômbia", "classificação": 989},
    {"equipe": "Inglaterra", "classificação": 1040},
]
QUESTIONS = [
    "Quais previsões, se houver, se mostraram incorretas conforme você aumentou o número de simulações?",
    'Suponha que você seja cobrado uma taxa por cada segundo de tempo de computação que seu programa usa.\nApós quantas simulações você consideraria as previsões "suficientemente boas"?',
]
SIMULATION_RUNS = [
    "10",
    "100",
    "1000",
    "10000",
    "100000",
    "1000000",
]


@check50.check()
def existe():
    """o arquivo tournament.py existe"""
    check50.exists("tournament.py", "answers.txt")
    check50.include("2018m.csv", "2019w.csv")


@check50.check(existe)
def importações():
    """o arquivo tournament.py tem as importações corretas"""
    check50.py.import_("tournament.py")


@check50.check(importações)
def sim_torneio_2():
    """o simulate_tournament lida com uma tabela de tamanho 2"""
    verificar_torneio(BRACKET2)


@check50.check(importações)
def sim_torneio_4():
    """o simulate_tournament lida com uma tabela de tamanho 4"""
    verificar_torneio(BRACKET4)


@check50.check(importações)
def sim_torneio_8():
    """o simulate_tournament lida com uma tabela de tamanho 8"""
    verificar_torneio(BRACKET8)


@check50.check(importações)
def sim_torneio_16():
    """o simulate_tournament lida com uma tabela de tamanho 16"""
    verificar_torneio(BRACKET16)


@check50.check(importações)
def contagens():
    """mantém o rastreamento correto das vitórias"""
    atual = check50.run("python3 tournament.py 2018m.csv").stdout()
    porcentagens = re.findall("[0-9]*\.[0-9]", atual)
    porcentagens = [float(x) for x in porcentagens]
    if sum(porcentagens) < 99 or sum(porcentagens) > 101:
        raise check50.Failure("falha ao manter o rastreamento das vitórias")


@check50.check(importações)
def equipes_corretas1():
    """informa corretamente as informações das equipes para Copa do Mundo Masculina"""
    atual = check50.run("python3 tournament.py 2018m.csv").stdout()
    esperado = ["Bélgica", "Brasil", "Portugal", "Espanha"]
    não_esperado = ["Alemanha"]
    for equipe in esperado:
        if equipe not in atual:
            raise check50.Failure(f"não encontrou a equipe {equipe}")
    for equipe in não_esperado:
        if equipe in atual:
            raise check50.Failure(f"encontrou erroneamente a equipe {equipe}")


@check50.check(importações)
def equipes_corretas2():
    """informa corretamente as informações das equipes para Copa do Mundo Feminina"""
    atual = check50.run("python3 tournament.py 2019w.csv").stdout()
    esperado = ["Alemanha", "Estados Unidos", "Inglaterra"]
    não_esperado = ["Bélgica"]
    for equipe in esperado:
        if equipe not in atual:
            raise check50.Failure(f"não encontrou a equipe {equipe}")
    for equipe in não_esperado:
        if equipe in atual:
            raise check50.Failure(f"encontrou erroneamente a equipe {equipe}")

    porcentagens = re.findall("[0-9]*\.[0-9]", atual)
    porcentagens = [float(x) for x in porcentagens]
    if sum(porcentagens) < 99 or sum(porcentagens) > 101:
        raise check50.Failure("falha ao manter o rastreamento das vitórias")


@check50.check(importações)
def verificar_respostas():
    """o arquivo answers.txt está completo"""
    with open("answers.txt") as f:
        conteudo = f.read()

        # Verificar tempos
        for simulações in SIMULATION_RUNS:
            correspondência = re.search(
                rf"(?i){re.escape(simulações)} simulações:\s*(\d+m\d+\.\d\d\ds)(?<!0m0\.000s)",
                conteudo,
            )
            if not correspondência:
                raise check50.Failure(
                    "o arquivo answers.txt não inclui tempos para cada número de simulações",
                    help="Você colocou todas as suas respostas no formato 0m0.000s?",
                )

        # Verificar resposta livre
        num_perguntas = len(QUESTIONS)
        for i, pergunta in enumerate(QUESTIONS):

            # Pesquisar pela pergunta, com pelo menos 3 palavras depois
            if i + 1 < num_perguntas:

                # Regex inclui a pergunta sendo feita, resposta e pergunta seguinte
                regex = (
                    rf"(?i){re.escape(pergunta)}"
                    + r":\s*(\S+\s+){3,}"
                    + rf"{re.escape(QUESTIONS[i + 1])}"
                )
            else:

                # Último regex inclui apenas a pergunta sendo feita e resposta
                regex = rf"(?i){re.escape(pergunta)}" + r":\s*(\S+\s+){3,}"

            correspondência = re.search(regex, conteudo)
            if not correspondência:
                raise check50.Failure(
                    "o arquivo answers.txt não inclui respostas para as perguntas da resposta livre",
                    help="Você escreveu uma resposta suficiente para cada pergunta?",
                )


# Funções auxiliares


def verificar_rodada(*args):
    torneio = check50.py.import_("tournament.py")
    atual = torneio.simulate_round(args[0])

    for i in range(len(atual)):
        esperado = [args[0][2 * i], args[0][2 * i + 1]]
        if not (atual[i] in esperado):
            raise check50.Failure(
                "o simulate_round falhou ao determinar os vencedores em uma rodada"
            )


def verificar_torneio(*args):
    torneio = check50.py.import_("tournament.py")
    atual = torneio.simulate_tournament(args[0])
    equipes = [x["equipe"] for x in args[0]]

    if not atual in equipes:
        raise check50.Failure(
            "o simulate_tournament falhou ao retornar o nome de 1 equipe vencedora"
        )
