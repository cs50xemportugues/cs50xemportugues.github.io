import check50
import check50.c

@check50.check()
def existe():
    """readability.c existe"""
    check50.exists("readability.c")

@check50.check(existe)
def compila():
    """readability.c compila"""
    check50.c.compile("readability.c", lcs50=True)

@check50.check(compila)
def uma_sentenca():
    """manipula uma única sentença com várias palavras"""
    check50.run("./readability").stdin("Em meus anos mais jovens e vulneráveis, meu pai me deu alguns conselhos que eu tenho ponderado desde então.").stdout("Nota 7\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def uma_sentenca_outra_pontuacao():
    """manuseia pontuação dentro de uma única sentença"""
    check50.run("./readability").stdin("Há mais coisas no céu e na terra, Horácio, do que sonha a nossa vã filosofia.").stdout("Nota 9\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def uma_sentenca_completa():
    """manuseia uma sentença única mais complexa"""
    check50.run("./readability").stdin("Alice estava começando a ficar muito cansada de ficar sentada ao lado de sua irmã à beira do rio, e de não ter nada para fazer: uma ou duas vezes ela deu uma espiada no livro que sua irmã estava lendo, mas ele não tinha figuras nem conversas, \"e qual é a utilidade de um livro,\" pensou Alice \"sem figuras ou conversas?\"").stdout("Nota 8\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def multiplas_sentencas():
    """manuseia múltiplas sentenças"""
    check50.run("./readability").stdin("Harry Potter era um garoto muito incomum de muitas maneiras. Para começar, ele odiava as férias de verão mais do que qualquer outra época do ano. Além disso, ele realmente queria fazer a lição de casa, mas era obrigado a fazê-la em segredo, no meio da noite. E ele também acontecia de ser um bruxo.").stdout("Nota 5\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def multiplas_sentencas_completa():
    """manuseia múltiplas sentenças mais complexas"""
    check50.run("./readability").stdin("Era um dia frio e luminoso de abril, e os relógios batiam treze horas. Winston Smith, com o queixo enfiado no peito em esforço para fugir do vento desagradável, deslizou rapidamente pelas portas de vidro da Mansão da Vitória, embora não rápido o suficiente para evitar que um sopro de pó asqueroso entrasse com ele.").stdout("Nota 10\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def passagens_longas():
    """manuseia passagens mais longas"""
    check50.run("./readability").stdin("Quando ele estava quase fazendo treze anos, meu irmão Jem quebrou feio o braço na altura do cotovelo. Quando sarou, e receios de Jem de nunca mais conseguir jogar futebol foram apaziguados, ele raramente se sentia autoconsciente sobre sua lesão. Seu braço esquerdo era um pouco mais curto que o direito; quando ele ficava em pé ou caminhava, o dorso da mão estava em ângulo reto com o corpo, o polegar paralelo à coxa.").stdout("Nota 8\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def pontuacao_sentenca():
    """manuseia múltiplas sentenças com pontuações diferentes"""
    check50.run("./readability").stdin("Parabéns! Hoje é o seu dia. Você está a caminho de lugares incríveis! Você está partindo agora!").stdout("Nota 3\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def perguntas_no_texto():
    """manuseia perguntas no texto"""
    check50.run("./readability").stdin("Você gostaria deles aqui ou lá? Eu não gostaria deles aqui nem lá. Eu não gostaria deles em lugar algum.").stdout("Nota 2\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def antes1():
    """manuseia nível de leitura antes do Nota 1"""
    check50.run("./readability").stdin("Um peixe. Dois peixes. Peixe vermelho. Peixe azul.").stdout("Antes do Nota 1\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def nota16mais():
    """manuseia nível de leitura no Nota 16+"""
    check50.run("./readability").stdin("Uma grande classe de problemas computacionais envolve a determinação de propriedades de gráficos, grafos dirigidos, inteiros, matrizes de inteiros, famílias finitas de conjuntos finitos, fórmulas booleanas e elementos de outros domínios contáveis.").stdout("Nota 16+\n").stdout(check50.EOF).exit(0)