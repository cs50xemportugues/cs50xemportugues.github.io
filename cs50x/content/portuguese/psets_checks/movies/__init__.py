'from cs50 import SQL

import check50
import sqlparse


@check50.check()
def existe():
    """Arquivos SQL existem"""
    for i in range(1, 14):
        check50.exists(f"{i}.sql")
    check50.include("movies.db")


@check50.check(existe)
def teste1():
    """1.sql produz o resultado correto"""
    check_single_col(
        executar_consulta("1.sql"),
        {"Homem de Ferro", "O Cavaleiro das Trevas", "Quem Quer Ser um Milionário?", "Kung Fu Panda"},
        ordered=False,
    )


@check50.check(existe)
def teste2():
    """2.sql produz o resultado correto"""
    check_single_cell(executar_consulta("2.sql"), "1988")


@check50.check(existe)
def teste3():
    """3.sql produz o resultado correto"""
    check_single_col(
        executar_consulta("3.sql"),
        [
            "Vingadores: Guerra Infinita",
            "Pantera Negra",
            "Eighth Grade",
            "Projeto Gemini",
            "Happy Times",
            "Os Incríveis 2",
            "Kirklet",
            "Ma Rainey's Black Bottom",
            "Roma",
            "The Professor",
            "Toy Story 4",
        ],
        ordered=True,
    )


@check50.check(existe)
def teste4():
    """4.sql produz o resultado correto"""
    check_single_cell(executar_consulta("4.sql"), "2")


@check50.check(existe)
def teste5():
    """5.sql produz o resultado correto"""
    check_double_col(
        executar_consulta("5.sql"),
        [
            {"Harry Potter e a Pedra Filosofal", "2001"},
            {"Harry Potter e a Câmara Secreta", "2002"},
            {"Harry Potter e o Prisioneiro de Azkaban", "2004"},
            {"Harry Potter e o Cálice de Fogo", "2005"},
            {"Harry Potter e a Ordem da Fênix", "2007"},
            {"Harry Potter e o Enigma do Príncipe", "2009"},
            {"Harry Potter e as Relíquias da Morte: Parte 1", "2010"},
            {"Harry Potter e as Relíquias da Morte: Parte 2", "2011"},
            {"Harry Potter: Uma História de Magia", "2017"},
        ],
        ordered=True,
    )


@check50.check(existe)
def teste6():
    """6.sql produz o resultado correto"""
    check_single_cell(executar_consulta("6.sql"), "7.74")


@check50.check(existe)
def teste7():
    """7.sql produz o resultado correto"""
    check_double_col(
        executar_consulta("7.sql"),
        [
            {"A Origem", "8.8"},
            {"Toy Story 3", "8.3"},
            {"Como Treinar seu Dragão", "8.1"},
            {"Ilha do Medo", "8.1"},
            {"O Discurso do Rei", "8.0"},
            {"Harry Potter e as Relíquias da Morte: Parte 1", "7.7"},
            {"Homem de Ferro 2", "7.0"},
            {"Alice no País das Maravilhas", "6.4"},
        ],
        ordered=True,
    )


@check50.check(existe)
def teste8():
    """8.sql produz o resultado correto"""
    check_single_col(
        executar_consulta("8.sql"),
        {"Don Rickles", "Jim Varney", "Tom Hanks", "Tim Allen"},
        ordered=False,
    )


@check50.check(existe)
def teste9():
    """9.sql produz o resultado correto"""
    check_single_col(
        executar_consulta("9.sql"),
        [
            "Craig T. Nelson",
            "Richard Griffifths",
            "Samuel L. Jackson",
            "Holly Hunter",
            "Jason Lee",
            "Rupert Grint",
            "Daniel Radcliffe",
            "Emma Watson",
        ],
        ordered=True,
    )


@check50.check(existe)
def teste10():
    """10.sql produz o resultado correto"""
    check_single_col(
        executar_consulta("10.sql"),
        {"Christopher Nolan", "Frank Darabont", "Yimou Zhang"},
        ordered=False,
    )


@check50.check(existe)
def teste11():
    """11.sql produz o resultado correto"""
    check_single_col(
        executar_consulta("11.sql"),
        ["42", "Pantera Negra", "Marshall", "Ma Rainey's Black Bottom", "Get on Up"],
        ordered=True,
    )


@check50.check(existe)
def teste12():
    """12.sql produz o resultado correto"""
    try:
        check_single_col(
            executar_consulta("12.sql"),
            {
                "A Noiva Cadáver",
                "A Fantástica Fábrica de Chocolate",
                "Alice no País das Maravilhas",
                "Alice Através do Espelho",
            },
            ordered=False,
        )
    except (check50.Failure, check50.Mismatch):

        # Versão alternativa do teste12 para levar em consideração a remoção de Johnny Depp da especificação
        check_single_col(
            executar_consulta("12.sql"),
            {"O Lado Bom da Vida", "Serena", "Trapaça", "Joy"},
            ordered=False,
        )


@check50.check(existe)
def teste13():
    """13.sql produz o resultado correto"""
    check_single_col(
        executar_consulta("13.sql"),
        {
            "Bill Paxton",
            "Gary Sinise",
            "James McAvoy",
            "Jennifer Lawrence",
            "Tom Cruise",
            "Michael Fassbender",
            "Tom Hanks",
        },
        ordered=False,
    )


def executar_consulta(filename):
    try:
        with open(filename) as f:
            consulta = f.read().strip()
            consulta = sqlparse.format(consulta, strip_comments=True).strip()
        db = SQL("sqlite:///movies.db")
        resultado = db.execute(consulta)
        return resultado
    except Exception as e:
        raise check50.Failure(f"Erro ao executar a consulta: {str(e)}")


def check_single_col(atual, esperado, ordered=False):
    """
    Verifica consultas que retornam apenas uma coluna, garante resultados corretos.
    """

    # Verifica se a consulta retornou resultados
    if atual is None or atual == []:
        raise check50.Failure("A consulta não retornou resultados")

    # Verifica se há apenas uma coluna
    contagens_linha = {len(list(linha.values())) for linha in atual}
    if contagens_linha != {1}:
        raise check50.Failure("A consulta deve retornar apenas uma coluna")

    # Obter dados da coluna
    try:
        result = [str(list(linha.values())[0]) for linha in atual]
        result = result if ordered else set(result)
    except IndexError:
        return None

    # Verifica se os dados da coluna estão corretos
    esperado = [str(valor) for valor in esperado]
    if not ordered:
        esperado = set(esperado)
    if result != esperado:
        raise check50.Mismatch("\n".join(esperado), "\n".join(list(result)))


def check_single_cell(atual, esperado):
    return check_single_col(atual, [esperado], ordered=True)


def check_double_col(atual, esperado, ordered=False):
    """
    Verifica consultas que retornam apenas duas colunas, garante resultados corretos.
    """

    # Verifica se a consulta retornou resultados
    if atual is None or atual == []:
        raise check50.Failure("A consulta não retornou resultados")

    # Verifica se há exatamente duas colunas
    contagens_linha = {len(list(linha.values())) for linha in atual}
    if contagens_linha != {2}:
        raise check50.Failure("A consulta deve retornar exatamente duas colunas")

    # Obter dados das colunas
    try:
        result = []
        for linha in atual:
            valores = list(linha.values())
            result.append({str(valores[0]), str(valores[1])})
        result = result if ordered else set(result)
    except IndexError:
        return None

    # Verifica se os dados das colunas estão corretos
    if result != esperado:
        raise check50.Mismatch(
            "\n".join([str(entrada) for entrada in list(esperado)]),
            "\n".join([str(entrada) for entrada in list(result)]),
        )
'