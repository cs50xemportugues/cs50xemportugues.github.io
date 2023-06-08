Dinheiro
====

Implemente um programa que calcule o número mínimo de moedas necessárias para dar o troco ao usuário.

    $ python cash.py
    Quanto devo: 0.41
    4
    

Primeiros Passos
-----------------

Acesse [code.cs50.io](https://code.cs50.io/), clique na janela do terminal e execute o comando `cd`. Você deverá ver que a linha de comando ficará semelhante a esta:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-cash.zip
    

para baixar um arquivo ZIP chamado `sentimental-cash.zip` em seu ambiente de desenvolvimento.

Então execute

    unzip sentimental-cash.zip
    

para criar uma pasta chamada `sentimental-cash`. Você não precisa mais do arquivo ZIP, então execute

    rm sentimental-cash.zip
    

e responda "y", seguido de Enter, para remover o arquivo ZIP que você baixou.

Agora digite

    cd sentimental-cash
    

seguido de Enter para se mover para este diretório. Sua linha de comando deve ficar parecida com esta:

    sentimental-cash/ $
    

Execute o comando `ls`, e você deve ver o arquivo `cash.py`. Se você tiver problemas, siga os mesmos passos novamente e veja onde errou!

Especificação
-------------

*   Escreva um programa, em um arquivo chamado `cash.py`, que primeiro pergunte ao usuário quanto troco deve ser dado e depois informe o número mínimo de moedas necessárias para fazer o troco. Você pode fazer exatamente como fez no [Problema Set 1](../../  1/), exceto que desta vez seu programa deve ser escrito em Python, e você deve assumir que o usuário irá inserir o troco em dólares (por exemplo, 0,50 dólares em vez de 50 centavos).
*   Use `get_float` da biblioteca CS50 para obter a entrada do usuário e `print` para exibir sua resposta. Assuma que as únicas moedas disponíveis são quartos (25¢), dimes (10¢), nickels (5¢) e pennies (1¢).
    *   Pedimos que você use `get_float` para poder lidar com dólares e centavos, embora sem o símbolo do dólar. Em outras palavras, se algum cliente tiver que receber $9,75 (como no caso em que um jornal custa 25¢, mas o cliente paga com uma nota de $10), assuma que a entrada do seu programa será `9,75` e não `$9,75` ou `975`. No entanto, se algum cliente tiver que receber $9 exatamente, assuma que a entrada do seu programa será `9,00` ou apenas `9`, mas novamente não `$9` ou `900`. Naturalmente, devido à natureza dos valores de ponto flutuante, seu programa provavelmente funcionará com entradas como `9,0` e `9,000`; você não precisa se preocupar em verificar se a entrada do usuário está "formatada" como deveria ser em dinheiro.
*   Se o usuário não fornecer um valor não negativo, o seu programa deve pedir novamente um valor válido até que o usuário a proporcione.
*   Por sinal, para que possamos automatizar alguns testes em seu código, pedimos que a última linha de saída do seu programa seja apenas o número mínimo de moedas possível: um número inteiro seguido de uma nova linha.

Uso
-----

Seu programa deve se comportar conforme o exemplo abaixo:

    $ python cash.py
    Quanto devo: 0.41
    4
    

Testes
-------

Embora `check50` esteja disponível para este problema, recomendamos que você primeiro teste seu código para cada um dos itens.

*   Execute seu programa como `python cash.py` e aguarde uma solicitação de entrada. Digite `0,41` e pressione Enter. Seu programa deve exibir `4`.
*   Execute seu programa como `python cash.py` e aguarde uma solicitação de entrada. Digite `0,01` e pressione Enter. Seu programa deve exibir `1`.
*   Execute seu programa como `python cash.py` e aguarde uma solicitação de entrada. Digite `0,15` e pressione Enter. Seu programa deve exibir `2`.
*   Execute seu programa como `python cash.py` e aguarde uma solicitação de entrada. Digite `1,60` e pressione Enter. Seu programa deve exibir `7`.
*   Execute seu programa como `python cash.py` e aguarde uma solicitação de entrada. Digite `23` e pressione Enter. Seu programa deve exibir `92`.
*   Execute seu programa como `python cash.py` e aguarde uma solicitação de entrada. Digite `4,2` e pressione Enter. Seu programa deve exibir `18`.
*   Execute seu programa `python cash.py`, e aguarde uma solicitação de entrada. Digite `-1` e pressione Enter. Seu programa deve rejeitar esta entrada como inválida, pedindo que o usuário digite outro número.
*   Execute seu programa `python cash.py`, e aguarde uma solicitação de entrada. Digite `foo` e pressione Enter. Seu programa deve rejeitar esta entrada como inválida, pedindo que o usuário digite outro número.
*   Execute seu programa `python cash.py`, e aguarde uma solicitação de entrada. Não digite nada e pressione Enter. Seu programa deve rejeitar esta entrada como inválida, pedindo que o usuário digite outro número.

Execute o comando abaixo para avaliar a correção do seu código utilizando `check50`. Mas certifique-se de compilá-lo e testá-lo por conta própria também!

    check50 cs50/problems/2023/x/sentimental/cash
    

Execute o comando abaixo para avaliar o estilo do seu código utilizando `style50`.

    style50 cash.py
    

Como Submeter
-------------

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/sentimental/cash"