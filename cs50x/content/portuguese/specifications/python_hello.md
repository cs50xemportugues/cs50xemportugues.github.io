Olá
====

Implemente um programa que imprima uma saudação simples ao usuário, conforme abaixo.

    $ python hello.py
    Qual é o seu nome?
    David
    olá, David
    

Introdução
----------

Faça login em [code.cs50.io](https://code.cs50.io/), clique na janela do terminal e execute `cd` sozinho. Você deve ver que o prompt da sua janela do terminal se parece com o abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-hello.zip
    

para baixar um arquivo ZIP chamado `sentimental-hello.zip` no seu espaço de códigos.

Em seguida, execute

    unzip sentimental-hello.zip
    

para criar uma pasta chamada `sentimental-hello`. Você não precisa mais do arquivo ZIP, então execute

    rm sentimental-hello.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd sentimental-hello
    

seguido de Enter para se mover para (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    sentimental-hello/ $
    

Execute `ls` sozinho e você deve ver `hello.py`. Se você tiver algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde errou!

Especificação
-------------

Escreva, em um arquivo chamado `hello.py`, um programa que solicita ao usuário seu nome e, em seguida, imprime `olá, fulano de tal`, em que `fulano de tal` é o nome fornecido pelo usuário, exatamente como você fez no [Problem Set 1](../../1/), mas desta vez deverá ser escrito em Python.

Utilização
----------

Seu programa deve se comportar conforme o exemplo abaixo.

    $ python hello.py
    Qual é o seu nome?
    Emma
    olá, Emma
    

Teste
-----

Embora o `check50` esteja disponível para este problema, você é incentivado a testar seu código primeiro por conta própria para cada um dos seguintes pontos.

* Execute seu programa como `python hello.py` e aguarde um prompt para a entrada. Digite `David` e pressione Enter. Seu programa deverá gerar a saída `olá, David`.
* Execute seu programa como `python hello.py` e aguarde um prompt para a entrada. Digite `Bernie` e pressione Enter. Seu programa deverá gerar a saída `olá, Bernie`.
* Execute seu programa como `python hello.py` e aguarde um prompt para a entrada. Digite `Carter` e pressione Enter. Seu programa deverá gerar a saída `olá, Carter`.

Execute o seguinte para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilar e testá-lo por conta própria também!

    check50 cs50/problems/2023/x/sentimental/hello
    

Execute o seguinte para avaliar o estilo do seu código usando `style50`.

    style50 hello.py
    

Como enviar
-----------

No seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2023/x/sentimental/hello"