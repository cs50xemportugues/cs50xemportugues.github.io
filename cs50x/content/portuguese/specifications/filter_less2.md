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