DNA
===

Implemente um programa que identifique uma pessoa baseada em seu DNA, como abaixo.

    $ python dna.py databases/large.csv sequences/5.txt
    Lavender
    

Introdução
----------

Faça login no [code.cs50.io] (https://code.cs50.io/), clique na janela do terminal e execute `cd` isoladamente. Você deve ver que o prompt da janela do seu terminal se parece com o abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/6/dna.zip
    

para baixar um ZIP chamado `dna.zip` no seu espaço de códigos.

Em seguida, execute

    unzip dna.zip
    

para criar uma pasta chamada `dna`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm dna.zip
    

e responder com "y" seguido por Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd dna
    

seguido de Enter para mover-se para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve ser semelhante ao abaixo.

    dna/ $
    

Execute `ls` sozinho e você deve ver alguns arquivos e pastas:

    databases/ dna.py sequences/
    

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde deu errado!

Background
----------

O DNA, o portador de informações genéticas nos seres vivos, tem sido utilizado na justiça criminal por décadas. Mas como exatamente funciona o perfil de DNA? Dada uma sequência de DNA, como os investigadores forenses podem identificar a quem pertence?

Bem, o DNA é realmente apenas uma sequência de moléculas chamadas nucleotídeos, organizados em uma forma particular (uma dupla hélice). Cada célula humana tem bilhões de nucleotídeos organizados em sequência. Cada nucleotídeo do DNA contém uma das quatro bases diferentes: adenina (A), citosina (C), guanina (G) ou timina (T). Algumas partes dessa sequência (ou seja, genoma) são iguais ou pelo menos muito semelhantes em quase todos os humanos, mas outras partes da sequência têm uma diversidade genética mais alta e, portanto, variam mais na população.

Um lugar onde o DNA tende a ter uma alta diversidade genética é em Repetições em Tandem Curtas (STRs). Um STR é uma sequência curta de bases de DNA que tende a se repetir consecutivamente inúmeras vezes em locais específicos dentro do DNA de uma pessoa. O número de vezes que um determinado STR é repetido varia muito entre os indivíduos. Nas amostras de DNA abaixo, por exemplo, Alice tem o STR `AGAT` repetido quatro vezes em seu DNA, enquanto Bob tem o mesmo STR repetido cinco vezes.

![Sample STRs](https://cs50.harvard.edu/x/2023/psets/6/dna/strs.png)

Usar vários STRs, em vez de apenas um, pode melhorar a precisão do perfil de DNA. Se a probabilidade de duas pessoas terem o mesmo número de repetições para um único STR é de 5%, e o analista examina 10 STRs diferentes, então a probabilidade de que duas amostras de DNA correspondam por pura coincidência é de cerca de 1 em 1 quatrilhão (assumindo que todos os STRs são independentes entre si). Então, se as duas amostras de DNA tiverem o mesmo número de repetições para cada um dos STRs, o analista pode ter bastante confiança de que elas vieram da mesma pessoa. CODIS, o banco de dados de DNA do FBI, usa 20 STRs diferentes como parte de seu processo de perfil de DNA.

Como seria um banco de dados de DNA? Bem, em sua forma mais simples, você poderia imaginar formatar um banco de dados de DNA como um arquivo CSV, em que cada linha corresponde a um indivíduo e cada coluna corresponde a um STR específico.

    name,AGAT,AATG,TATC
    Alice,28,42,14
    Bob,17,22,19
    Charlie,36,18,25

Os dados do arquivo acima sugeririam que Alice tem a sequência `AGAT` repetida 28 vezes consecutivamente em algum lugar de seu DNA, a sequência `AATG` repetida 42 vezes e `TATC` repetida 14 vezes. Bob, por sua vez, tem os mesmos três STRs repetidos 17, 22 e 19 vezes, respectivamente. E Charlie tem os mesmos três STRs repetidos 36, 18 e 25 vezes, respectivamente.

Então, dada uma sequência de DNA, como você poderia identificar a quem ela pertence? Bem, imagine que você procurou na sequência de DNA a sequência consecutiva mais longa de `AGAT`s repetidos e descobriu que a sequência mais longa tem 17 repetições. Se você então descobrisse que a sequência mais longa de `AATG` tem 22 repetições e a sequência mais longa de `TATC` tem 19 repetições, isso forneceria uma evidência bastante boa de que o DNA pertence a Bob. Claro, é também possível que, uma vez que você tenha as contagens para cada um dos STRs, ela não coincida com ninguém em seu banco de dados de DNA, nesse caso, não haveria correspondência.

Na prática, como os analistas sabem em qual cromossomo e em qual localização do DNA um STR será encontrado, eles podem localizar sua busca apenas em uma seção estreita de DNA. Mas ignoraremos esse detalhe para este problema.

Sua tarefa é escrever um programa que aceite uma sequência de DNA e um arquivo CSV contendo contagens de STR para uma lista de indivíduos e, em seguida, produza a quem pertence esse DNA (provavelmente).

Especificação
-------------

Em um arquivo chamado `dna.py`, implemente um programa que identifique a quem pertence uma sequência de DNA.

*   O programa deve exigir como primeiro argumento na linha de comando o nome de um arquivo CSV contendo as contagens STR para uma lista de indivíduos e deve exigir como segundo argumento na linha de comando o nome de um arquivo de texto contendo a sequência de DNA a ser identificada.
    *   Se o seu programa for executado com o número incorreto de argumentos de linha de comando, o programa deve imprimir uma mensagem de erro de sua escolha (com `print`). Se o número correto de argumentos for fornecido, você pode assumir que o primeiro argumento é de fato o nome de arquivo de um arquivo CSV válido e que o segundo argumento é o nome de arquivo de um arquivo de texto válido.
*   Seu programa deve abrir o arquivo CSV e ler seu conteúdo na memória.
    *   Você pode assumir que a primeira linha do arquivo CSV será os nomes das colunas. A primeira coluna será a palavra `name` e as colunas restantes serão as próprias sequências STR.
*   Seu programa deve abrir a sequência de DNA e ler seu conteúdo na memória.
*   Para cada um dos STRs (da primeira linha do arquivo CSV), seu programa deve calcular a sequência mais longa de repetições consecutivas do STR na sequência de DNA a ser identificada. Observe que definimos uma função auxiliar para você, `longest_match`, que fará exatamente isso!
*   Se as contagens STR coincidirem exatamente com algum dos indivíduos no arquivo CSV, seu programa deve imprimir o nome do indivíduo correspondente.
    *   Você pode assumir que as contagens STR não coincidirão com mais de um indivíduo.
    *   Se as contagens STR não coincidirem exatamente com nenhum dos indivíduos no arquivo CSV, seu programa deve imprimir `No match`.

Visão Geral
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/j84b_EgntcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Uso
-----

Seu programa deve ter o comportamento mostrado no exemplo abaixo:

<pre>
$ python dna.py databases/large.csv sequences/5.txt
Lavender
</pre>

<pre>
$ python dna.py
Usage: python dna.py data.csv sequence.txt
</pre>

<pre>
$ python dna.py data.csv
Usage: python dna.py data.csv sequence.txt
</pre>

Dicas
-----

*   Você pode achar o módulo [`csv`](https://docs.python.org/pt-br/3/library/csv.html) do Python útil para ler arquivos CSV na memória. Você pode querer aproveitar [`csv.reader`](https://docs.python.org/pt-br/3/library/csv.html#csv.reader) ou [`csv.DictReader`](https://docs.python.org/pt-br/3/library/csv.html#csv.DictReader).
*   As funções [`open`](https://docs.python.org/pt-br/3.3/tutorial/inputoutput.html#reading-and-writing-files) e [`read`](https://docs.python.org/pt-br/3.3/tutorial/inputoutput.html#methods-of-file-objects) podem ser úteis para ler arquivos de texto na memória.
*   Considere quais estruturas de dados podem ser úteis para manter o controle da informação em seu programa. Uma [`list`](https://docs.python.org/pt-br/3/tutorial/introduction.html#lists) ou um [`dict`](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries) podem ser úteis.
*   Lembre-se de que definimos uma função (`longest_match`) que, em dado uma sequência de DNA e um STR como entrada, retorna o número máximo de vezes que o STR se repete. Você pode usar essa função em outras partes do seu programa!

Testando
-------

Embora o `check50` esteja disponível para este problema, você é incentivado a testar o seu código por conta própria para cada um dos seguintes items.

*   Execute o seu programa como `python dna.py databases/small.csv sequences/1.txt`. Seu programa deve produzir a saída `Bob`.
*   Execute o seu programa como `python dna.py databases/small.csv sequences/2.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/small.csv sequences/3.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/small.csv sequences/4.txt`. Seu programa deve produzir a saída `Alice`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/5.txt`. Seu programa deve produzir a saída `Lavender`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/6.txt`. Seu programa deve produzir a saída `Luna`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/7.txt`. Seu programa deve produzir a saída `Ron`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/8.txt`. Seu programa deve produzir a saída `Ginny`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/9.txt`. Seu programa deve produzir a saída `Draco`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/10.txt`. Seu programa deve produzir a saída `Albus`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/11.txt`. Seu programa deve produzir a saída `Hermione`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/12.txt`. Seu programa deve produzir a saída `Lily`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/13.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/14.txt`. Seu programa deve produzir a saída `Severus`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/15.txt`. Seu programa deve produzir a saída `Sirius`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/16.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/17.txt`. Seu programa deve produzir a saída `Harry`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/18.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/19.txt`. Seu programa deve produzir a saída `Fred`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/20.txt`. Seu programa deve produzir a saída `No match`.

Execute o comando abaixo para avaliar a correção do seu código usando o `check50`. Mas não se esqueça de compilá-lo e testá-lo sozinho também!

    check50 cs50/problems/2023/x/dna
    

Execute o comando abaixo para avaliar o estilo do seu código usando o `style50`.

    style50 dna.py
    

Como Submeter
-------------

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2023/x/dna"

