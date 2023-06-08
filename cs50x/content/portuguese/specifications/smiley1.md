Laboratório 4: Smiley
=============

Objetivos de aprendizagem
--------------

* Aprender como trabalhar com imagens.
* Praticar a manipulação de pixels.

Contexto
----------

![Smiley](https://cs50.harvard.edu/x/2023/labs/4/smiley/smiley_spec_image.png)

Na aula, você viu um pouco sobre como as imagens são armazenadas em um computador. Neste laboratório, você vai praticar o trabalho com um arquivo BMP, na verdade, a imagem de uma cara sorridente que está representada aqui e mudar todos os pixels pretos para uma cor de sua escolha.

No entanto, a cara sorridente com a qual você estará trabalhando não é composta apenas de 0 e 1, ou seja, pixels em preto e branco, mas consiste em 24 bits por pixels. Ela usa oito bits para representar os valores de vermelho, oito bits para verde e oito bits para azul. Como cada cor utiliza oito bits ou um byte, podemos utilizar um número no intervalo de 0 a 255 para representar o valor de sua cor. Em hexadecimal, isto é representado por `0x00` a `0xff`. Misturando esses valores de vermelho, verde e azul, podemos criar milhões de cores possíveis.

Se você olhar para `bmp.h`, um dos arquivos auxiliares no código de distribuição, você verá como cada `TRIPLO RGB` é representado por uma `estrutura` como:

    typedef struct
    {
        BYTE rgbtBlue;
        BYTE rgbtGreen;
        BYTE rgbtRed;
    }
    RGBTRIPLE;
    

onde `BYTE` é definido como um inteiro de 8 bits.

Você notará que vários arquivos são fornecidos no código de distribuição para lidar com a leitura e escrita de um arquivo de imagem, bem como para lidar com os metadados ou "cabeçalhos" da imagem. Você estará completando a função `colorize` em `helpers.c`, que já tem como parâmetros de entrada a altura da imagem, largura e uma matriz bidimensional de `TRIPLO RGB` que criam a própria imagem.

* Dicas
    * Se salvássemos o primeiro pixel como `TRIPLO RGB pixel = imagem[0][0]`, poderíamos acessar cada uma das cores individuais de `pixel` como `pixel.rgbtBlue`, `pixel.rgbtGreen`, e `pixel.rgbtRed`.

Demonstração
----

Como começar
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da sua janela do terminal e execute `cd` sozinho. Você deve perceber que seu "prompt" se assemelha ao abaixo.

    $
    

Clique dentro dessa janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/labs/4/smiley.zip
    

seguido de Enter para baixar um ZIP chamado `smiley.zip` em seu espaço de códigos. Não deixe de observar o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere!

Agora execute

    unzip smiley.zip
    

para criar uma pasta chamada `smiley`. Você não precisa mais do arquivo ZIP, então execute

    rm smiley.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd smiley
    

seguido de Enter para mover-se para dentro (i.e., abrir) esse diretório. Seu prompt deve agora se assemelhar ao seguinte.

    smiley/ $
    

Se tudo ocorreu bem, você deve executar

    ls
    

e deverá ver `bmp.h`, `colorize.c`, `helpers.c`, `helpers.h`, `Makefile`, e `smiley.bmp`.

Se você encontrar qualquer problema, siga essas mesmas etapas novamente e veja se você consegue determinar onde errou!

Detalhes de implementação
----------------------

Abra o `helpers.c` e note que a função `colorize` está incompleta. Observe que a altura da imagem, largura e a matriz bidimensional de pixels é configurada como os parâmetros de entrada para essa função. Você deve implementar esta função para alterar todos os pixels pretos na imagem para uma cor escolhida por você.

Você pode compilar o seu código simplesmente digitando `make` no prompt `$`.

Em seguida, execute o programa digitando:

    ./colorize smiley.bmp outfile.bmp
    

onde `outfile.bmp` é o nome do novo bmp que você está criando.

Questão de pensamento
----------------

* Como você acha que representa um pixel preto ao usar um arquivo BMP de cor de 24 bits?
* É isso mesmo ou diferente de misturar tintas para representar várias cores?

Como testar o seu código
---------------------

Seu programa deve se comportar conforme os exemplos abaixo.

    smiley/ $ ./colorize smiley.bmp smiley_out.bmp
    

Quando o seu programa estiver funcionando corretamente, você deve ver um novo arquivo chamado `smiley_out.bmp` em seu diretório `smiley`. Abra-o e veja se os pixels pretos agora estão na cor que você especificou.

Você pode verificar seu código usando o `check50`, um programa que a CS50 usará para testar seu código quando você enviá-lo, digitando o seguinte no prompt `$`. Certifique-se de testá-lo você mesmo também!

    check50 cs50/labs/2023/x/smiley
    

Para avaliar se o estilo do seu código (indentação e espaçamento) está correto, digite o seguinte no prompt `$`.

    style50 helpers.c
    
"