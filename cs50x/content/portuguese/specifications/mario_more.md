# Mario

## Guia de Início

Abra o editor [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal, então execute o comando `cd` sem nenhum argumento para navegar pelo sistema de arquivos. Você deve ter um prompt que se parece com o abaixo.

    $

Clique dentro da janela do terminal e execute o comando

    wget https://cdn.cs50.net/2022/fall/psets/1/mario-more.zip

seguido de Enter para baixar o arquivo ZIP `mario-more.zip` em sua área de trabalho. Cuidado para não esquecer o espaço entre `wget` e a URL, ou qualquer outro caractere!

Agora execute

    unzip mario-more.zip

para criar uma pasta chamada `mario-more`. Você não precisa mais do arquivo ZIP, então pode executar

    rm mario-more.zip

e responder com “y” seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd mario-more

seguido de Enter para entrar (ou abrir) o diretório. Seu prompt deve agora se parecer pelo abaixo.

    mario-more/ $

Se tudo deu certo, execute

    ls

e você verá um arquivo chamado `mario.c`. Execute `code mario.c` para abrir o arquivo no qual você digitará o código para resolver este problema. Se isso não acontecer, refaça os passos anteriores e descubra onde você errou!

## Mundo 1-1

Perto do começo do jogo Super Mario Bros. da Nintendo, Mario precisa atravessar pirâmides adjacentes de blocos, como na imagem abaixo.

![Print Screen de Mario atravessando pirâmides adjacentes.](https://cs50.harvard.edu/x/2023/psets/1/mario/more/pyramids.png)

Vamos reproduzir essas pirâmides em C, com texto e "#" representando os blocos, como abaixo. Cada "#" é um pouco mais alto do que largo, então as próprias pirâmides serão altas e estreitas.

       #  #
      ##  ##
     ###  ###
    ####  ####

O programa que escreveremos será chamado de `mario`. Vamos permitir que o usuário decida a altura das pirâmides digitando um número inteiro positivo entre 1 e 8.

Veja abaixo um exemplo de como o programa deve funcionar se o usuário digitar `8` quando solicitado:

    $ ./mario
    Altura: 8
           #  #
          ##  ##
         ###  ###
        ####  ####
       #####  #####
      ######  ######
     #######  #######
    ########  ########

Veja abaixo um exemplo de como o programa deve funcionar se o usuário digitar `4` quando solicitado:

    $ ./mario
    Altura: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Veja abaixo um exemplo de como o programa deve funcionar se o usuário digitar `2` quando solicitado:

    $ ./mario
    Altura: 2
     #  #
    ##  ##

E veja abaixo um exemplo de como o programa deve funcionar se o usuário digitar `1` quando solicitado:

    $ ./mario
    Altura: 1
    #  #

Se o usuário não digitar um número inteiro positivo entre 1 e 8, o programa deve solicitar novamente até obter uma resposta válida:

    $ ./mario
    Altura: -1
    Altura: 0
    Altura: 42
    Altura: 50
    Altura: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Observe que a largura do "espaço" entre as pirâmides adjacentes é igual à largura de dois "#", independentemente da altura das pirâmides.

Abra o arquivo `mario.c` para implementar esse problema como descrito!

### Passo a Passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/FzN9RAjYG_Q?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Como Testar Seu Código

Seu código funciona como prescrito quando você insere:

- `-1` (ou outros números negativos)?
- `0`?
- Números de `1` a `8`?
- `9` ou outros números positivos?
- letras ou palavras?
- nenhuma entrada, quando você somente pressiona Enter?

Você também pode executar o seguinte comando para avaliar a correção do seu código usando `check50`. Mas não esqueça de compilar e testar o código sozinho também!

    check50 cs50/problems/2023/x/mario/more

Execute o comando abaixo para avaliar o estilo do seu código usando `style50`.

    style50 mario.c

## Como Enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/mario/more
"