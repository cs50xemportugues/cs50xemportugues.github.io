import check50
import check50.c
import re


@check50.verifique()
def existe():
    """wordle.c existe"""
    check50.exists("wordle.c")
    check50.inclui("testing.c")
    check50.inclui("5.txt")


@check50.verifique(existe)
def compila():
    """wordle.c compila"""

    # Verificar se o código do aluno compila
    check50.c.compile("wordle.c", lcs50=True)

    # Renomear a função principal para "distro_main"
    wordle = re.sub("int\s+main", "int distro_main", open("wordle.c").leia())

    # Ler o arquivo de teste
    testing = open("testing.c").leia()

    # Combinar o código do aluno e o arquivo de teste
    com open("wordle_test.c", "w") como f:
        f.escreva(wordle)
        f.escreva("\n")
        f.escreva(testing)

    check50.c.compile("wordle_test.c", lcs50=True)


@check50.verifique(compila)
def varios_argv():
    """wordle rejeita vários argumentos de linha de comando"""
    check50.c.executa("./wordle 5 5").saida(1)


@check50.verifique(compila)
def zero_argv():
    """wordle rejeita 0 argumentos de linha de comando"""
    check50.c.executa("./wordle").saida(1)


@check50.verifique(compila)
def rejeitar_entrada():
    """wordle rejeita entradas que não sejam 5, 6, 7, ou 8"""
    para i em [3, 4, 9]:
        check50.c.executa(f"./wordle {i}").saida(1)


@check50.verifique(compila)
def rejeitar_comprimento():
    """wordle rejeita palpites que não tenham o comprimento adequado"""
    para palavra em ["cs50", "wordle", "please"]:
        check50.c.executa("./wordle_test get_guess").stdin(palavra).stdout("Digite uma palavra de 5 letras:")


@check50.verifique(compila)
def aceitar_comprimento():
    """wordle aceita palpites com comprimento adequado"""
    para palavra em ["audio", "video", "cable"]:
        check50.c.executa("./wordle_test get_guess").stdin(palavra).stdout(palavra)


@check50.verifique(compila)
def palpite_incorreto():
    """wordle reconhece palpite sem correspondências"""
    para palavra em ["movie", "poker", "child"]:
        check50.c.executa(f"./wordle_test check_word staff {palavra}").stdout(0)


@check50.verifique(compila)
def correspondencia_parcial_proximo():
    """wordle reconhece palpite com correspondência próxima"""
    para palavra em ["smile", "bison", "links"]:
        check50.c.executa(f"./wordle_test check_word crash {palavra}").stdout(1)


@check50.verifique(compila)
def correspondencia_parcial_exata():
    """wordle reconhece palpite com correspondência exata"""
    para palavra em ["squid", "claim", "fluke"]:
        check50.c.executa(f"./wordle_test check_word stare {palavra}").stdout(2)


@check50.verifique(compila)
def correspondencia_parcial_exata_e_proxima():
    """wordle reconhece palpite com correspondências exatas e próximas"""
    para palavra em ["agent", "burst", "canoe"]:
        check50.c.executa(f"./wordle_test check_word arise {palavra}").stdout(3)

        
@check50.verifique(compila)
def correspondencia_multiple_parcial():
    """wordle reconhece palpite com correspondências múltiplas"""
    para palavra em ["drops", "ghost", "ports"]:
        check50.c.executa(f"./wordle_test check_word sport {palavra}").stdout(5)


@check50.verifique(compila)
def correspondencia_exata():
    """wordle reconhece palpite correto"""
    para palavra em ["gnome", "sized", "world"]:
        check50.c.executa(f"./wordle_test check_word {palavra} {palavra}").stdout(10)