Speller
=======

<div class="alert" data-alert="danger" role="alert"><p><strong>Leia esta especificação inteiramente antes de começar para saber o que fazer e como fazê-lo!</strong></p></div>


Neste problema, você implementará um programa que verifica a ortografia de um arquivo, como no exemplo abaixo, usando uma tabela hash.

    $ ./speller texts/lalaland.txt
    MISSPELLED WORDS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    WORDS MISSPELLED:
    WORDS IN DICTIONARY:
    WORDS IN TEXT:
    TIME IN load:
    TIME IN check:
    TIME IN size:
    TIME IN unload:
    TIME IN TOTAL:
    

Introdução
-----------

Conecte-se ao [code.cs50.io](https://code.cs50.io/), clique na janela do seu terminal e execute o comando `cd`. Você deve ver que o prompt da sua janela de terminal se assemelha ao seguinte:

    $
    

Em seguida, execute o comando

    wget https://cdn.cs50.net/2022/fall/psets/5/speller.zip
    

para baixar um arquivo ZIP chamado de `speller.zip` em seu espaço de códigos.

Em seguida, execute o comando

    unzip speller.zip
    

para criar uma pasta chamada `speller`. Você não precisa mais do arquivo ZIP, portanto você pode executar o comando:

    rm speller.zip
    

e responda "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd speller
    

seguido de Enter para mover-se para dentro desse diretório. Seu prompt deve se parecer com o seguinte:

    speller/ $
    

Execute o comando `ls` e você verá alguns arquivos e pastas:

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
    

Se você tiver algum problema durante este processo, siga esses mesmos passos novamente e veja se consegue determinar onde errou!