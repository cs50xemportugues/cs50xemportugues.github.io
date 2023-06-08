Começando
---------------

Acesse [code.cs50.io](https://code.cs50.io/), clique na janela do terminal e execute `cd` sozinho. Você deve encontrar que o prompt da janela do terminal se parece com o seguinte:

    $
    
Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-less.zip
    
para baixar um ZIP chamado `filter-less.zip` em seu espaço de códigos.

Depois execute

    unzip filter-less.zip
    
para criar uma pasta chamada `filter-less`. Você não precisa mais do arquivo ZIP, então execute

    rm filter-less.zip
    
e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd filter-less
    
seguido de Enter para mover-se para (ou seja, abrir) o diretório. Seu prompt agora deve se parecer com o seguinte:

    filter-less/ $
    
Execute `ls` sozinho e você deve ver alguns arquivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` e `Makefile`. Você também deve ver uma pasta chamada `images` com quatro arquivos BMP. Se você tiver algum problema, siga os mesmos passos novamente e veja se você pode determinar onde errou!