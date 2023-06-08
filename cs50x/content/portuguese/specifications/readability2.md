## Contexto

De acordo com a [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), o livro _Charlotte’s Web_ de E.B. White está nivelado entre o segundo e o quarto ano e o livro _The Giver_ de Lois Lowry entre o oitavo e o décimo segundo ano. Mas o que significa, afinal, para um livro estar em um determinado nível de leitura?

Bem, em muitos casos, um especialista humano pode ler um livro e decidir em que série escolar acha mais apropriado. Mas um algoritmo também pode descobrir isso!

Então, que características são típicas de níveis de leitura mais altos? Palavras mais longas provavelmente têm uma correlação com níveis de leitura mais altos. Da mesma forma, frases mais longas também têm uma correlação com níveis de leitura mais altos.

Ao longo dos anos, vários "testes de legibilidade" foram desenvolvidos que definem fórmulas para calcular o nível de leitura de um texto. Um desses testes de legibilidade é o _índice Coleman-Liau_. O índice Coleman-Liau de um texto é projetado para indicar o nível escolar necessário para entender algum texto. A fórmula é

    indice = 0.0588 * L - 0.296 * S - 15.8

onde `L` é o número médio de letras por 100 palavras no texto e `S` é o número médio de frases por 100 palavras no texto.

Vamos escrever um programa chamado `readability` que recebe um texto e determina seu nível de leitura. Por exemplo, se o usuário digitar uma linha de texto do Dr. Seuss, o programa deve se comportar da seguinte maneira:

    $ ./readability
    Texto: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Série 3

O texto que o usuário digitou tem 65 letras, 4 frases e 14 palavras. 65 letras por 14 palavras é uma média de cerca de 464,29 letras por 100 palavras (porque 65/14 * 100 = 464,29). E 4 frases por 14 palavras é uma média de cerca de 28,57 frases por 100 palavras (porque 4/14 * 100 = 28,57). Quando aplicamos isso à fórmula Coleman-Liau e arredondamos o resultado para o inteiro mais próximo, obtemos um resultado de 3 (porque 0.0588 * 464,29 - 0.296 * 28,57 - 15,8 = 3): portanto, este trecho está no nível de leitura da terceira série.

Vamos tentar outro exemplo:

    $ ./readability
    Texto: Harry Potter era um garoto muito incomum em muitos aspectos. Para começar, ele odiava as férias de verão mais do que qualquer outra época do ano. Além disso, ele realmente queria fazer sua lição de casa, mas era forçado a fazê-la em segredo, no meio da noite. E ele também era um bruxo.
    Série 5

Este texto tem 214 letras, 4 frases e 56 palavras. Isso dá cerca de 382,14 letras por 100 palavras e 7,14 frases por 100 palavras. Quando aplicamos isso à fórmula Coleman-Liau, obtemos um nível de leitura da quinta série.

À medida que a quantidade média de letras e palavras por frase aumenta, o índice Coleman-Liau dá um nível de leitura mais alto ao texto. Se pegarmos este parágrafo, por exemplo, que tem palavras e frases mais longas do que os dois exemplos anteriores, a fórmula nos dará um nível de leitura do décimo-segundo ano.

    $ ./readability
    Texto: À medida que a quantidade média de letras e palavras por frase aumenta, o índice Coleman-Liau dá um nível de leitura mais alto ao texto. Se pegarmos este parágrafo, por exemplo, que tem palavras e frases mais longas do que os dois exemplos anteriores, a fórmula nos dará um nível de leitura do décimo-segundo ano.
    Série 12

<details><summary>Assista a uma Gravação</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script></details>

## Especificações

Projete e implemente um programa, `readability`, que calcule o índice Coleman-Liau do texto.

- Implemente seu programa em um arquivo chamado `readability.c` em um diretório chamado `readability`.
- Seu programa deve solicitar ao usuário uma `string` de texto usando `get_string`.
- Seu programa deve contar o número de letras, palavras e frases no texto. Você pode assumir que uma letra é qualquer caractere minúsculo de `a` a `z` ou qualquer caractere maiúsculo de `A` a `Z`, qualquer sequência de caracteres separados por espaços deve contar como uma palavra e que qualquer ocorrência de um ponto, ponto de exclamação ou ponto de interrogação indica o final de uma frase.
- Seu programa deve imprimir como saída `"Série X`, onde `X` é o nível escolar calculado pela fórmula Coleman-Liau, arredondado para o inteiro mais próximo.
- Se o número do índice resultante for 16 ou superior (equivalente ou maior que o nível universitário sênior), seu programa deverá imprimir `"Série 16+"` em vez de dar o número exato do índice. Se o número do índice for inferior a 1, o programa deverá imprimir `"Antes da Série 1"`.