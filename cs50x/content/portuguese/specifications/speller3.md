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