'import json
import os
import shlex
import itertools

import check50


@check50.check()
def valido():
    """O projeto existe e é um programa Scratch válido"""

    # Garanta que existe apenas um arquivo .sb3.
    nomes_arquivos = [nome_arquivo para nome_arquivo in os.listdir() se nome_arquivo.endswith(".sb3")]

    se len(nomes_arquivos) > 1:
        lança check50.Failure("mais de um arquivo .sb3 encontrado. Garanta que existe apenas um!")
    senão se não nomes_arquivos:
        lança check50.Failure("nenhum arquivo .sb3 encontrado")

    nome_arquivo = nomes_arquivos[0]

    # Garanta que o arquivo .sb2 descompactado contém o arquivo .json.
    se check50.run(f"descompactar {shlex.quote(nome_arquivo)}").exit():
        lança check50.Failure("arquivo .sb3 inválido")
    check50.exists("projeto.json")

    com abrir("projeto.json") como f:
        projeto = json.load(f)

    retornar projeto["alvos"]

@check50.check(valido)
def dois_sprites(projeto):
    """Projeto contém pelo menos dois sprites"""

    num_sprites = soma(não alvo["éCena"] para alvo em projeto)

    se num_sprites < 2:
        lança check50.Failure(f"apenas {num_sprites} sprite{'' se num_sprites == 1 senão 's'} encontrado, 2 necessários")

@check50.check(valido)
def não_gato(projeto):
    """Projeto contém um sprite que não é um gato"""

    ids_sprit_gato = {"bcf454acf82e4504149f7ffe07081dbc",
                      "0fb9be3e8397c983338cb71dc84d0b25"}

    se todos(alvo["éCena"] ou {fantasia["identificaçãoAtivo"] para fantasia em alvo["fantasias"]} == ids_sprit_gato para alvo em projeto):
        lança check50.Failure("nenhum sprite que não é um gato encontrado")

@check50.check(valido)
def três_blocos(projeto):
    """Projeto contém pelo menos três scripts"""

    num_blocos = soma(len(alvo["blocos"]) para alvo em projeto)
    se num_blocos < 3:
        lança check50.Failure(f"apenas {num_blocos} script{'' se num_blocos == 1 senão 's'} encontrado, 3 necessários")

@check50.check(valido)
def usa_condição(projeto):
    """Projeto usa pelo menos uma condição"""

    se não contém_blocos(projeto, ["control_repetir", "control_se_senão", "control_se", "motion_quicasabeirarCima"]):
        lança check50.Failure("nenhuma condição encontrada, 1 necessária")

@check50.check(valido)
def usa_laço(projeto):
    """Projeto usa pelo menos um laço"""

    # Pesquise nos scripts do projeto por um bloco de repetição, repetir até, ou sempre.
    se não contém_blocos(projeto, ["control_sempre", "control_repetir_até", "control_repetir"]):
        lança check50.Failure("nenhum laço encontrado, 1 necessário")

@check50.check(valido)
def usa_variável(projeto):
    """Projeto usa pelo menos uma variável"""

    se não algum(alvo["variáveis"] para alvo em projeto):
        lança check50.Failure("nenhuma variável encontrada, 1 necessária")

@check50.check(valido)
def usa_bloco_personalizado(projeto):
    """Projeto usa pelo menos um bloco personalizado"""

    se "blocos_personalizados" não em json.dumps(projeto):
        lança check50.Failure("nenhum bloco personalizado encontrado, 1 necessário")

def contém_blocos(projeto, opcodes):
    """Retorna se o projeto contém algum bloco cujos nomes estão em opcodes"""
    retornar algum(algum((isinstance(bloco, dict) e bloco["opcode"] in opcodes) para bloco em alvo["blocos"].values())
               para alvo em projeto)