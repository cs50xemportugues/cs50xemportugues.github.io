Legibilidade
===========

Implemente um programa que calcule o nível de grau aproximado necessário para compreender um determinado texto, conforme abaixo.

    $ python readability.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3
    

Como começar
---------------

Faça login em [code.cs50.io](https://code.cs50.io/), clique na janela do seu terminal e execute `cd`. Você deverá encontrar o prompt da sua janela do terminal como abaixo:

    $
    

Em seguida, execute:

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-readability.zip
    

para baixar um ZIP denominado `sentimental-readability.zip` no seu espaço de códigos.

Em seguida, execute:

    unzip sentimental-readability.zip
    

para criar uma pasta chamada 'sentimental-readability'. Você não precisa mais do arquivo ZIP, então execute:

    rm sentimental-readability.zip
    

e responda com "y" seguido de Enter para remover o arquivo ZIP que você baixou.

Agora digite:

    cd sentimental-readability
    

seguido de Enter para mover-se para (ou seja, abrir) esse diretório. Seu prompt deve ser como abaixo:

    sentimental-readability/ $
    

Execute `ls` por si só e você deve ver `readability.py`. Se você tiver algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde errou!

Especificação
-------------

* Escreva, em um arquivo chamado `readability.py`, um programa que primeiro solicita ao usuário que digite algum texto e, em seguida, apresente o nível de leitura do texto de acordo com a fórmula Coleman-Liau, exatamente como fez no [Problem Set 2](../../ 2 /), exceto que desta vez o programa deve ser escrito em Python.
   * Lembre-se de que o índice Coleman-Liau é calculado como `0.0588 * L - 0.296 * S - 15.8`, onde `L` é o número médio de letras por 100 palavras no texto e` S` é o número médio de frases por 100 palavras no texto.
* Use o `get_string` da biblioteca CS50 para obter a entrada do usuário e `print` para exibir a resposta.
* Seu programa deve contar o número de letras, palavras e frases no texto. Você pode supor que uma letra é qualquer caractere minúsculo de `a` a `z` ou qualquer caractere maiúsculo de `A` a `Z`, qualquer sequência de caracteres separados por espaços deve contar como uma palavra e que qualquer ocorrência de um ponto, ponto de exclamação ou ponto de interrogação indica o final de uma frase.
* Seu programa deve imprimir como saída `"Grade X"` onde `X` é o nível de leitura calculado pela fórmula Coleman-Liau, arredondado para o inteiro mais próximo.
* Se o índice resultante for 16 ou superior (equivalente ou superior a um nível de leitura de graduação sênior), seu programa deve apresentar a mensagem `"Grade 16+"` em vez de fornecer o índice exato. Se o índice for inferior a 1, seu programa deve apresentar a mensagem `"Before Grade 1"`.

Uso
-----

Seu programa deve se comportar como o exemplo abaixo.

    $ python readability.py
    Text: Parabéns! Hoje é o seu dia. Você está a caminho de lugares incríveis! Está indo embora!
    Grade 3


Testando
-------

Embora o `check50` esteja disponível para este problema, é incentivado que você primeiro teste seu código por conta própria para cada um dos seguintes casos.

*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `One fish. Two fish. Red fish. Blue fish.` e pressione enter. Seu programa deve apresentar a saída `Before Grade 1`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` e pressione enter. Seu programa deve apresentar a saída `Grade 2`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `Congratulations! Today is your day. You're off to Great Places! You're off and away!` e pressione enter. Seu programa deve apresentar a saída `Grade 3`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` e pressione enter. Seu programa deve apresentar a saída `Grade 5`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` e pressione enter. Seu programa deve apresentar a saída `Grade 7`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` e pressione enter. Seu programa deve apresentar a saída `Grade 8`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` e pressione enter. Seu programa deve apresentar a saída `Grade 8`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` e pressione enter. Seu programa deve apresentar a saída `Grade 9`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` e pressione enter. Seu programa deve apresentar a saída `Grade 10`.
*   Execute seu programa como `python readability.py`, e aguarde a solicitação de entrada. Digite `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` e pressione enter. Seu programa deve apresentar a saída `Grade 16+`.

Execute o comando abaixo para avaliar a correção do seu código usando `check50`. Certifique-se de compilar e testar você mesmo também!

    check50 cs50/problems/2023/x/sentimental/readability
    

Execute o comando abaixo para avaliar o estilo do seu código usando `style50`.

    style50 readability.py
    "

Como enviar

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2023/x/sentimental/readability

