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