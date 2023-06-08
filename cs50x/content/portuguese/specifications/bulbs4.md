## Especificação

Projete e implemente um programa, `bulbs`, que converte texto em instruções para a série de lâmpadas no palco do CS50 da seguinte maneira:

- Implemente seu programa em um arquivo chamado `bulbs.c`.
- Seu programa deve primeiro solicitar ao usuário uma mensagem usando `get_string`.
- Seu programa deve, em seguida, converter a `string` dada em uma série de números binários de 8 bits, um para cada caractere da string.
- Você pode usar a função fornecida `print_bulb` para imprimir uma série de `0`s e `1`s como uma série de emojis amarelos e pretos, que representam lâmpadas acesas e apagadas.
- Cada "byte" de 8 símbolos deve ser impresso em sua própria linha quando impresso; deve haver um `\n` após o último "byte" de 8 símbolos também.

<details><summary>Dicas para Decimal to Binary</summary><p>Vamos caminhar por um exemplo com o número 4. Como você converteria 4 para binário? Comece considerando o bit mais à direita, aquele que, se ligado, adiciona 1 ao número que estamos representando. Você precisa que este bit seja ativado? Divida 4 por 2 para descobrir:</p>

<mjx-container class = "MathJax CtxtMenu_Attached_0" jax = "CHTML" display="true" justify="left" tabindex="0" ctxtmenu_counter="7" style="font-size: 113,1%; position: relative;"><mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2F"></mjx-c></mjx-mo></mjx-texatom><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mn>4</mn><mrow data-mjx-texclass="ORD"><mo>/</mo></mrow><mn>2</mn><mo>=</mo><mn>2</mn></math></mjx-assistive-mml></mjx-container>

<p>2 divide uniformemente em 4, o que nos diz que não há resto de 1 para se preocupar. Podemos deixar com segurança este bit mais à direita desligado, então:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>0
</code></pre></div></div>

<p>E o bit precedente, agora, aquele que fica à esquerda deste bit que descobrimos? Para verificar, vamos seguir um processo semelhante, mas pegar de onde paramos. No passo anterior, dividimos 4 por 2 e obtivemos 2. Agora, o 2 divide uniformemente em 2? Divide, então não há resto 2 para se preocupar:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>00
</code></pre></div></div>

<p>Vamos continuar ainda mais. Depois de dividir 2 por 2, restamos com 1. A divisão de 1 por 2 deixa um resto de 1. Isso significa que precisaremos ligar este bit:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>100
</code></pre></div></div>

<p>E agora que dividimos nosso número para 0, não precisamos de mais bits para representá-lo. Note que descobrimos os bits para representar 4 na ordem oposta à qual precisamos imprimi-los: provavelmente precisaremos de uma estrutura que nos permita armazenar esses bits, para que possamos imprimi-los para frente mais tarde. E, é claro, em seu código real, você estará trabalhando com <code class="language-plaintext highlighter-rouge">char</code>s de 8 bits, então você vai querer antecipar quaisquer zeros necessários.</p>

<p>Quando se trata de verificar restos, o operador módulo(<code class= "language-plaintext highlighter-rouge">%</code>) pode ser útil! <code class="language-plaintext highlighter-rouge">4%2</code>, por exemplo, retorna 0, o que significa que 2 divide em 4 com um resto de 0.</p></details>


## Como teste seu código

Seu programa deve se comportar como nos exemplos acima. Você pode verificar seu código usando `check50`, um programa que CS50 irá usar para testar seu código quando você enviar, digitando o seguinte no prompt `$`. Mas lembre-se de testá-lo por conta própria também!

    check50 cs50/problems/2023/x/bulbs

Para avaliar o estilo do seu código, digite o seguinte no prompt `$`.

    style50 bulbs.c

## Como Enviar

Em seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/bulbs