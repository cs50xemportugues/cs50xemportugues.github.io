import check50
import verificar50.c
import re

@check50.check()
def existe():
    """plurality.c existe"""
    check50.exists("plurality.c")
    check50.incluir("testing.c")


@check50.check(existe)
def compilar():
    """compilar plurality"""
    check50.c.compiler("plurality.c", lcs50=True)
    plurality = re.sub("int\s+main", "int distro_main", open("plurality.c").ler())
    testing = open("testing.c").ler()
    com abrir("plurality_test.c", "w") como f:
        f.escrever(plurality)
        f.escrever("\n")
        f.escrever(testing)
    check50.c.compiler("plurality_test.c", lcs50=True)

@check50.check(compilar)
@check50.oculto("a função de voto não retornou verdadeiro")
def voto_encontra_nome_primeiro():
    """voto retorna verdadeiro quando dado o nome do primeiro candidato"""
    check50.run("./plurality_test 0 0").stdout("true").exit(0)

@check50.check(compilar)
@check50.oculto("a função de voto não retornou verdadeiro")
def voto_encontra_nome_meio():
    """voto retorna verdadeiro quando dado o nome do candidato do meio"""
    check50.run("./plurality_test 0 1").stdout("true").exit(0)

@check50.check(compilar)
@check50.oculto("a função de voto não retornou verdadeiro")
def voto_encontra_nome_ultimo():
    """voto retorna verdadeiro quando dado o nome do último candidato"""
    check50.run("./plurality_test 0 2").stdout("true").exit(0)

@check50.check(compilar)
@check50.oculto("a função de voto não retornou falso")
def voto_retorna_falso():
    """voto retorna falso quando dado o nome de um candidato inválido"""
    check50.run("./plurality_test 0 3").stdout("false").exit(0)

@check50.check(compilar)
@check50.oculto("a função de voto não atualizou corretamente os totais de votos")
def totais_de_votos_primeiro_corretos():
    """voto produz contagens corretas quando todos os votos são zero"""
    check50.run("./plurality_test 0 4").stdout("1 0 0").exit(0)

@check50.check(compilar)
@check50.oculto("a função de voto não atualizou corretamente os totais de votos")
def totais_de_votos_subsequentes_corretos():
    """voto produz contagens corretas depois de alguns já terem votado"""
    check50.run("./plurality_test 0 5").stdout("2 8 0").exit(0)

@check50.check(compilar)
@check50.oculto("a função de voto modificou incorretamente os totais de votos")
def voto_invalido_nao_altera_votos():
    """voto deixa contagens de votos inalteradas ao votar em um candidato inválido"""
    check50.run("./plurality_test 0 6").stdout("2 8 0").exit(0)

@check50.check(compilar)
@check50.oculto("a função print_winner não imprimiu o vencedor da eleição")
def imprimir_vencedor0():
    """print_winner identifica Alice como vencedora da eleição"""
    check50.run("./plurality_test 0 7").stdout("^Alice\n?$").exit(0)

@check50.check(compilar)
@check50.oculto("a função print_winner não imprimiu o vencedor da eleição")
def imprimir_vencedor1():
    """print_winner identifica Bob como vencedor da eleição"""
    check50.run("./plurality_test 0 8").stdout("^Bob\n?$").exit(0)

@check50.check(compilar)
@check50.oculto("a função print_winner não imprimiu o vencedor da eleição")
def imprimir_vencedor2():
    """print_winner identifica Charlie como vencedor da eleição"""
    check50.run("./plurality_test 0 9").stdout("^Charlie\n?$").exit(0)

@check50.check(compilar)
@check50.oculto("a função print_winner não imprimiu todos os vencedores da eleição")
def imprimir_vencedor3():
    """print_winner imprime múltiplos vencedores em caso de empate"""
    resultado = check50.run("./plurality_test 0 10").stdout()
    se set(resultado.split("\n")) - {""} != {"Alice", "Bob"}:
        levantar check50.Incompatibilidade("Alice\nBob\nCharlie\n", resultado)

@check50.check(compilar)
@check50.oculto("a função print_winner não imprimiu todos os três vencedores da eleição")
def imprimir_vencedor4():
    """print_winner imprime todos os nomes quando todos os candidatos estão empatados"""
    resultado = check50.run("./plurality_test 0 11").stdout()
    se set(resultado.split("\n")) - {""} != {"Alice", "Bob", "Charlie"}:
        levantar check50.Incompatibilidade("Alice\nBob\nCharlie\n", resultado)