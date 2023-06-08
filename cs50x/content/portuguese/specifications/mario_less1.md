# Mario

## Começando

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e, em seguida, execute `cd` sozinho. Você deve ver que o "prompt" se parece com o abaixo.

    $

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/psets/1/mario-less.zip

seguido de Enter para baixar um arquivo ZIP chamado `mario-less.zip` em seu espaço de código. Tome cuidado para não ignorar o espaço entre "wget" e a URL a seguir, ou qualquer outro caractere!

Agora execute

    unzip mario-less.zip

para criar uma pasta chamada `mario-less`. Você não precisa mais do arquivo ZIP, então execute

    rm mario-less.zip

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd mario-less

seguido de Enter para entrar nesse diretório. O seu prompt agora deve se parecer com o abaixo.

    mario-less/ $

Se tudo correu bem, você deve digitar

    ls

e ver um arquivo chamado "mario.c". Ao executar "code mario.c", o arquivo deverá ser aberto para que você possa digitar seu código para este problema. Caso contrário, refaça seus passos e veja se consegue determinar onde você errou!

## World 1-1

No final do World 1-1 do jogo Super Mario Brothers da Nintendo, Mario deve subir uma pirâmide alinhada à direita, como mostrado abaixo.

![captura de tela de Mario subindo uma pirâmide alinhada à direita](https://cs50.harvard.edu/x/2023/psets/1/mario/less/pyramid.png)

Vamos recriar aquela pirâmide em C, embora em texto, usando hashtags (`#`) para representar tijolos, como mostrado abaixo. Cada hashtag é um pouco mais alta do que é larga, então a própria pirâmide também será mais alta do que é larga.

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

O programa que escreveremos será chamado de `mario`. E vamos permitir que o usuário decida qual deve ser a altura da pirâmide, solicitando inicialmente um número inteiro positivo entre, digamos, 1 e 8, inclusive.

Veja como o programa pode funcionar se o usuário informar `8` quando solicitado:

    $ ./mario
    Altura: 8
           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Veja como o programa pode funcionar se o usuário informar `4` quando solicitado:

    $ ./mario
    Altura: 4
       #
      ##
     ###
    ####

Veja como o programa pode funcionar se o usuário informar `2` quando solicitado:

    $ ./mario
    Altura: 2
     #
    ##

E veja como o programa pode funcionar se o usuário informar `1` quando solicitado:

    $ ./mario
    Altura: 1
    #

Se o usuário não informar um número inteiro positivo entre 1 e 8, inclusive, quando solicitado, o programa deverá solicitar novamente até que o usuário colabore:

    $ ./mario
    Altura: -1
    Altura: 0
    Altura: 42
    Altura: 50
    Altura: 4
       #
      ##
     ###
    ####

Como começar? Vamos abordar este problema um passo de cada vez.

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>