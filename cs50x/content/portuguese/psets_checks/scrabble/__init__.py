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
def empate_case_letra():
    """lida com casos de letras corretamente"""
    check50.run("./scrabble").stdin("LETTERCASE").stdin("lettercase").stdout("[Tt]ie!?", "Empate!").exit(0)

@check50.check(compila)
def empate_pontuacao():
    """lida com pontuação corretamente"""
    check50.run("./scrabble").stdin("Punctuation!?!?").stdin("punctuation").stdout("[Tt]ie!?", "Empate!").exit(0)

@check50.check(compila)
def teste1():
    """identifica corretamente 'Question?' e 'Question!' como empate"""
    check50.run("./scrabble").stdin("Question?").stdin("Question!").stdout("[Tt]ie!?", "Empate!").exit(0)

@check50.check(compila)
def teste2():
    """identifica corretamente 'drawing' e 'illustration' como empate"""
    check50.run("./scrabble").stdin("drawing").stdin("illustration").stdout("[Tt]ie!?", "Empate!").exit(0)

@check50.check(compila)
def teste3():
    """identifica corretamente 'hai!' como vencedor sobre 'Oh,'"""
    check50.run("./scrabble").stdin("Oh,").stdin("hai!").stdout("[Pp]layer 2 [Ww]ins!?", "Jogador 2 vence!").exit(0)

@check50.check(compila)
def teste4():
    """identifica corretamente 'COMPUTER' como vencedor sobre 'science'"""
    check50.run("./scrabble").stdin("COMPUTER").stdin("science").stdout("[Pp]layer 1 [Ww]ins!?", "Jogador 1 vence!").exit(0)

@check50.check(compila)
def teste5():
    """identifica corretamente 'Scrabble' como vencedor sobre 'wiNNeR'"""
    check50.run("./scrabble").stdin("Scrabble").stdin("wiNNeR").stdout("[Pp]layer 1 [Ww]ins!?", "Jogador 1 vence!").exit(0)

@check50.check(compila)
def teste6():
    """identifica corretamente 'pig' como vencedor sobre 'dog'"""
    check50.run("./scrabble").stdin("pig").stdin("dog").stdout("[Pp]layer 1 [Ww]ins!?", "Jogador 1 vence!").exit(0)

@check50.check(compila)
def caso_complexo():
    """identifica corretamente 'Skating!' como vencedor sobre 'figure?'"""
    check50.run("./scrabble").stdin("figure?").stdin("Skating!").stdout("[Pp]layer 2 [Ww]ins!?", "Jogador 2 vence!").exit(0)