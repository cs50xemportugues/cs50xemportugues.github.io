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