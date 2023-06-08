Filtro
======

Implemente um programa que aplique filtros a arquivos BMP conforme abaixo.

    $ ./filter -r IMAGEM.bmp REFLETIDA.bmp
    

onde `IMAGEM.bmp` é o nome do arquivo de imagem e `REFLETIDA.bmp` é o nome atribuído a um arquivo de imagem de saída, agora refletida.

Contexto
----------

### Bitmaps

A maneira mais simples de representar uma imagem é com uma grade de pixels (ou pontos), cada um dos quais pode ter uma cor diferente. Para imagens em preto e branco, portanto, precisamos de 1 bit por pixel, já que 0 pode representar preto e 1 pode representar branco, como o exemplo abaixo.

![um bitmap simples](https://cs50.harvard.edu/x/2023/psets/4/filter/more/bitmap.png)

Nesse sentido, então, uma imagem é apenas um bitmap (ou seja, um mapa de bits). Para imagens mais coloridas, você simplesmente precisa de mais bits por pixel. Um formato de arquivo (como [BMP](https://pt.wikipedia.org/wiki/BMP), [JPEG](https://pt.wikipedia.org/wiki/JPEG) ou [PNG](https://pt.wikipedia.org/wiki/PNG)) que suporte "cor de 24 bits" usa 24 bits por pixel (o BMP realmente suporta cores de 1, 4, 8, 16, 24 e 32 bits).

Um BMP de 24 bits usa 8 bits para indicar a quantidade de vermelho na cor de um pixel, 8 bits para indicar a quantidade de verde na cor de um pixel e 8 bits para indicar a quantidade de azul na cor de um pixel. Se os valores R, G e B de algum pixel em um BMP forem, digamos, `0xff`, `0x00` e `0x00` em hexadecimal, esse pixel é puramente vermelho, pois `0xff` (também conhecido como `255` em decimal) implica "muito vermelho", enquanto `0x00` e `0x00` implicam "nenhum verde" e "nenhum azul", respectivamente.

### Um pouco mais técnico

Lembre-se de que um arquivo é apenas uma sequência de bits, organizados de alguma maneira. Um arquivo BMP de 24 bits, então, é basicamente apenas uma sequência de bits, (quase) todos os quais representam a cor de um pixel. Mas um arquivo BMP também contém alguns "metadados", informações como a altura e a largura de uma imagem. Esses metadados são armazenados no início do arquivo na forma de duas estruturas de dados geralmente referidas como "cabeçalhos", para não serem confundidas com os arquivos de cabeçalho C. (Aliás, esses cabeçalhos evoluíram ao longo do tempo. Este problema usa a versão mais recente do formato BMP da Microsoft, 4.0, que estreou com o Windows 95.)

O primeiro desses cabeçalhos, chamado `BITMAPFILEHEADER`, tem 14 bytes de comprimento. (Lembre-se de que 1 byte equivale a 8 bits.) O segundo desses cabeçalhos, chamado `BITMAPINFOHEADER`, tem 40 bytes de comprimento. Logo após esses cabeçalhos vem o bitmap real: uma matriz de bytes, trios dos quais representam a cor de um pixel. No entanto, o BMP armazena esses trios ao contrário (ou seja, como BGR), com 8 bits para azul, seguidos de 8 bits para verde, seguidos de 8 bits para vermelho. (Alguns BMPs também armazenam todo o bitmap ao contrário, com a linha superior da imagem no final do arquivo BMP. Mas armazenamos os BMPs deste conjunto de problemas conforme descrito aqui, com a primeira linha superior de cada bitmap e a última linha inferior.) Em outras palavras, se convertermos o smiley de 1 bit acima para um smiley de 24 bits, substituindo o preto por vermelho, um BMP de 24 bits armazenaria este bitmap da seguinte forma, onde `0000ff` significa vermelho e `ffffff` significa branco. Destacamos em vermelho todas as instâncias de `0000ff`.

![sorriso vermelho](https://cs50.harvard.edu/x/2023/psets/4/filter/more/red_smile.png)

Como apresentamos esses bits da esquerda para a direita, de cima para baixo, em 8 colunas, você pode realmente ver o sorriso vermelho se der um passo para trás.

Para ficar claro, lembre-se de que um dígito hexadecimal representa 4 bits. Por conseguinte, `ffffff` em hexadecimal realmente significa `111111111111111111111111` em binário.

Observe que você pode representar um bitmap como uma matriz tridimensional de pixels: onde a imagem é uma matriz de linhas, cada linha é uma matriz de pixels. De fato, é assim que escolhemos representar imagens bitmap neste problema.