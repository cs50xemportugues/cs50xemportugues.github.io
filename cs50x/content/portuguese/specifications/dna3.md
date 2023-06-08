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