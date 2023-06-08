Speller
=======

<div class="alert" data-alert="danger" role="alert"><p><strong>Leia esta especificação inteiramente antes de começar para saber o que fazer e como fazê-lo!</strong></p></div>


Neste problema, você implementará um programa que verifica a ortografia de um arquivo, como no exemplo abaixo, usando uma tabela hash.

    $ ./speller texts/lalaland.txt
    MISSPELLED WORDS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    WORDS MISSPELLED:
    WORDS IN DICTIONARY:
    WORDS IN TEXT:
    TIME IN load:
    TIME IN check:
    TIME IN size:
    TIME IN unload:
    TIME IN TOTAL:
    

Introdução
-----------

Conecte-se ao [code.cs50.io](https://code.cs50.io/), clique na janela do seu terminal e execute o comando `cd`. Você deve ver que o prompt da sua janela de terminal se assemelha ao seguinte:

    $
    

Em seguida, execute o comando

    wget https://cdn.cs50.net/2022/fall/psets/5/speller.zip
    

para baixar um arquivo ZIP chamado de `speller.zip` em seu espaço de códigos.

Em seguida, execute o comando

    unzip speller.zip
    

para criar uma pasta chamada `speller`. Você não precisa mais do arquivo ZIP, portanto você pode executar o comando:

    rm speller.zip
    

e responda "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd speller
    

seguido de Enter para mover-se para dentro desse diretório. Seu prompt deve se parecer com o seguinte:

    speller/ $
    

Execute o comando `ls` e você verá alguns arquivos e pastas:

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
    

Se você tiver algum problema durante este processo, siga esses mesmos passos novamente e veja se consegue determinar onde errou!

Distribuição
------------

### Compreensão

Teoricamente, em uma entrada de tamanho _n_, um algoritmo com tempo de execução _n_ é "assintoticamente equivalente", em termos de _O_, a um algoritmo com tempo de execução de _2n_. Na verdade, ao descrever o tempo de execução de um algoritmo, normalmente nos concentramos no termo dominante (ou seja, mais impactante) (ou seja, _n_ neste caso, já que _n_ pode ser muito maior do que 2). No mundo real, no entanto, a verdade é que _2n_ parece duas vezes mais lento que _n_.

O desafio à sua frente é implementar o verificador ortográfico mais rápido que puder! Mas quando dizemos "o mais rápido", estamos falando de tempo "real", não assintótico.

Em `speller.c `, criamos um programa projetado para verificar a ortografia de um arquivo após carregar um dicionário de palavras do disco na memória. Esse dicionário, enquanto isso, é implementado em um arquivo chamado `dictionary.c`. (Poderia ser implementado em` speller.c`, mas à medida que os programas se tornam mais complexos, geralmente é conveniente dividi-los em vários arquivos.) Os protótipos das funções do arquivo, enquanto isso, não são definidos em `dictionary.c` em si, mas sim em `dictionary.h`. Dessa forma, tanto `speller.c` quanto `dictionary.c` podem incluir o arquivo. Infelizmente, não conseguimos implementar a parte de carregamento. Nem a parte de verificação. Ambos (e um pouco mais) deixamos com você! Mas primeiro, uma turnê.

#### `dictionary.h`

Abra o arquivo `dictionary.h` e você verá alguma nova sintaxe, incluindo algumas linhas que menciona `DICTIONARY_H`. Não se preocupe com isso, mas, se curioso, essas linhas apenas garantem que, mesmo que `dictionary.c` e `speller.c`(que você verá em um momento) incluam este arquivo, o `clang` o compilará apenas uma vez.

A seguir, observe como incluímos um arquivo chamado `stdbool.h`. Esse é o arquivo no qual `bool` é definido. Você não precisou dele antes, já que a Biblioteca CS50 o incluia para você.

Observe também nosso uso de `#define`, uma "diretiva de pré-processador" que define uma "constante" chamada `LENGTH` que tem um valor de `45`. É uma constante no sentido de que você não pode (acidentalmente) alterá-la em seu próprio código. De fato, o `clang` substituirá qualquer menção a `LENGTH` em seu próprio código por, literalmente, `45`. Em outras palavras, não é uma variável, apenas um truque de encontrar e substituir.

Finalmente, observe os protótipos de cinco funções: `check`, `hash`, `load`, `size` e `unload`. Observe como três deles recebem um ponteiro como argumento, de acordo com o `*`:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">check</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">word</span><span class="p">);</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="nf">hash</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">word</span><span class="p">);</span>
<span class="n">bool</span> <span class="nf">load</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">dictionary</span><span class="p">);</span>
</code></pre></div></div>

Lembre-se de que `char *` é o que costumávamos chamar de `string`. Portanto, esses três protótipos são essencialmente:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">check</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">word</span><span class="p">);</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="nf">hash</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">word</span><span class="p">);</span>
<span class="n">bool</span> <span class="nf">load</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">dictionary</span><span class="p">);</span>
</code></pre></div></div>

E, enquanto isso, `const` apenas diz que essas strings, quando passadas como argumentos, devem permanecer constantes; você não poderá alterá-las, acidentalmente ou não!

#### `dictionary.c`

Agora abra o arquivo `dictionary.c`. Observe como, no topo do arquivo, definimos uma `struct` chamada `node` que representa um nó em uma tabela de hash. E declaramos uma array do ponteiro global, `table`, que representará (em breve) a tabela de hash que você usará para acompanhar as palavras no dicionário. A array contém `N` ponteiros de nó, e definimos `N` como `26` por enquanto, para corresponder à função `hash` padrão, conforme descrito abaixo. Você provavelmente desejará aumentar isso, dependendo de sua própria implementação de `hash`.

Em seguida, observe que implementamos `load`, `check`, `size` e `unload`, mas apenas o suficiente para que o código compile. Observe também que implementamos a função `hash` com um algoritmo de exemplo com base na primeira letra da palavra. Seu trabalho, em última análise, é reimplementar essas funções da maneira mais inteligente possível para que este verificador de ortografia funcione conforme anunciado. E rápido!

#### `speller.c`

Ok, agora abra o arquivo `speller.c` e passe algum tempo examinando o código e os comentários nele. Você não precisará mudar nada neste arquivo, e não precisará entendê-lo na íntegra, mas tente obter uma ideia de sua funcionalidade, mesmo assim. Observe como, por meio da função chamada `getrusage`, "teremos" o "benchmark" (ou seja, cronometragem da execução de) suas implementações de `check`, `load`, `size` e `unload`. Além disso, observe como passamos o `check`, palavra por palavra, em conteúdo de algum arquivo a ser verificado ortograficamente. Por fim, relatamos cada palavra mal escrita naquele arquivo junto com muitas estatísticas.

Observe, incidentalmente, que definimos o uso do `speller` como

    Uso: speller [dicionário] texto
    

onde o `dicionário` é assumido como um arquivo contendo uma lista de palavras em minúsculas, uma por linha, e `texto` é um arquivo a ser verificado a ortografia. Como os colchetes sugerem, a provisão de um `dicionário` é opcional; se esse argumento for omitido, o `speller` usará `dictionaries/large` por padrão. Em outras palavras, executar

    ./speller texto
    

será equivalente a executar

    ./speller dictionaries/large text
    

onde `texto` é o arquivo que você deseja verificar a ortografia. Isso tudo e claro, o `speller` não poderá carregar quaisquer dicionários até você implementar `load` em `dictionary.c`! Até então, você verá `Could not load`.

Dentro do dicionário padrão, há 143.091 palavras, todas as quais devem ser carregadas na memória! De fato, dê uma olhada nesse arquivo para ter uma ideia de sua estrutura e tamanho. Observe que toda palavra nesse arquivo aparece em minúsculo (até mesmo, por simplicidade, os nomes próprios e siglas). De cima para baixo, o arquivo é classificado lexicograficamente, com apenas uma palavra por linha (cada uma das quais termina com `\n`). Nenhuma palavra tem mais de 45 caracteres, e nenhuma palavra aparece mais de uma vez. Durante o desenvolvimento, pode ser útil fornecer um `dicionário` próprio ao `speller` que contenha muito menos palavras, para que você não tenha dificuldade em depurar uma estrutura enorme na memória. Em `dictionaries/small` existe um dicionário desses. Para usá-lo, execute

    ./speller dictionaries/small text
    

onde `texto` é o arquivo que você deseja verificar a ortografia. Não prossiga até ter certeza de que entende como o `speller` funciona!

É provável que você não tenha passado tempo suficiente examinando o `speller.c`. Volte uma casa e passe por ele novamente!

#### `texts/`

Para que você possa testar sua implementação do `speller`, também fornecemos uma série de textos, entre eles, o roteiro de _La La Land_, o texto da Lei de Assistência Acessível, três milhões de bytes de Tolstoy, algumas passagens dos _Federalist Papers_ e Shakespeare e mais. Para que você saiba o que esperar, abra e examine cada um desses arquivos, que estão em um diretório chamado `texts` dentro do seu diretório `pset5`.

Agora, como você deve saber depois de ter lido o `speller.c` cuidadosamente, a saída do `speller`, se executada com, digamos,

    ./speller texts/lalaland.txt
    

irá se assemelhar eventualmente ao abaixo.

Abaixo segue alguns exemplos de palavras mal escritas que você verá. E por não querer estragar a diversão, omitimos nossas próprias estatísticas por agora.

    PALAVRAS MAL ESCRITAS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    PALAVRAS MAL ESCRITAS:
    PALAVRAS NO DICIONÁRIO:
    PALAVRAS NO TEXTO:
    TEMPO EM load:
    TEMPO EM check:
    TEMPO EM tamanho:
    TEMPO EM unload:
    TEMPO EM TOTAL:
    

`TEMPO EM load` representa o número de segundos que o `speller` passa executando sua implementação de `load`. `TEMPO EM check` representa o número de segundos que o `speller` passa, no total, executando sua implementação de `check`. `TEMPO EM tamanho` representa o número de segundos que o `speller` passa executando sua implementação de `size`. `TEMPO EM unload` representa o número de segundos que o `speller` passa executando sua implementação de `unload`. `TEMPO EM TOTAL` é a soma dessas quatro medidas.

Observe que esses tempos podem variar ligeiramente em execuções diferentes do `speller`, dependendo do que mais sua área de trabalho está fazendo, mesmo que você não altere seu código.

Aliás, para ficar claro, "mal escritas" significa apenas que alguma palavra não está no `dicionário` fornecido.

#### `Makefile`

E, por último, lembre-se de que o `make` automatiza a compilação do seu código para que você não precise executar o `clang` manualmente junto com um monte de chaves. No entanto, à medida que seus programas crescem em tamanho, o `make` não poderá inferir mais do contexto como compilar seu código; você precisará começar a dizer ao `make` como compilar seu programa, principalmente quando envolve vários arquivos de origem (ou seja, `.c`), como no caso deste problema. E então usaremos um `Makefile`, um arquivo de configuração que diz ao `make` exatamente o que fazer. Abra o `Makefile`, e você verá quatro linhas:

1.  A primeira linha diz ao `make` para executar as linhas subsequentes sempre que você mesmo executar `make speller` (ou apenas `make`).
2.  A segunda linha diz ao `make` como compilar `speller.c` em código de máquina (ou seja, `speller.o`).
3.  A terceira linha diz ao `make` como compilar `dictionary.c` em código de máquina (ou seja, `dictionary.o`).
4.  A quarta linha diz ao `make` para vincular `speller.o` e `dictionary.o` em um arquivo chamado `speller`.

**Certifique-se de compilar `speller` executando o `make speller` (ou apenas `make`). Executar `make dictionary` não funcionará!**

Especificação
-------------

Tudo bem, o desafio agora para você é implementar, em ordem, `load`, `hash`, `size`, `check` e `unload` da maneira mais eficiente possível usando uma tabela hash, de tal forma que `TIME IN load`, `TIME IN check`, `TIME IN size` e `TIME IN unload` sejam minimizados. Certamente, não é óbvio o que significa ser minimizado, já que essas referências certamente variarão à medida que você alimentar o `speller` com diferentes valores para `dictionary` e para `text`. Mas aí está o desafio, se não a diversão, desse problema. Este problema é sua chance de projetar. Embora convidemos você a minimizar o espaço, o seu inimigo final é o tempo. Mas antes de começar, algumas especificações de nossa parte.

*   Você não pode alterar `speller.c` ou `Makefile`.
*   Você pode alterar `dictionary.c` (e, de fato, deve fazê-lo para concluir as implementações de `load`, `hash`, `size`, `check` e `unload`), mas não pode alterar as declarações (ou seja, protótipos) de `load`, `hash`, `size`, `check` ou `unload`. Você pode, no entanto, adicionar novas funções e variáveis (locais ou globais) a `dictionary.c`.
*   Você pode alterar o valor de `N` em `dictionary.c`, para que sua tabela hash possa ter mais buckets.
*   Você pode alterar `dictionary.h`, mas não pode alterar as declarações de `load`, `hash`, `size`, `check` ou `unload`.
*   Sua implementação de `check` deve ser insensível a maiúsculas e minúsculas. Em outras palavras, se `foo` estiver no dicionário, então `check` deve retornar verdadeiro para qualquer capitalização do mesmo; nenhum dos `foo`, `foO`, `fOo`, `fOO`, `fOO`, `Foo`, `FoO`, `FOo` e `FOO` devem ser considerados como ignorados.
*   Com relação à capitalização, sua implementação de `check` só deve retornar `true` para as palavras que realmente estiverem no `dictionary`. Tenha cuidado para não codificar palavras comuns (por exemplo, `a`), para que não venhamos a passar para sua implementação um `dictionary` sem essas mesmas palavras. Além disso, somente os possessivos permitidos são aqueles que realmente estão no `dictionary`. Em outras palavras, mesmo que `foo` esteja no `dictionary`, `check` deve retornar `false` para `foo's` se `foo's` também não estiver no `dictionary`.
*   Você pode pressupor que qualquer `dictionary` passado para o seu programa terá a mesma estrutura que a nossa, classificada em ordem alfabética de cima para baixo com uma palavra por linha, cada uma das quais termina com `\n`. Você também pode assumir que o `dictionary` conterá pelo menos uma palavra, que nenhuma palavra terá mais de `LENGTH` (uma constante definida em `dictionary.h`) caracteres, que nenhuma palavra aparecerá mais de uma vez, que cada palavra conterá apenas caracteres alfabéticos minúsculos e possivelmente apostrofes, e que nenhuma palavra começará com um apóstrofo.
*   Você pode pressupor que o `check` só receberá palavras que contenham caracteres alfabéticos (maiúsculos ou minúsculos) e possivelmente apostrofes.
*   Seu corretor ortográfico pode somente receber `text` e, opcionalmente, `dictionary` como entrada. Embora você possa estar inclinado (particularmente se é mais experiente) a “pre-processar” nosso dicionário padrão para derivar uma “função hash ideal” para ele, você não pode salvar a saída de qualquer pré-processamento em disco com o intuito de carregá-la novamente na memória em execuções subsequentes do verificador ortográfico para ganhar uma vantagem.
*   Seu corretor ortográfico não deve vazar memória. Certifique-se de verificar vazamentos com `valgrind`.
*   **A função hash que você escreve deve ser sua, não aquela que você procura online.** Há muitas maneiras de implementar uma função hash além de usar o primeiro caractere (ou caracteres) de uma palavra. Considere uma função hash que usa a soma dos valores ASCII ou o comprimento de uma palavra. Uma boa função hash tende a reduzir as “colisões” e tem uma distribuição bastante uniforme em “buckets” da tabela hash.

Ok, prontos para começar?

*   Implemente `load`.
*   Implemente `hash`.
*   Implemente `size`.
*   Implemente `check`.
*   Implemente `unload`.

Guias
------------

Observe que há 6 vídeos na playlist abaixo.


<div class="alert" data-alert="danger" role="alert"><p>Embora o guia de Speller indique que é razoável usar uma função hash encontrada on-line, este vídeo é de uma versão anterior do problema em que permitimos isso. Conforme a especificação acima, a função hash que você escrever deve ser sua; você <strong>não pode</strong> usar uma função hash que encontrar on-line. Certifique-se de citar quaisquer fontes externas que você tenha referenciado ao escrever sua função hash.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="acelerômetro; autoplay; encrypted-media; giroscópio; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>

Dicas
-----

Para comparar duas strings ignorando as diferenças entre letras maiúsculas e minúsculas, você pode usar a função [`strcasecmp`](https://man.cs50.io/3/strcasecmp), declarada em `strings.h`! Você também deve garantir que sua função de hash não leve em consideração as diferenças entre letras maiúsculas e minúsculas, para que as palavras "foo" e "FOO" tenham o mesmo valor de hash.

Por fim, certifique-se de liberar toda memória alocada em `load` ao implementar a função `unload`! Lembre-se de que `valgrind` é seu novo melhor amigo. Saiba que `valgrind` verifica vazamentos de memória enquanto seu programa está em execução, então, certifique-se de fornecer argumentos na linha de comando caso queira que `valgrind` analise `speller` enquanto você usa um dicionário e/ou texto específico, como abaixo. É melhor usar um texto curto, senão `valgrind` pode demorar bastante para rodar.

    valgrind ./speller texts/cat.txt
    

Se você executar `valgrind` sem especificar um `texto` para `speller`, suas implementações de `load` e `unload` não serão chamadas (e, portanto, não serão analisadas).

Se não tiver certeza de como interpretar a saída do `valgrind`, basta pedir ajuda ao `help50`:

    help50 valgrind ./speller texts/cat.txt
    

Testando
--------

Como verificar se o programa está identificando as palavras incorretas? Bem, você pode consultar a chave de respostas que está no diretório `keys`, que está dentro do diretório `speller`. Por exemplo, dentro do arquivo `keys/lalaland.txt`, há todas as palavras que o seu programa _deveria_ considerar como incorretas.

Então, você pode executar seu programa em um texto em uma janela e, em outra janela, executar a solução da equipe no mesmo texto, como abaixo.

    ./speller texts/lalaland.txt
    ./speller50 texts/lalaland.txt
    

E então você pode comparar as janelas visualmente lado a lado. Porém, isso pode ficar tedioso rapidamente. Portanto, você pode querer redirecionar a saída do programa para um arquivo, como abaixo.

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt
    

Em seguida, você pode comparar ambos os arquivos lado a lado na mesma janela com um programa como `diff`, como abaixo.

    diff -y student.txt staff.txt
    

Ou então, para economizar tempo, você pode comparar a saída do seu programa (supondo que você redirecionou-a para, por exemplo, `student.txt`) com uma das chaves de resposta sem executar a solução da equipe, como abaixo.

    diff -y student.txt keys/lalaland.txt
    

Se a saída do seu programa corresponder às da equipe, o `diff` exibirá duas colunas que devem ser idênticas, exceto talvez pelos tempos de execução na parte inferior. Entretanto, se as colunas diferirem, você verá um `>` ou `|` onde elas diferem. Por exemplo, se você vir

    MISSPELLED WORDS                                                MISSPELLED WORDS
    
    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L
    

isso significa que seu programa (cuja saída está à esquerda) não considera que `Thelonious` ou `MIA` sejam palavras incorretas, mesmo que a saída da equipe (à direita) considere, como é mostrado pela ausência de, digamos, `Thelonious` na coluna da esquerda e pela presença de `Thelonious` na coluna da direita.

### `check50`

Para testar seu código de maneira menos manual (embora ainda não exaustiva), você também pode executar o comando abaixo.

    check50 cs50/problems/2023/x/speller
    

Observe que `check50` também verifica vazamentos de memória, portanto, certifique-se de que você tenha executado o `valgrind` também.

### style50

Execute o comando abaixo para avaliar o estilo de seu código usando o `style50`.

    style50 dictionary.c
    

Solução da equipe
-----------------

Como avaliar a velocidade (e a correção) do seu código? Bem, como sempre, sinta-se a vontade para brincar com a solução da equipe e comparar seus resultados, como abaixo.

    ./speller50 texts/lalaland.txt
    

Enviar
------

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/speller"

