### Obtendo entrada do usuário

Vamos primeiro escrever um código em C que obtenha apenas uma entrada de texto do usuário e imprima de volta. Especificamente, implemente em `readability.c` uma função `main` que solicita ao usuário "Texto: " usando `get_string` e, em seguida, imprime o mesmo texto usando `printf`. E lembre-se, ao trabalhar neste programa, que se você usar qualquer função de biblioteca, verifique se inclui os arquivos de cabeçalho correspondentes usando `#include`.

O programa deve se comportar conforme abaixo.

    $ ./readability
    Text: Em meus anos mais jovens e vulneráveis, meu pai me deu alguns conselhos que tenho pensado muito desde então.
    Em meus anos mais jovens e vulneráveis, meu pai me deu alguns conselhos que tenho pensado muito desde então.

### Letras

Agora que você coletou a entrada do usuário, vamos começar a analisar essa entrada contando o número de letras. Considere letras como caracteres alfabéticos maiúsculos ou minúsculos, sem pontuação, dígitos ou outros símbolos.

Adicione em `readability.c`, abaixo de `main`, uma função chamada `count_letters` que recebe um argumento, uma `string` de texto, e retorna um `int`, o número de letras nesse texto. Certifique-se de adicionar o protótipo da função no início do arquivo, para que `main` saiba como chamá-lo. Provavelmente, o protótipo deve se parecer com o abaixo:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">count_letters</span><span class="p">(</span><span class="n">string</span> <span class="n">text</span><span class="p">)</span>
</code></pre></div></div>

Em seguida, chame essa função em `main`, para que, em vez de imprimir o próprio texto, agora o programa imprima o número de letras no texto.

O programa deve se comportar conforme abaixo.

    $ ./readability
    Texto: Alice estava começando a ficar muito cansada de sentar ao lado de sua irmã em frente ao córrego e não ter nada para fazer: uma ou duas vezes ela deu uma espiada no livro que a sua irmã estava lendo, mas não tinha figuras nem conversas nele, "e qual é o uso de um livro", pensou Alice "sem figuras ou conversas?"
    235 letras

<details><summary>Dica</summary><p>Declarada em <code class="language-plaintext highlighter-rouge">ctype.h</code>, existe uma função que pode ser útil, de acordo com o <a href="https://manual.cs50.io/">manual.cs50.io</a>. Se você usar essa função, certifique-se de incluir o cabeçalho no início do seu próprio código!</p></details>

### Palavras

O índice de Coleman-Liau não se preocupa apenas com o número de letras, mas também com o número de palavras em uma frase. Para este problema, consideramos qualquer sequência de caracteres separados por um espaço como uma palavra (então uma palavra hifenizada como `"cabeça-de-ponte"` deve ser considerada uma palavra, não três).

Adicione em `readability.c`, abaixo de `main`, uma função chamada `count_words` que recebe um argumento, uma `string` de texto, e retorna um `int`, o número de palavras nesse texto. Certifique-se de adicionar o protótipo da função no início do arquivo, para que `main` saiba como chamá-lo. (Deixamos o protótipo a seu critério!)

Em seguida, chame essa função em `main` para que seu programa também imprima o número de palavras no texto.

Você pode assumir que uma frase:

- conterá pelo menos uma palavra;
- não começará ou terminará com um espaço; e
- não terá vários espaços em sequência.

Você é, é claro, bem-vindo a tentar uma solução que tolerará vários espaços entre as palavras ou mesmo, nenhuma palavra!

O programa deve se comportar conforme abaixo.

    $ ./readability
    Text: Foi um dia frio e brilhante de abril, e os relógios batiam treze vezes. Winston Smith, com o queixo enfiado no peito na tentativa de escapar do vento, entrou rapidamente pelas portas de vidro das Mansões da Vitória, mas não rápido o suficiente para evitar que uma nuvem de poeira entrasse junto com ele.
    250 letras
    55 palavras