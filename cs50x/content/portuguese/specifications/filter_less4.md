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