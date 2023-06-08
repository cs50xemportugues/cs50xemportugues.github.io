Filtro
======

Implemente um programa que aplica filtros a imagens BMPs, como abaixo.

    $ ./filter -r IMAGE.bmp REFLECTED.bmp
    

onde `IMAGE.bmp` é o nome do arquivo de imagem e `REFLECTED.bmp` é o nome dado a um arquivo de imagem de saída, agora refletida.

Contexto
---------

### Bitmaps

A maneira mais simples de representar uma imagem é com uma grade de pixels (ou seja, pontos), cada um dos quais pode ter uma cor diferente. Para imagens em preto e branco, portanto, precisamos de 1 bit por pixel, onde 0 pode representar preto e 1 pode representar branco, como abaixo.

![uma imagem simples em bitmap](https://cs50.harvard.edu/x/2023/psets/4/filter/less/bitmap.png)

Nesse sentido, então, uma imagem é apenas um bitmap (ou seja, um mapa de bits). Para imagens mais coloridas, basta usar mais bits por pixel. Um formato de arquivo (como [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG) ou [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)), que suporta “cores de 24 bits” usa 24 bits por pixel. (BMP suporta 1, 4, 8, 16, 24 e 32 bits de cor.)

Um BMP de 24 bits usa 8 bits para significar a quantidade de vermelho na cor de um pixel, 8 bits para significar a quantidade de verde na cor de um pixel e 8 bits para significar a quantidade de azul na cor de um pixel. Se você já ouviu falar de cor RGB, bem, aí está: vermelho, verde, azul.

Se os valores R, G e B de algum pixel em um BMP forem, digamos, `0xff`, `0x00` e `0x00` em hexadecimal, esse pixel é puramente vermelho, já que `0xff` (também conhecido como `255` em decimal) implica “muito vermelho”, enquanto `0x00` e `0x00` implicam “nenhum verde” e “nenhum azul”, respectivamente.

### Um Pouco Mais Técnico Sobre Bitmaps

Lembre-se de que um arquivo é apenas uma sequência de bits, organizados de alguma forma. Um arquivo BMP de 24 bits é, então, essencialmente apenas uma sequência de bits, (quase) cada 24 dos quais representam a cor de um pixel. Mas um arquivo BMP também contém alguns “metadados”, informações como a altura e largura de uma imagem. Esses metadados são armazenados no início do arquivo na forma de duas estruturas de dados geralmente referenciadas como “cabeçalhos”, para não ser confundido com os arquivos de cabeçalho em C. (Aliás, esses cabeçalhos evoluíram ao longo do tempo. Esse problema usa a versão mais recente do formato BMP da Microsoft, 4.0, que estreou com o Windows 95).

O primeiro desses cabeçalhos, chamado `BITMAPFILEHEADER`, tem 14 bytes de comprimento. (Lembre-se de que 1 byte equivale a 8 bits.) O segundo desses cabeçalhos, chamado `BITMAPINFOHEADER`, tem 40 bytes de comprimento. Logo após esses cabeçalhos está o bitmap real: uma matriz de bytes, triplos de cada um representando a cor de um pixel. No entanto, o BMP armazena esses triplos ao contrário (ou seja, como BGR), com 8 bits para azul, seguidos por 8 bits para verde, seguidos por 8 bits para vermelho. (Alguns BMPs também armazenam todo o bitmap ao contrário, com a linha superior da imagem no final do arquivo BMP. Mas armazenamos os BMPs deste conjunto de problemas como aqui descrito, com a linha superior de cada bitmap primeiro e a linha inferior por último.) Em outras palavras, se convertêssemos o smiley de 1 bit acima em um smiley de 24 bits, substituindo vermelho por preto, um BMP de 24 bits armazenaria este bitmap da seguinte forma, onde `0000ff` significa vermelho e` ffffff` significa branco; destacamos em vermelho todas as instâncias de `0000ff`.

![um sorriso vermelho](https://cs50.harvard.edu/x/2023/psets/4/filter/less/red_smile.png)

Porque apresentamos esses bits da esquerda para a direita, de cima para baixo, em 8 colunas, você realmente pode ver o smiley vermelho se você recuar um passo.

Para ser claro, lembre-se de que um dígito hexadecimal representa 4 bits. Assim, `ffffff` em hexadecimal, na verdade, significa `111111111111111111111111` em binário.

Observe que você pode representar um bitmap como uma matriz 2D de pixels: onde a imagem é uma matriz de linhas, cada linha é uma matriz de pixels. De fato, é assim que escolhemos representar imagens bitmap neste problema.

### Filtragem de Imagem

O que significa filtrar uma imagem? Você pode pensar na filtragem de uma imagem como pegar os pixels de uma imagem original e modificar cada pixel de tal forma que um efeito particular seja aparente na imagem resultante.

#### Escala de cinza

Um filtro comum é o filtro de “tons de cinza”, em que levamos uma imagem e queremos convertê-la em preto-e-branco. Como isso funciona?

Lembre-se de que, se os valores vermelho, verde e azul forem todos definidos como `0x00` (hexadecimal para `0`), o pixel é preto. E se todos os valores forem definidos como `0xff` (hexadecimal para `255`), o pixel é branco. Desde que os valores vermelho, verde e azul sejam iguais, o resultado será variados tons de cinza ao longo do espectro preto-branco, com valores mais altos significando tons mais claros (mais próximo do branco) e valores mais baixos significando tons mais escuros (mais próximo do preto).

Então, para converter um pixel em escala de cinza, precisamos apenas garantir que os valores vermelho, verde e azul sejam do mesmo valor. Mas como sabemos qual valor torná-los iguais? Bem, provavelmente é razoável esperar que se os valores originais de vermelho, verde e azul fossem todos bastante altos, o novo valor também devesse ser bastante alto. E se os valores originais fossem todos baixos, então o novo valor deveria ser baixo também.

De fato, para garantir que cada pixel da nova imagem tenha a mesma brilho ou escuridão geral que a imagem antiga, podemos tirar a média dos valores de vermelho, verde e azul para determinar qual tom de cinza fazer o novo pixel. Se você aplicar isso a cada pixel da imagem, o resultado será uma imagem convertida em escala de cinza.

#### Sépia

A maioria dos programas de edição de imagens suportam o filtro "sépia", que dá às imagens uma aparência antiga, tornando toda a imagem um pouco avermelhada e marrom.

Uma imagem pode ser convertida em sépia pegando cada pixel e computando os novos valores de vermelho, verde e azul com base nos valores originais dos três.

Existem vários algoritmos para converter uma imagem em sépia, mas para este problema, pedimos que você use o seguinte algoritmo. Para cada pixel, os valores de cor sépia devem ser calculados com base nos valores de cor originais conforme abaixo.

      sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
      sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
      sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
    

Claro, o resultado de cada uma dessas fórmulas pode não ser um número inteiro, mas cada valor pode ser arredondado para o inteiro mais próximo. Também é possível que o resultado da fórmula seja um número maior que 255, o valor máximo para um valor de cor de 8 bits. Nesse caso, os valores de vermelho, verde e azul devem ser limitados a 255. Como resultado, podemos garantir que os valores de vermelho, verde e azul resultantes serão números inteiros entre 0 e 255, inclusive.

#### Reflexão

Alguns filtros também podem mover pixels. Refletir uma imagem, por exemplo, é um filtro onde a imagem resultante é o que você obteria colocando a imagem original na frente de um espelho. Então, quaisquer pixels no lado esquerdo da imagem devem acabar no lado direito, e vice-versa.

Observe que todos os pixels originais da imagem original ainda estarão presentes na imagem refletida, apenas que esses pixels podem ter sido rearranjados para estar em um lugar diferente na imagem.

#### Desfoque

Existem várias maneiras de criar o efeito de desfocar ou suavizar uma imagem. Para este problema, usaremos o "desfoque de caixa", que funciona pegando cada pixel e, para cada valor de cor, dando-lhe um novo valor fazendo a média dos valores de cor dos pixels vizinhos.

Considere a seguinte grade de pixels, onde cada pixel foi numerado.

![uma grade de pixels](https://cs50.harvard.edu/x/2023/psets/4/filter/less/grid.png)

O novo valor de cada pixel seria a média dos valores de todos os pixels que estão a uma coluna e uma linha do pixel original (formando uma caixa de 3x3). Por exemplo, cada um dos valores de cor para o pixel 6 seria obtido calculando a média dos valores de cor originais dos pixels 1, 2, 3, 5, 6, 7, 9, 10 e 11 (note que o pixel 6 em si está incluído na média). Da mesma forma, os valores de cor para o pixel 11 seriam obtidos calculando a média dos valores de cor dos pixels 6, 7, 8, 10, 11, 12, 14, 15 e 16.

Para um pixel ao longo da borda ou canto, como o pixel 15, ainda procuraríamos por todos os pixels a uma coluna e linha: neste caso, pixels 10, 11, 12, 14, 15 e 16.

Começando
---------------

Acesse [code.cs50.io](https://code.cs50.io/), clique na janela do terminal e execute `cd` sozinho. Você deve encontrar que o prompt da janela do terminal se parece com o seguinte:

    $
    
Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-less.zip
    
para baixar um ZIP chamado `filter-less.zip` em seu espaço de códigos.

Depois execute

    unzip filter-less.zip
    
para criar uma pasta chamada `filter-less`. Você não precisa mais do arquivo ZIP, então execute

    rm filter-less.zip
    
e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd filter-less
    
seguido de Enter para mover-se para (ou seja, abrir) o diretório. Seu prompt agora deve se parecer com o seguinte:

    filter-less/ $
    
Execute `ls` sozinho e você deve ver alguns arquivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` e `Makefile`. Você também deve ver uma pasta chamada `images` com quatro arquivos BMP. Se você tiver algum problema, siga os mesmos passos novamente e veja se você pode determinar onde errou!

Entendendo
-------------

Vamos dar uma olhada em alguns dos arquivos fornecidos como código de distribuição para entender o que há dentro deles.

### `bmp.h`

Abra `bmp.h`(dando duplo clique no arquivo no navegador de arquivos) e dê uma olhada.

Você verá definições dos cabeçalhos que mencionamos (`BITMAPINFOHEADER` e `BITMAPFILERHEADER`). Além disso, esse arquivo define `BYTE`, `DWORD`, `LONG` e `WORD`, que são tipos de dados normalmente encontrados no mundo da programação Windows. Observe como eles são apenas aliases de primitivos com os quais você provavelmente já está familiarizado. Parece que `BITMAPFILERHEADER` e `BITMAPINFOHEADER` usam esses tipos.

Talvez o mais importante para você, esse arquivo também define uma `struct` chamada `RGBTRIPLE` que, simplesmente, "encapsula" três bytes: um azul, um verde e um vermelho (a ordem, lembre-se, em que esperamos encontrar triplos RGB realmente em disco).

Por que essas `struct` são úteis? Bem, lembre-se de que um arquivo é apenas uma sequência de bytes (ou, em última análise, bits) em disco. Mas esses bytes geralmente são ordenados de tal forma que os primeiros representam algo, os próximos representam outra coisa e assim por diante. "Formatos de arquivo" existem porque o mundo padronizou quais bytes significam o quê. Agora, poderíamos simplesmente ler um arquivo do disco na RAM como uma grande matriz de bytes. E poderíamos apenas nos lembrar de que o byte em `array[i]` representa uma coisa, enquanto o byte em `array[j]` representa outra. Mas por que não dar alguns desses bytes nomes para que possamos recuperá-los da memória mais facilmente? É precisamente isso que as `struct` em `bmp.h` nos permitem fazer. Em vez de pensar em algum arquivo como uma longa sequência de bytes, podemos pensar nele como uma sequência de `struct`.

### `filter.c`

Agora, vamos abrir `filter.c`. Este arquivo já foi escrito para você, mas há alguns pontos importantes que vale a pena mencionar aqui.

Em primeiro lugar, observe a definição de `filters` na linha 10. Essa string informa ao programa quais são os argumentos da linha de comando permitidos para o programa: `b`, `g`, `r` e `s`. Cada um deles especifica um filtro diferente que podemos aplicar às nossas imagens: borrão, escala de cinza, reflexão e sépia.

As próximas linhas abrem um arquivo de imagem, garantem que é realmente um arquivo BMP e lêem todas as informações de pixel em uma matriz 2D chamada `image`.

Role até a instrução `switch` que começa na linha 101. Observe que, dependendo do filtro que escolhemos, uma função diferente é chamada: se o usuário escolher o filtro `b`, o programa chama a função `blur`; se `g`, é chamado `grayscale`; se `r`, `reflect` é chamado; e se `s`, é chamado `sepia`. Observe também que cada uma dessas funções recebe como argumentos a altura da imagem, a largura da imagem e a matriz 2D de pixels.

Essas são as funções que você implementará em breve. Como você pode imaginar, o objetivo é para que cada uma dessas funções edite a matriz 2D de pixels de tal maneira que o filtro desejado seja aplicado à imagem.

As linhas restantes do programa pegam a `image`resultante e a escrevem em um novo arquivo de imagem.

### `helpers.h`

Agora, dê uma olhada em `helpers.h`. Este arquivo é bastante curto e fornece apenas os protótipos de função das funções que você viu anteriormente.

Aqui, observe o fato de que cada função recebe uma matriz 2D chamada `image`como argumento, onde `image` é uma matriz de `height` linhas e cada linha é ela própria outra matriz de `width` `RGBTRIPLE`s. Portanto, se `image` representa a imagem inteira, `image[0]` representa a primeira linha e `image[0][0]` representa o pixel no canto superior esquerdo da imagem.

### `helpers.c`

Agora, abra `helpers.c`. Aqui está a implementação das funções declaradas em `helpers.h`. Mas observe que, no momento, as implementações estão faltando! Esta parte é com você.

### `Makefile`

Por fim, vamos dar uma olhada em `Makefile`. Este arquivo especifica o que deve acontecer quando executamos um comando de terminal como `make filter`. Enquanto programas que você pode ter escrito anteriormente estavam confinados a apenas um arquivo,`filter` parece usar vários arquivos: `filter.c` e `helpers.c`. Portanto, precisamos dizer ao `make` como compilar este arquivo.

Tente compilar `filter` por si mesmo indo para o terminal e executando

      $ make filter

Em seguida, você pode executar o programa executando:

      $ ./filter -g images/yard.bmp out.bmp

o qual pega a imagem em `images/yard.bmp` e gera uma nova imagem chamada `out.bmp` depois de executar os pixels pela função `grayscale`. No entanto, `grayscale` ainda não faz nada, então a imagem de saída deve ser igual à imagem original.

Especificação
-------------

Implemente as funções em `helpers.c` para permitir que o usuário aplique filtros de escala de cinza, sépia, reflexão ou desfoque em suas imagens.

* A função `grayscale` deve levar uma imagem e transformá-la em uma versão preto e branco da mesma imagem.
* A função `sepia` deve levar uma imagem e transformá-la em uma versão sépia da mesma imagem.
* A função `reflect` deve levar uma imagem e refleti-la horizontalmente.
* Finalmente, a função `blur` deve levar uma imagem e transformá-la em uma versão desfocada da mesma imagem.

Você não deve modificar nenhuma das assinaturas das funções, nem deve modificar nenhum outro arquivo além de `helpers.c`.

Passo a Passo
-----------

** Observe que há 5 vídeos nesta lista de reprodução. **

<div class="ratio ratio-16x9" data-video = ""><iframe allow = "acelerômetro; autoplay; encrypted-media; giroscópio; picture-in-picture" allowfullscreen = "" class = "border" data-video = "" src = "https://www.youtube.com/embed/K0v9byp9jd0?modestbranding =0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut"></iframe></div>


Uso
-----

Seu programa deve ser executado conforme os exemplos abaixo. `INFILE.bmp` é o nome da imagem de entrada e `OUTFILE.bmp` é o nome da imagem resultante após a aplicação de um filtro.

```
$ ./filter - g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter - s INFILE.bmp OUTFILE.bmp
```
```
$ ./filter - r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter - b INFILE.bmp OUTFILE.bmp
```

Sugestões
-----

* Os valores das componentes `rgbtRed`, `rgbtGreen` e `rgbtBlue` de um pixel são todos inteiros, portanto, certifique-se de arredondar quaisquer números de ponto flutuante para o inteiro mais próximo ao atribuí-los a um valor de pixel!
* Ao implementar a função `grayscale`, você precisará calcular a média dos valores de 3 inteiros. Por que você deve dividir a soma desses inteiros por 3,0 e não por 3?
* Na função `reflect`, você precisará trocar os valores dos pixels em lados opostos de uma linha. Lembre-se da aula de como implementamos a troca de dois valores com uma variável temporária. Não é necessário usar uma função separada para troca, a menos que você queira!
* Como uma função que retorna o menor dos dois inteiros pode ser útil ao implementar `sepia`, especialmente quando você precisa garantir que o valor de uma cor não seja superior a 255?
* Ao implementar a função `blur`, você pode descobrir que o desfoque de um pixel acaba afetando o desfoque de outro pixel. Talvez seja melhor criar uma cópia da `image` (terceiro argumento da função) declarando uma nova matriz (bidimensional) com o código como `RGBTRIPLE copy [height] [width];` e copiando `image` em` copy`, pixel por pixel, com loops `for` aninhados? E, em seguida, leia as cores dos pixels de` copy`, mas escreva (ou seja, altere) as cores dos pixels em` image`?

Testando
-------

Certifique-se de testar todos os seus filtros nos arquivos de bitmap de amostra fornecidos!

Execute o abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilar e testá-lo você mesmo também!

```
check50 cs50/problems/2023/x/filter/less
```

Execute o abaixo para avaliar o estilo do seu código usando `style50`.

```
style50 helpers.c
```

Como Enviar
-------------

No seu terminal, execute o abaixo para enviar o seu trabalho.

```
submit50 cs50/problems/2023/x/filter/less
```

