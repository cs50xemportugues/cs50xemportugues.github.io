# Facilidade de Leitura

Para este problema, você implementará um programa que calcula o nível aproximado de escolaridade necessário para compreender algum texto, conforme abaixo.

    $ ./readability
    Texto: Parabéns! Hoje é seu dia. Você está se dirigindo a grandes lugares! Você está saindo do nada!
    Grau 3

## Primeiros Passos

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da sua janela do terminal e, em seguida, execute `cd` sozinho. Você deve encontrar que o "prompt" se assemelha ao abaixo.

    $

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/psets/2/readability.zip

seguido de Enter para baixar um arquivo ZIP chamado `readability.zip` em seu ambiente de codificação. Cuidado para não ignorar o espaço entre `wget` e a URL a seguir, ou qualquer outro caractere!

Agora execute

    unzip readability.zip

para criar uma pasta chamada `readability`. Você não precisa mais do arquivo ZIP, então execute

    rm readability.zip

e responda com "y" seguido de Enter na solicitação para remover o arquivo ZIP que você baixou.

Agora digite

    cd readability

seguido de Enter para se mover para (i.e., abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    readability/ $

Se tudo correu bem, você deve executar

    ls

e ver um arquivo chamado `readability.c`. Executar `code readability.c` deve abrir o arquivo onde você irá escrever seu código para este conjunto de problemas. Caso contrário, refaça seus passos e veja se consegue determinar onde errou!

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

### Sentenças

A última informação que a fórmula Coleman-Liau se preocupa, além do número de letras e palavras, é o número de sentenças. Determinar o número de sentenças pode ser surpreendentemente complicado. Você pode imaginar que uma sentença é apenas qualquer sequência de caracteres que termina com um ponto, mas é claro que as sentenças também podem terminar com um ponto de exclamação ou uma interrogação. Mas é claro, nem todos os pontos necessariamente significam que a sentença acabou. Por exemplo, considere a sentença abaixo.

    Sr. e Sra. Dursley, do número quatro da Rua dos Alfeneiros, estavam orgulhosos por dizer que eram perfeitamente normais, muito obrigado.

Essa é apenas uma única sentença, mas existem três pontos! Para este problema, pediremos para você ignorar essa sutileza: você deve considerar qualquer sequência de caracteres que termine com `.` ou `!` ou `?` como uma sentença (então para a "sentença" acima, você deve considerar três sentenças). Na prática, a detecção de limite de sentença precisa ser um pouco mais inteligente para lidar com esses casos, mas não se preocupe com isso por enquanto.

Adicione ao arquivo `readability.c`, abaixo do `main`, uma função chamada `count_sentences` que recebe um argumento, uma `string` de texto, e que retorna um `int`, o número de sentenças naquele texto. Certifique-se de adicionar o protótipo da função também no topo do arquivo, para que o `main` saiba como chamá-lo. (Deixamos o protótipo da função para você definir!)

Então, chame essa função no `main` para que o seu programa também imprima o número de sentenças no texto.

O programa agora deve se comportar conforme o abaixo.

    $ ./readability
    Texto: Quando ele tinha quase treze anos, meu irmão Jem quebrou o braço gravemente no cotovelo. Quando sarou, e os medos de Jem de nunca mais poder jogar futebol foram acalmados, ele raramente se mostrou autoconsciente sobre sua lesão. Seu braço esquerdo era um pouco mais curto do que o direito; quando ele ficava em pé ou caminhava, o dorso de sua mão ficava em ângulo reto com o corpo, o polegar paralelo à coxa.
    295 letras
    70 palavras
    3 sentenças

### Colocando Tudo Junto

Agora é hora de juntar todas as peças! Lembre-se de que o índice Coleman-Liau é calculado usando a fórmula:

    índice = 0.0588 * L - 0.296 * S - 15.8

onde `L` é o número médio de letras por 100 palavras no texto e `S` é o número médio de sentenças por 100 palavras no texto.

Modifique o `main` em `readability.c` para que, em vez de imprimir o número de letras, palavras e sentenças, ele imprima (apenas) o nível de grau conforme definido pelo índice Coleman-Liau (por exemplo, `"Grau 2"` ou `"Grau 8"` ou similar). Certifique-se de arredondar o número do índice resultante para o número inteiro mais próximo!

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que `round` é declarado em `math.h`, de acordo com o <a href="https://manual.cs50.io/">manual.cs50.io</a>!</li>
  <li data-marker="*">Lembre-se de que, ao dividir valores do tipo `int` em C, o resultado também será um `int`, com qualquer resto (ou seja, dígitos após a vírgula decimal) descartados. Em outras palavras, o resultado será "truncado". Você pode querer converter um ou mais valores em `float` antes de fazer a divisão ao calcular `L` e `S`!</li>
</ul></details>

Se o número do índice resultante for 16 ou maior (equivalente ou superior a um nível de leitura de graduação superior), seu programa deve imprimir `"Grau 16+"` em vez de imprimir um número de índice exato. Se o número do índice for menor que 1, seu programa deve imprimir `"Antes do Grau 1"`.

## Passo a Passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/AOVyZEh9zgE?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como Testar seu Código

Tente executar seu programa nos seguintes textos, para garantir que você veja o nível de escolaridade especificado. Certifique-se de copiar apenas o texto, sem espaços extras.

- `One fish. Two fish. Red fish. Blue fish.` (Antes do 1º Ano)
- `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` (2º Ano)
- `Congratulations! Today is your day. You're off to Great Places! You're off and away!` (3º Ano)
- `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` (5º Ano)
- `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` (7º Ano)
- `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` (8º Ano)
- `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` (8º Ano)
- `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` (9º Ano)
- `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` (10º Ano)
- `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` (Graduação)

Execute abaixo para avaliar a correção do seu código ainda mais usando `check50`. Mas não se esqueça de compilá-lo e testá-lo também!

    check50 cs50/problems/2023/x/readability

Execute abaixo para avaliar o estilo do seu código usando `style50`.

    style50 readability.c

## Como Enviar

No terminal, execute abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/readability


