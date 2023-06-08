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