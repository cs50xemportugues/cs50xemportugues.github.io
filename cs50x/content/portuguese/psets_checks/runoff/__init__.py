import check50
import check50.c
import re


@check50.check()
def existe():
    """runoff.c existe"""
    check50.exists("runoff.c")
    check50.incluir("teste.c")


@check50.check(existe)
def compila():
    """runoff compila"""
    check50.c.compiler("runoff.c", lcs50=True)
    runoff = re.sub("int\s+main", "int distro_main", open("runoff.c").ler())
    teste = open("teste.c").ler()
    with open("runoff_test.c", "w") como f:
        f.escrever(runoff)
        f.escrever("\n")
        f.escrever(teste)
    check50.c.compiler("runoff_test.c", lcs50=True)

@check50.check(compila)
@check50.hidden("função de voto não retornou verdadeiro")
def voto_retorna_verdadeiro():
    """voto retorna verdadeiro quando dado o nome de um candidato"""
    check50.run("./runoff_test 0 0").stdout("true").exit(0)

@check50.check(compila)
@check50.hidden("função de voto não retornou falso")
def voto_retorna_falso():
    """voto retorna falso quando dado o nome de um candidato inválido"""
    check50.run("./runoff_test 0 1").stdout("false").exit(0)

@check50.check(compila)
@check50.hidden("função de voto não definiu corretamente as preferências")
def voto_define_preferencia1():
    """voto define corretamente a primeira preferência para o primeiro eleitor"""
    check50.run("./runoff_test 0 2").stdout("2").exit(0)

@check50.check(compila)
@check50.hidden("função de voto não definiu corretamente as preferências")
def voto_define_preferencia2():
    """voto define corretamente a terceira preferência para o segundo eleitor"""
    check50.run("./runoff_test 0 3").stdout("0").exit(0)

@check50.check(compila)
@check50.hidden("função de voto não definiu corretamente as preferências")
def voto_define_todas_as_preferencias():
    """voto define corretamente todas as preferências para o eleitor"""
    check50.run("./runoff_test 0 4").stdout("1 0 2").exit(0)

@check50.check(compila)
@check50.hidden("função tabulate não produziu o total correto de votos")
def tabulate1():
    """tabulate conta votos quando todos os candidatos ainda estão na eleição"""
    check50.run("./runoff_test 1 5").stdout("3 3 1 0 ").exit(0)

@check50.check(compila)
@check50.hidden("função tabulate não produziu o total correto de votos")
def tabulate2():
    """tabulate conta votos quando um candidato é eliminado"""
    check50.run("./runoff_test 1 6").stdout("3 3 1 0 ").exit(0)

@check50.check(compila)
@check50.hidden("função tabulate não produziu o total correto de votos")
def tabulate3():
    """tabulate conta votos quando múltiplos candidatos são eliminados"""
    check50.run("./runoff_test 1 7").stdout("3 4 0 0 ").exit(0)

@check50.check(compila)
@check50.hidden("função tabulate não produziu o total correto de votos")
def tabulate4():
    """tabulate trata de múltiplas rodadas de preferências"""
    check50.run("./runoff_test 1 22").stdout("3 4 0 0 ").exit(0)

@check50.check(compila)
@check50.hidden("função print_winner não imprimiu o vencedor da eleição")
def print_winner1():
    """print_winner imprime o nome quando alguém tem a maioria"""
    check50.run("./runoff_test 2 8").stdout("Bob\n").exit(0)

@check50.check(compila)
@check50.hidden("função print_winner não imprimiu o vencedor e depois retorna verdadeiro")
def print_winner2():
    """print_winner retorna verdadeiro quando alguém tem a maioria"""
    check50.run("./runoff_test 2 9").stdout("Bob\ntrue").exit(0)

@check50.check(compila)
@check50.hidden("função print_winner não retornou falso")
def print_winner3():
    """print_winner retorna falso quando ninguém tem a maioria"""
    check50.run("./runoff_test 2 10").stdout("false").exit(0)

@check50.check(compila)
@check50.hidden("função print_winner não retornou falso")
def print_winner4():
    """print_winner retorna falso quando o líder tem exatamente 50% dos votos"""
    check50.run("./runoff_test 2 11").stdout("false").exit(0)

@check50.check(compila)
@check50.hidden("função find_min não identificou o mínimo correto")
def find_min1():
    """find_min retorna o número mínimo de votos para o candidato"""
    check50.run("./runoff_test 2 12").stdout("1").exit(0)

@check50.check(compila)
@check50.hidden("função find_min não identificou o mínimo correto")
def find_min2():
    """find_min retorna o mínimo quando todos os candidatos estão empatados"""
    check50.run("./runoff_test 2 13").stdout("7").exit(0)

@check50.check(compila)
@check50.hidden("função find_min não identificou o mínimo correto")
def find_min3():
    """find_min ignora os candidatos eliminados"""
    check50.run("./runoff_test 2 14").stdout("4").exit(0)

@check50.check(compila)
@check50.hidden("função is_tie não retornou verdadeiro")
def is_tie1():
    """is_tie retorna verdadeiro quando a eleição está empatada"""
    check50.run("./runoff_test 2 15").stdout("true").exit(0)

@check50.check(compila)
@check50.hidden("função is_tie não retornou falso")
def is_tie2():
    """is_tie retorna falso quando a eleição não está empatada"""
    check50.run("./runoff_test 2 16").stdout("false").exit(0)

@check50.check(compila)
@check50.hidden("função is_tie não retornou falso")
def is_tie3():
    """is_tie retorna falso quando apenas alguns dos candidatos estão empatados"""
    check50.run("./runoff_test 2 17").stdout("false").exit(0)

@check50.check(compila)
@check50.hidden("função is_tie não retornou verdadeiro")
def is_tie4():
    """is_tie detecta empate depois que alguns candidatos foram eliminados"""
    check50.run("./runoff_test 2 18").stdout("true").exit(0)

@check50.check(compila)
@check50.hidden("função eliminate não eliminou os candidatos corretos")
def eliminate1():
    """eliminate elimina o candidato em último lugar"""
    check50.run("./runoff_test 2 19").stdout("false false false true ").exit(0)

@check50.check(compila)
@check50.hidden("função eliminate não eliminou os candidatos corretos")
def eliminate2():
    """eliminate elimina múltiplos candidatos empatados em último lugar"""
    check50.run("./runoff_test 2 20").stdout("true false true false ").exit(0)

@check50.check(compila)
@check50.hidden("função eliminate não eliminou os candidatos corretos")
def eliminate3():
    """eliminate elimina candidatos depois de alguns já eliminados"""
    check50.run("./runoff_test 2 21").stdout("true false true false ").exit(0)