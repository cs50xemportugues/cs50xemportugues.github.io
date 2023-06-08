Mario
=====

![screenshot do Mario pulando uma pirâmide](pyramid.png)

Implemente um programa que imprime meia pirâmide em altura específica, como indicado abaixo.

    $ python mario.py
    Altura: 4
         #
        ##
       ###
      ####
    

Introdução
---------------

Faça login no [code.cs50.io](https://code.cs50.io/), clique na janela do seu terminal e execute `cd` sozinho. Você deve ver que o prompt da janela do seu terminal se assemelha ao abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-mario-less.zip
    

para baixar um arquivo ZIP chamado `sentimental-mario-less.zip` no seu espaço de códigos.

Depois execute

    unzip sentimental-mario-less.zip
    

para criar uma pasta chamada `sentimental-mario-less`. Você não precisa mais do arquivo ZIP, então execute

    rm sentimental-mario-less.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd sentimental-mario-less
    

seguido de Enter para entrar (ou seja, abrir) esse diretório. Seu prompt agora deve ser semelhante ao abaixo.

    sentimental-mario-less/ $
    

Digite `ls` sozinho e você verá um arquivo `mario.py`. Se você tiver algum problema, siga novamente os mesmos passos e veja se consegue determinar onde errou!

Especificação
-------------

* Escreva, em um arquivo chamado `mario.py`, um programa que recria a meia-pirâmide usando o caractere hash (`#`) para os blocos, exatamente como fez no [Problem Set 1](../../../1/), exceto que seu programa desta vez deve ser escrito em Python.
* Para tornar as coisas mais interessantes, peça primeiro ao usuário a altura da meia pirâmide com `get_int`: um número inteiro positivo entre `1` e `8`, inclusive.
* Se o usuário não fornecer um número inteiro positivo não maior que `8`, você deve solicitar novamente o mesmo número.
* Em seguida, gere (com a ajuda de `print` e um ou mais loops) a meia-pirâmide desejada.
* Cuide para alinhar o canto inferior esquerdo da sua meia-pirâmide com a borda esquerda da sua janela do terminal.

Uso
-----

Seu programa deve se comportar conforme o exemplo abaixo.

    $ python mario.py
    Altura: 4
         #
        ##
       ###
      ####
    

Teste
-------

Embora o `check50` esteja disponível para este problema, você é incentivado a testar seu código primeiro para cada um dos seguintes itens.

* Execute o seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `-1` e pressione enter. Seu programa deve rejeitar esta entrada como inválida, solicitando novamente para o usuário digitar outro número.
* Execute o seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `0` e pressione enter. Seu programa deve rejeitar esta entrada como inválida, solicitando novamente para o usuário digitar outro número.
* Execute o seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `1` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada no canto inferior esquerdo do seu terminal e que não existam espaços extras no final de cada linha.

    #
    

* Execute o seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `2` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada no canto inferior esquerdo do seu terminal e que não existam espaços extras no final de cada linha.

     #
    ##
    

* Execute o seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `8` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada no canto inferior esquerdo do seu terminal e que não existam espaços extras no final de cada linha.

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########
    

* Execute o seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `9` e pressione enter. Seu programa deve rejeitar esta entrada como inválida, solicitando novamente para o usuário digitar outro número. Em seguida, digite `2` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada no canto inferior esquerdo do seu terminal e que não existam espaços extras no final de cada linha.

     #
    ##
    

* Execute o seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `foo` e pressione enter. Seu programa deve rejeitar esta entrada como inválida, solicitando novamente para o usuário digitar outro número.
* Execute o seu programa como `python mario.py` e aguarde uma solicitação de entrada. Não digite nada e pressione enter. Seu programa deve rejeitar esta entrada como inválida, solicitando novamente para o usuário digitar outro número.

Execute o abaixo para avaliar a correção do código usando `check50`. Mas não se esqueça de compilar e testar por conta própria também!.

    check50 cs50/problems/2023/x/sentimental/mario/less
    

Execute o abaixo para avaliar o estilo do código usando `style50`.

    style50 mario.py
    

Como enviar
-------------

No seu terminal, execute o abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2023/x/sentimental/mario/less"