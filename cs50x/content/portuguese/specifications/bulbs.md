Lâmpadas
========

Lâmpadas não-tão-quebradas
---------------------------

Na palestra, você pode ter notado algo que parecia um "bug" no palco, em que algumas das lâmpadas sempre parecem estar desligadas:

![captura de tela da palestra da Semana 2 com faixa de lâmpadas](binary_bulbs.jpg)

Cada sequência de lâmpadas, no entanto, codifica uma mensagem em _binário_, a linguagem que os computadores "falam". Vamos escrever um programa para produzir mensagens secretas próprias, talvez até mesmo que poderíamos colocar no palco!

Começando
----------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e execute o comando `cd` sozinho. Você deve ver que seu "prompt" se parece com o abaixo.

    $
    

Clique dentro dessa janela do terminal e então execute

    wget https://cdn.cs50.net/2022/fall/psets/2/bulbs.zip
    

seguido por Enter para baixar um arquivo ZIP chamado `bulbs.zip` em seu espaço de códigos. Cuidado para não esquecer o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere, na verdade!

Em seguida, execute

    unzip bulbs.zip
    

para criar uma pasta chamada `bulbs`. Você não precisa mais do arquivo ZIP, por isso execute

    rm bulbs.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd bulbs
    

seguido de Enter para entrar (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    bulbs/ $
    

Se tudo correu bem, você deve executar

    ls
    

e ver um arquivo chamado `bulbs.c`. A execução de `code bulbs.c` deve abrir o arquivo onde você digitará o código para este conjunto de problemas. Se não funcionar, volte seus passos e veja se pode determinar onde você se enganou!

Detalhes de Implementação
-------------------------

Para escrever nosso programa, primeiro precisamos pensar em **bases**.

### O Básico

A base mais simples é a base-1, ou _unária_; para escrever um número, _N_, na base-1, simplesmente escreveríamos _N_ `1`s consecutivos. Portanto, o número `4` na base-1 seria escrito como `1111` e o número `12` como `111111111111`. Pense nisso como contar nos dedos ou marcar pontos em um quadro.

Você pode ver por que a base-1 não é muito utilizada atualmente. (Os números ficam bastante longos!) Em vez disso, uma convenção comum é a base 10, ou _decimal_. Na base-10, cada _dígito_ é multiplicado por alguma potência de 10, a fim de representar números maiores. Por exemplo, \\(123\\) é a abreviação de \\(123 =  1 \\cdot 10^2 + 2 \\cdot 10^1 + 3 \\cdot 10^0\\).

A mudança de base é tão simples quanto mudar o \\(10\\) acima para um número diferente. Por exemplo, se você escreveu `123` na base-4, o número que você estaria realmente escrevendo é \\(\small 123 = 1 \cdot 4^2 + 2 \cdot 4^1 + 3 \cdot 4^0\\), o que é igual ao número decimal \\(27\\).

Os computadores, no entanto, usam a base 2, ou _binária_. Em binário, escrever `123` seria um erro, já que os números binários só podem ter `0`s e `1`s. Mas o processo de descobrir exatamente qual número decimal um número binário representa é exatamente o mesmo. Por exemplo, o número `10101` na base-2 representa \\(1 \\cdot 2^4 + 0 \\cdot 2^3 + 1 \\cdot 2^2 + 0 \\cdot 2^1 + 1 \\cdot 2^0\\), o que é igual ao número decimal \\(21\\).

### Codificando uma mensagem

As lâmpadas só podem estar ligadas ou desligadas. Em outras palavras, as lâmpadas representam dois estados possíveis; ou a lâmpada está ligada, ou a lâmpada está desligada, assim como os números binários são apenas 1 ou 0. Teremos que encontrar uma maneira de codificar texto como uma sequência de números binários.

Vamos escrever um programa chamado `bulbs` que recebe uma mensagem e a converte em um conjunto de lâmpadas que poderíamos mostrar a um público desavisado. Faremos isso em duas etapas:

* A primeira etapa consiste em transformar o texto em números decimais. Vamos dizer que queremos codificar a mensagem `HI!`. Felizmente, já temos uma convenção em vigor para fazer isso, o [ASCII](https://asciichart.com/). Note que `H` é representado pelo número decimal `72`, `I` é representado por `73` e `!` é representado por `33`.
* A próxima etapa envolve a conversão de nossos números decimais (como `72`, `73` e `33`) em números binários equivalentes, que usam apenas 0s e 1s. Para ter um número consistente de bits em cada um dos nossos números binários, assuma que cada decimal é representado com 8 bits. `72` é `01001000`, `73` é `01001001` e `33` é `00100001`.

Por fim, interpretaremos esses números binários como instruções para as lâmpadas no palco; 0 está desligado, 1 está ligado. (Você descobrirá que `bulbs.c` inclui uma função `print_bulb` que já foi implementada para você, que recebe um `0` ou `1` e produz emojis representando lâmpadas.)

Aqui está um exemplo de como o programa completo pode funcionar. Diferentemente do palco de Sanders, imprimiremos um byte por linha para clareza.

    # ./bulbs
    Message: HI!
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫🟡
    

Para verificarmos nosso trabalho, podemos ler uma lâmpada acesa (🟡) como um `1` e uma lâmpada apagada (⚫) como um `0`. Então, `HI!` tornou-se

    01001000
    01001001
    00100001
    

o que é precisamente o que esperávamos.

Outro exemplo:

    # ./bulbs
    Message: HI MOM
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫⚫
    ⚫🟡⚫⚫🟡🟡⚫🟡
    ⚫🟡