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