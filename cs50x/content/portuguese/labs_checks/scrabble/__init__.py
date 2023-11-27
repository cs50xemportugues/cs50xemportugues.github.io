import check50
import check50.c

@check50.check()
def existe():
    """scrabble.c existe"""
    check50.exists("scrabble.c")

@check50.check(existe)
def compila():
    """scrabble.c compila"""
    check50.c.compile("scrabble.c", lcs50=True)

@check50.check(compila)
def empate_letra_maiuscula():
    """trata corretamente maiúsculas e minúsculas"""
    check50.run("./scrabble").stdin("MAIÚSCULASMINÚSCULAS").stdin("maiúsculasminúsculas").stdout("[Ee]mpate!?", "Empate").exit(0)

@check50.check(compila)
def empate_pontuacao():
    """trata corretamente pontuação"""
    check50.run("./scrabble").stdin("Pontuação!?!?").stdin("pontuação").stdout("[Ee]mpate!?", "Empate").exit(0)

@check50.check(compila)
def teste1():
    """identifica corretamente 'Pergunta?' e 'Pergunta!' como empate"""
    check50.run("./scrabble").stdin("Pergunta?").stdin("Pergunta!").stdout("[Ee]mpate!?", "Empate").exit(0)

@check50.check(compila)
def teste2():
    """identifica corretamente 'desenho' e 'ilustração' como empate"""
    check50.run("./scrabble").stdin("desenho").stdin("ilustração").stdout("[Ee]mpate!?", "Empate").exit(0)

@check50.check(compila)
def teste3():
    """identifica corretamente 'hai!' como vencedor sobre 'Oh,'"""
    check50.run("./scrabble").stdin("Oh,").stdin("hai!").stdout("[Jj]ogador 2 [Gg]anha!?", "Jogador 2 ganha").exit(0)

@check50.check(compila)
def teste4():
    """identifica corretamente 'COMPUTADOR' como vencedor sobre 'ciência'"""
    check50.run("./scrabble").stdin("COMPUTADOR").stdin("ciência").stdout("[Jj]ogador 1 [Gg]anha!?", "Jogador 1 ganha").exit(0)

@check50.check(compila)
def teste5():
    """identifica corretamente 'Palavras Cruzadas' como vencedor sobre 'vEnCeDoR'"""
    check50.run("./scrabble").stdin("Palavras Cruzadas").stdin("vEnCeDoR").stdout("[Jj]ogador 1 [Gg]anha!?", "Jogador 1 ganha").exit(0)

@check50.check(compila)
def teste6():
    """identifica corretamente 'porco' como vencedor sobre 'cachorro'"""
    check50.run("./scrabble").stdin("porco").stdin("cachorro").stdout("[Jj]ogador 1 [Gg]anha!?", "Jogador 1 ganha").exit(0)

@check50.check(compila)
def caso_complexo():
    """identifica corretamente 'Patinação!' como vencedor sobre 'figura?'"""
    check50.run("./scrabble").stdin("figura?").stdin("Patinação!").stdout("[Jj]ogador 2 [Gg]anha!?", "Jogador 2 ganha").exit(0)