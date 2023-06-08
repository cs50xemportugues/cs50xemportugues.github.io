### Codificando uma Mensagem

As lâmpadas só podem estar acessas ou apagadas. Em outras palavras, as lâmpadas representam dois estados possíveis; ou a lâmpada está acessa, ou a lâmpada está apagada, assim como os números binários são representados como 1 ou 0. Precisamos encontrar uma forma de codificar texto como uma sequência de números binários.

Vamos escrever um programa chamado `bulbs` que recebe uma mensagem e a converte em um conjunto de lâmpadas que poderíamos mostrar para uma plateia desatenta. Realizaremos essa tarefa em duas etapas:

- A primeira etapa consiste em transformar o texto em números decimais. Digamos que queremos codificar a mensagem `HI!`. Felizmente, já temos uma convenção em vigor para fazer isso, o [ASCII](https://asciichart.com/). Observe que `H` é representado pelo número decimal `72`, `I` é representado por `73` e `!` é representado por `33`.
- A próxima etapa envolve a conversão dos nossos números decimais (como `72`, `73` e `33`) em números binários equivalentes, que usam apenas 0s e 1s. Para ter um número consistente de bits em cada um dos nossos números binários, assuma que cada decimal é representado com 8 bits. `72` é `01001000`, `73` é `01001001` e `33` é `00100001`.

Por último, interpretaremos esses números binários como instruções para as lâmpadas no palco; 0 é apagada, 1 está acessa. (Você encontrará no arquivo `bulbs.c` uma função chamada `print_bulb` que já foi implementada para você, e que recebe um `0` ou `1` como parâmetro e imprime um emoji representando as lâmpadas.)

Aqui está um exemplo de como o programa completo poderia funcionar. Ao contrário do palco de Sanders, imprimiremos um byte por linha para clareza.

    # ./bulbs
    Mensagem: HI!
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫🟡

Para verificar nosso trabalho, podemos ler uma lâmpada que está acessa (🟡) como `1` e uma lâmpada apagada (⚫) como `0`. Assim `HI!` ficou:

    01001000
    01001001
    00100001

que é precisamente o que esperávamos.

Outro exemplo:

    # ./bulbs
    Mensagem: HI MOM
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫⚫
    ⚫🟡⚫⚫🟡🟡⚫🟡
    ⚫🟡⚫⚫🟡🟡🟡🟡
    ⚫🟡⚫⚫🟡🟡⚫🟡

Observe que todos os caracteres estão incluídos nas instruções das lâmpadas, incluindo caracteres não alfabéticos, como espaços (`00100000`).