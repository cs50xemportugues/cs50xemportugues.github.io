Crédito 
======

Implemente um programa que determine se um número de cartão de crédito fornecido é válido de acordo com o algoritmo de Luhn.

    $ python credit.py
    Número: 378282246310005
    AMEX
    

Introdução
---------------

Faça login em [code.cs50.io] (https://code.cs50.io/) , clique na sua janela do terminal e execute `cd` sozinho. Você deve encontrar que o prompt da sua janela do terminal se pareça com o abaixo:

    $
    

A seguir, execute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-credit.zip
    

para baixar um ZIP chamado `sentimental-credit.zip` no seu codespace.

Em seguida, execute

    unzip sentimental-credit.zip
    

para criar uma pasta chamada `sentimental-credit`. Você não precisa mais do arquivo ZIP, então execute

    rm sentimental-credit.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd sentimental-credit
    

seguido de Enter para mover-se para (ou seja, abrir) esse diretório. Seu prompt agora deve se assemelhar ao abaixo.

    sentimental-credit/ $
    

Execute `ls` sozinho e você deve ver `credit.py`. Se você encontrar qualquer problema, siga essas mesmas etapas novamente e veja se consegue determinar onde errou!

Especificação
-------------

*   Em `credit.py`, escreva um programa que solicita ao usuário um número de cartão de crédito e, em seguida, relata (via `print`) se é um número de cartão de crédito American Express, MasterCard ou Visa válido, exatamente como você fez no [Problem Set 1](../../1/), exceto que seu programa desta vez deve ser escrito em Python.
*   Para que possamos automatizar alguns testes do seu código, pedimos que a última linha de saída do seu programa seja ` AMEX \ n` ou` MASTERCARD \ n` ou `VISA \ n` ou` INVALID \ n `, nada mais, nada menos.
*   Para simplificar, você pode assumir que a entrada do usuário será inteiramente numérica (ou seja, sem hífens, como pode ser impresso em um cartão real).
*   Melhor usar `get_int` ou `get_string` da biblioteca CS50 para obter a entrada dos usuários, dependendo de como você decide implementar este.

Uso
-----

Seu programa deve se comportar conforme o exemplo abaixo.

    $ python credit.py
    Número: 378282246310005
    AMEX
    

Dicas
-----

*   É possível usar expressões regulares para validar a entrada do usuário. Você pode usar o módulo [`re`] do Python(https://docs.python.org/3/library/re.html), por exemplo, para verificar se a entrada do usuário é realmente uma sequência de dígitos com o comprimento correto.

Testando
-------

Embora `check50` esteja disponível para este problema, você é encorajado a testar seu código primeiro para cada um dos seguintes.

*   Execute seu programa como `python credit.py` e aguarde um prompt para entrada. Digite `378282246310005` e pressione enter. Seu programa deve imprimir `AMEX`.
*   Execute seu programa como `python credit.py` e aguarde um prompt para entrada. Digite `371449635398431` e pressione enter. Seu programa deve imprimir `AMEX`.
*   Execute seu programa como `python credit.py` e aguarde um prompt para entrada. Digite `5555555555554444` e pressione enter. Seu programa deve imprimir `MASTERCARD`.
*   Execute seu programa como `python credit.py` e aguarde um prompt para entrada. Digite `5105105105105100` e pressione enter. Seu programa deve imprimir `MASTERCARD`.
*   Execute seu programa como `python credit.py` e aguarde um prompt para entrada. Digite `4111111111111111` e pressione enter. Seu programa deve imprimir `VISA`.
*   Execute seu programa como `python credit.py` e aguarde um prompt para entrada. Digite `4012888888881881` e pressione enter. Seu programa deve imprimir `VISA`.
*   Execute seu programa como `python credit.py` e aguarde um prompt para entrada. Digite `1234567890` e pressione enter. Seu programa deve imprimir `INVALID`.

Execute o abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo você mesmo também!

    check50 cs50/problems/2023/x/sentimental/credit
    

Execute o abaixo para avaliar o estilo do seu código usando `style50`.

    style50 credit.py
    

Como Enviar
-------------

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/sentimental/credit"