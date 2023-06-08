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

### Filtro de Imagens

O que significa, exatamente, filtrar uma imagem? Podemos pensar em filtrar uma imagem como pegar os pixels de uma imagem original e modificar cada pixel de tal forma que um efeito particular seja aparente na nova imagem resultante.

#### Escala de Cinza

Um filtro comum é o filtro "escala de cinza", onde queremos converter uma imagem em uma imagem preto e branco. Como isso funciona?

Lembre-se de que se os valores em vermelho, verde e azul forem todos definidos como `0x00` (hexadecimal para `0`), o pixel será preto. E se todos os valores forem definidos como `0xff` (hexadecimal para `255`), o pixel será branco. Desde que os valores em vermelho, verde e azul sejam iguais, o resultado será tons variados de cinza ao longo da escala preto-branco, com valores mais altos significando tons mais claros (mais próximos do branco) e valores mais baixos significando tons mais escuros (mais próximos do preto).

Portanto, para converter um pixel em escala de cinza, precisamos apenas garantir que os valores vermelho, verde e azul sejam iguais. Mas como saber qual valor dar a eles? Bem, provavelmente é razoável esperar que, se os valores originais em vermelho, verde e azul forem todos altos, então o novo valor também deve ser alto. E se os valores originais forem todos baixos, o novo valor também deve ser baixo.

Na verdade, para garantir que cada pixel da nova imagem ainda tenha o mesmo brilho geral ou escuridão que a velha imagem, podemos tirar uma média dos valores vermelho, verde e azul para determinar que tom de cinza dar ao novo pixel.

Se aplicarmos isso a cada pixel da imagem, o resultado será uma imagem convertida em escala de cinza.

#### Reflexão

Alguns filtros podem mover pixels. Refletir uma imagem, por exemplo, é um filtro onde a imagem resultante é o que você obteria colocando a imagem original na frente de um espelho. Portanto, quaisquer pixels no lado esquerdo da imagem devem acabar no lado direito e vice-versa.

Observe que todos os pixels originais da imagem ainda estarão presentes na imagem refletida, é apenas que esses pixels podem ter rearranjado para estar em um lugar diferente na imagem.

#### Desfoque

Existem várias maneiras de criar o efeito de desfoque ou suavidade em uma imagem. Para este problema, usaremos o "desfoque de caixa" que funciona tomando cada pixel e, para cada valor de cor, dando a ele um novo valor pela média dos valores de cores dos pixels vizinhos.

Considere a seguinte grade de pixels, onde cada pixel está numerado.

![a grid of pixels](https://cs50.harvard.edu/x/2023/psets/4/filter/more/grid.png)

O novo valor de cada pixel seria a média dos valores de todos os pixels que estão dentro de 1 linha e coluna do pixel original (formando uma caixa 3x3). Por exemplo, cada um dos valores de cor do pixel 6 seria obtido pela média dos valores de cor originais dos pixels 1, 2, 3, 5, 6, 7, 9, 10 e 11 (observe que o pixel 6 em si está incluído na média). Da mesma forma, os valores de cor do pixel 11 seriam obtidos pela média dos valores de cor dos pixels 6, 7, 8, 10, 11, 12, 14, 15 e 16.

Para um pixel na borda ou no canto, como o pixel 15, ainda procuraríamos todos os pixels dentro de 1 linha e coluna: nesse caso, os pixels 10, 11, 12, 14, 15 e 16.

#### Bordas

Em algoritmos de inteligência artificial para processamento de imagem, muitas vezes é útil detectar bordas em uma imagem: linhas na imagem que criam um limite entre um objeto e outro. Uma maneira de alcançar esse efeito é aplicando o operador [Sobel](https://en.wikipedia.org/wiki/Sobel_operator) à imagem.

Assim como no desfoque de imagem, a detecção de bordas funciona tomando cada pixel e modificando-o com base na grade 3x3 de pixels que o rodeia. Mas em vez de apenas tirar a média dos nove pixels, o operador Sobel calcula o novo valor de cada pixel, fazendo uma soma ponderada dos valores dos pixels circundantes. E como as bordas entre objetos podem ocorrer em direções tanto vertical quanto horizontal, na verdade, você calculará duas somas ponderadas: uma para detectar bordas na direção x e outra para detectar bordas na direção y. Em particular, você usará os seguintes dois "kernels":

![Sobel kernels](https://cs50.harvard.edu/x/2023/psets/4/filter/more/sobel.png)

Como interpretar esses kernels? Resumidamente, para cada um dos três valores de cor para cada pixel, calcularemos duas valores `Gx` e `Gy`. Para calcular `Gx` para o valor do canal vermelho de um pixel, por exemplo, pegaremos os valores vermelhos originais dos nove pixels que formam uma caixa 3x3 ao redor do pixel, multiplicaremos cada um deles pelo valor correspondente no kernel `Gx` e levaremos a soma dos valores resultantes.

Por que esses valores particulares para o kernel? Na direção `Gx`, por exemplo, estamos multiplicando os pixels à direita do pixel alvo por um número positivo e os pixels à esquerda do pixel alvo por um número negativo. Quando tiramos a soma, se os pixels à direita forem de uma cor semelhante aos pixels à esquerda, o resultado será próximo de 0 (os números se cancelam).Mas se os pixels à direita forem muito diferentes dos pixels à esquerda, o valor resultante será muito positivo ou muito negativo, indicando uma mudança na cor que provavelmente é o resultado de um limite entre objetos. E um argumento semelhante é válido para calcular bordas na direção `y`.

Usando esses kernels, podemos gerar um valor `Gx` e `Gy` para cada um dos canais de vermelho, verde e azul para um pixel. Mas cada canal só pode ter um valor, não dois: portanto, precisamos de alguma maneira de combinar `Gx` e `Gy` em um único valor. O algoritmo do filtro Sobel combina `Gx` e `Gy` em um valor final calculando a raiz quadrada de `Gx^2 + Gy^2`. E como os valores do canal só podem ter valores inteiros de 0 a 255, certifique-se de que o valor resultante seja arredondado para o inteiro mais próximo e limitado a 255!

E quanto ao tratamento de pixels na borda ou no canto da imagem? Existem muitas maneiras de lidar com pixels na borda, mas, para os fins deste problema, pediremos que você trate a imagem como se houvesse uma borda preta sólida de 1 pixel ao redor da borda da imagem: portanto, tentar acessar um pixel além da borda da imagem deve ser tratado como um pixel preto sólido (valores de 0 para cada vermelho, verde e azul). Isso efetivamente ignorará esses pixels de nossos cálculos de `Gx` e `Gy`.

Começando
---------------

Faça login em [code.cs50.io] (https://code.cs50.io/), clique na sua janela do terminal e execute o comando `cd` . Você deve perceber que o prompt da sua janela do terminal se parece com o abaixo:

     $
     
Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-more.zip
    
para baixar um arquivo ZIP chamado `filter-more.zip` em seu espaço de códigos.

Em seguida, execute

    unzip filter-more.zip
    
para criar uma pasta chamada `filter-more`. Você não precisa mais do arquivo ZIP, portanto, execute

    rm filter-more.zip
    
e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd filter-more
    
seguido de Enter para se mover para ("abrir") esse diretório. Seu prompt agora deve se parecer com o abaixo.

    filter-more/ $
    
Execute `ls` isoladamente e você deve ver alguns arquivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` e `Makefile`. Você também deve ver uma pasta chamada `images` com quatro arquivos BMP. Se você tiver algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde ocorreu o erro!

Compreensão
-------------

Agora vamos dar uma olhada em alguns dos arquivos fornecidos para você como código de distribuição para entender o que há dentro deles.

### `bmp.h`

Abra `bmp.h` (clicando duas vezes nele no navegador de arquivos) e dê uma olhada.

Você verá definições dos cabeçalhos que mencionamos (`BITMAPINFOHEADER` e `BITMAPFILEHEADER`). Além disso, esse arquivo define `BYTE`, `DWORD`, `LONG` e `WORD`, tipos de dados normalmente encontrados no mundo da programação do Windows. Observe como eles são apenas aliases para primitivos com os quais você está (esperançosamente) familiarizado. Parece que `BITMAPFILEHEADER` e `BITMAPINFOHEADER` usam esses tipos.

Talvez o mais importante para você, este arquivo também define um `struct` chamado `RGBTRIPLE` que, simplesmente, "encapsula" três bytes: um azul, um verde e um vermelho (a ordem, lembre-se, na qual esperamos encontrar triples RGB no disco).

Por que essas `struct`s são úteis? Bem, lembre-se de que um arquivo é apenas uma sequência de bytes (ou, em última análise, bits) no disco. Mas esses bytes geralmente estão ordenados de tal forma que os primeiros representam algo, os próximos representam outra coisa e assim por diante. Existem "formatos de arquivo" porque o mundo padronizou o que os bytes significam. Agora, poderíamos simplesmente ler um arquivo do disco para a RAM como um grande array de bytes. E poderíamos simplesmente lembrar que o byte em `array[i]` representa uma coisa, enquanto o byte em `array[j]` representa outra. Mas por que não dar nomes a alguns desses bytes para que possamos recuperá-los da memória com mais facilidade? É precisamente isso que as `struct`s em `bmp.h` nos permitem fazer. Em vez de pensar em algum arquivo como uma longa sequência de bytes, podemos pensar nele como uma sequência de `struct`s.

### `filter.c`

Agora, vamos abrir `filter.c`. Este arquivo já foi escrito para você, mas há alguns pontos importantes que vale a pena observar aqui.

Em primeiro lugar, observe a definição de `filters` na linha 10. Essa string informa ao programa quais são os argumentos permitidos na linha de comando do programa: `b`, `e`, `g` e `r`. Cada um deles especifica um filtro diferente que podemos aplicar às nossas imagens: desfoque, detecção de borda, escala de cinza e reflexão.

As próximas várias linhas abrem um arquivo de imagem, certificam-se de que é de fato um arquivo BMP e leem todas as informações de pixel em uma matriz 2D chamada `image`.

Role para baixo até a instrução `switch` que começa na linha 101. Observe que, dependendo do `filter` que escolhemos, uma função diferente é chamada: se o usuário escolher o filtro `b`, o programa chama a função `blur`; se `e`, então `edges` é chamada; se `g`, então `grayscale` é chamada; e se `r`, então `reflect` é chamada. Observe também que cada uma dessas funções recebe como argumentos a altura da imagem, a largura da imagem e a matriz 2D de pixels.

Essas são as funções que você implementará em breve. Como você pode imaginar, o objetivo é que cada uma dessas funções edite a matriz 2D de pixels de tal forma que o filtro desejado seja aplicado à imagem.

As últimas linhas do programa levam a imagem resultante e a gravam em um novo arquivo de imagem.

### `helpers.h`

A seguir, dê uma olhada em `helpers.h`. Este arquivo é bastante curto e fornece apenas os protótipos de função para as funções que você viu anteriormente.

Observe aqui que cada função recebe como argumento uma matriz 2D chamada `image`, onde `image` é um array com muitas linhas `height`, e cada linha é, por si só, outro array de `width` `RGBTRIPLE`s. Então, se `image` representa a imagem completa, então `image[0]` representa a primeira linha e `image[0][0]` representa o pixel no canto superior esquerdo da imagem.

### `helpers.c`

Agora, abra `helpers.c`. É aqui que a implementação das funções declaradas em `helpers.h` devem estar. Mas observe que, no momento, as implementações estão faltando! Essa parte depende de você.

### `Makefile`

Por fim, vamos dar uma olhada em `Makefile`. Este arquivo especifica o que deve acontecer quando executamos um comando no terminal como `make filter`. Enquanto programas que você pode ter escrito antes estavam confinados a apenas um arquivo, `filter` parece usar vários arquivos: `filter.c` e `helpers.c`. Portanto, precisamos dizer ao `make` como compilar este arquivo.

Tente compilar `filter` por si mesmo indo para o terminal e executando

    $ make filter
    

Em seguida, você pode executar o programa digitando:

    $ ./filter -g images/yard.bmp out.bmp
    

que pega a imagem em `images/yard.bmp` e gera uma nova imagem chamada `out.bmp` depois de passar os pixels pela função `grayscale`. No entanto, `grayscale` ainda não faz nada, então a imagem de saída deve ficar igual à imagem original do quintal.

Especificação
-------------

Implemente as funções em `helpers.c` para que um usuário possa aplicar filtros de escala de cinza, reflexão, desfoque ou detecção de borda em suas imagens.

*   A função `grayscale` deve pegar uma imagem e transformá-la em uma versão em preto e branco da mesma imagem.
*   A função `reflect` deve pegar uma imagem e refleti-la horizontalmente.
*   A função `blur` deve pegar uma imagem e transformá-la em uma versão desfocada da mesma imagem.
*   A função `edges` deve pegar uma imagem e destacar as bordas entre objetos, de acordo com o operador Sobel.

Você não deve modificar nenhuma das assinaturas de função, nem deve modificar nenhum outro arquivo além de `helpers.c`.

Walkthrough
-----------

**Observe que há 5 vídeos nesta lista de reprodução.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/vsOsctDernw?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382OwvMbZuaMGtD9wZkhnhYj"></iframe></div>

Uso
---

Seu programa deve se comportar como nos exemplos abaixo. `INFILE.bmp` é o nome da imagem de entrada e `OUTFILE.bmp` é o nome da imagem resultante após a aplicação de um filtro.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -e INFILE.bmp OUTFILE.bmp
```

Dicas
---

*   Os valores dos componentes `rgbtRed`, `rgbtGreen` e `rgbtBlue` de um pixel são todos números inteiros. Certifique-se de arredondar quaisquer números de ponto flutuante para o inteiro mais próximo ao atribuí-los a um valor de pixel!

Testando
--------

Certifique-se de testar todos os seus filtros nos arquivos de bitmap de amostra fornecidos!

Execute o comando abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo também!

    check50 cs50/problems/2023/x/filter/more
    

Execute o comando abaixo para avaliar o estilo do seu código usando `style50`.

    style50 helpers.c
    

Como Enviar
-----------

No terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/filter/more

