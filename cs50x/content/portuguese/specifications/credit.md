# Crédito

## Introdução

Abra o [VS Code](https://code.cs50.io/pt/).

Comece clicando dentro da janela do seu terminal, em seguida, execute `cd` sozinho. Você deve encontrar que seu "prompt" é semelhante ao abaixo.

    $

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/psets/1/credit.zip

seguido de Enter para baixar um arquivo ZIP chamado `credit.zip` em seu codespace. Certifique-se de não ignorar o espaço entre `wget` e a seguinte URL, ou qualquer outro caractere!

Agora execute

    unzip credit.zip

para criar uma pasta chamada `credit`. Você não precisa mais do arquivo ZIP, então execute

    rm credit.zip

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd credit

seguido de Enter para se mover para (ou seja, abrir) aquele diretório. Seu prompt agora deve ser semelhante ao abaixo.

    credit/ $

Se tudo correu bem, você deve executar

    ls

e ver um arquivo chamado `credit.c`. Executar `code credit.c` deve abrir o arquivo onde você digitará seu código para este problema. Se não, refaça seus passos e veja se você pode determinar onde errou!

## Cartões de crédito

Um cartão de crédito ou débito, é claro, é um cartão de plástico com o qual você pode pagar por bens e serviços. Impresso nesse cartão está um número que também é armazenado em um banco de dados em algum lugar, para que quando seu cartão seja usado para comprar algo, o credor saiba a quem cobrar. Há muitas pessoas com cartões de crédito neste mundo, então esses números são bastante longos: American Express usa números de 15 dígitos, MasterCard usa números de 16 dígitos e Visa usa números de 13 e 16 dígitos. E esses são números decimais (0 a 9), não binários, o que significa, por exemplo, que a American Express pode imprimir até 10^15 = 1.000.000.000.000.000 cartões únicos! (Isso é... um quatrilhão.)

Na verdade, isso é um pouco de exagero, porque os números de cartão de crédito realmente têm alguma estrutura. Todos os números da American Express começam com 34 ou 37; a maioria dos números da MasterCard começa com 51, 52, 53, 54 ou 55 (eles também têm alguns outros números iniciais potenciais com os quais não nos preocuparemos para este problema); e todos os números da Visa começam com 4. Mas os números de cartão de crédito também têm um "checksum" embutido neles, uma relação matemática entre pelo menos um número e outros. Esse checksum permite que computadores (ou humanos que gostam de matemática) detectem erros de digitação (por exemplo, transposições), se não números fraudulentos, sem ter que consultar um banco de dados, o que pode ser lento. Claro, um matemático desonesto certamente poderia criar um número falso que, no entanto, respeite a restrição matemática, então uma consulta ao banco de dados ainda é necessária para verificações mais rigorosas.

## O algoritmo de Luhn

Então, qual é a fórmula secreta? Bem, a maioria dos cartões usa um algoritmo inventado por Hans Peter Luhn da IBM. De acordo com o algoritmo de Luhn, você pode determinar se um número de cartão de crédito é válido (sintaticamente) da seguinte forma:

1. Multiplique por 2 todos os outros dígitos, começando pelo segundo dígito do final do número, e então some os dígitos desses produtos juntos.
2. Adicione a soma à soma dos dígitos que não foram multiplicados por 2.
3. Se o último dígito do total for 0 (ou, de forma mais formal, se o resto da divisão do total por 10 for congruente a 0), o número é válido!

Isso é meio confuso, então vamos tentar um exemplo com o Visa do David: 4003600000000014.

1. Para fins de discussão, vamos primeiro sublinhar todos os outros dígitos, começando pelo segundo dígito do final do número:

    <p><u>4</u>0<u>0</u>3<u>6</u>0<u>0</u>0<u>0</u>0<u>0</u>0<u>0</u>0<u>1</u>4</p>

    Ok, vamos multiplicar cada um dos dígitos sublinhados por 2:

    1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

    Isso nos dá:

    2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

    Agora vamos adicionar os dígitos desses produtos (ou seja, não os próprios produtos) juntos:

    2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

2. Agora vamos adicionar essa soma (13) à soma dos dígitos que não foram multiplicados por 2 (começando pelo final):

    13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

3. Sim, o último dígito nessa soma (20) é 0, então o cartão de David é legítimo!

Portanto, validar números de cartão de crédito não é difícil, mas pode ficar um pouco tedioso manualmente. Vamos escrever um programa.

## Detalhes da implementação

No arquivo chamado `credit.c` no diretório `credit`, escreva um programa que pede ao usuário um número de cartão de crédito e, em seguida, relata (por meio de `printf`) se é um número de cartão American Express, MasterCard ou Visa válido, de acordo com as definições de cada formato aqui. Para que possamos automatizar alguns testes do seu código, pedimos que a última linha de saída do seu programa seja `AMEX\n` ou `MASTERCARD\n` ou `VISA\n` ou `INVALID\n`, nada mais, nada menos. Para simplicidade, você pode assumir que a entrada do usuário será totalmente numérica (ou seja, sem hífens, como pode ser impresso em um cartão real) e que não terá zeros à esquerda. Mas não assuma que a entrada do usuário vai caber em um `int`! É melhor usar `get_long` da biblioteca do CS50 para obter a entrada dos usuários. (Por quê?)

Considere o exemplo abaixo representativo de como seu próprio programa deve se comportar quando passado um número de cartão de crédito válido (sem hífens).

    $ ./credit
    Number: 4003600000000014
    VISA

Agora, `get_long` por si só já rejeitará hífens (e mais):

    $ ./credit
    Number: 4003-6000-0000-0014
    Number: foo
    Number: 4003600000000014
    VISA

Mas cabe a você detectar entradas que não são números de cartão de crédito (por exemplo, um número de telefone), mesmo que numéricas:

    $ ./credit
    Number: 6176292929
    INVALID

Teste seu programa com uma variedade de entradas, tanto válidas quanto inválidas. (Nós certamente vamos!) Aqui estão alguns [números de cartão](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards) que o PayPal recomenda para testes.

Se o seu programa se comportar incorretamente em algumas entradas (ou não compilar), é hora de depurar!

### Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/dF7wNjsRBjI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Como testar seu código

Você também pode executar o seguinte para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilar e testá-lo também!

    check50 cs50/problems/2023/x/credit

Execute o abaixo para avaliar o estilo do seu código usando `style50`.

    style50 credit.c

## Como Enviar

Em seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/credit