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