Substituição
============

Para este problema, você escreverá um programa que implementa uma cifra de substituição, conforme abaixo.

    $ ./substitution JTREKYAVOGDXPSNCUIZLFBMWHQ
    plaintext:  HELLO
    ciphertext: VKXXN
    

Primeiros passos
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e, em seguida, execute `cd` sozinho. Você deve encontrar que sua “prompt” se parece com a abaixo.

    $
    

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/psets/2/substitution.zip
    

seguido por Enter para baixar um arquivo ZIP chamado `substitution.zip` em seu espaço de códigos. Não se esqueça de não deixar um espaço em branco entre `wget` e a URL seguinte, ou qualquer outro caractere, na verdade!

Agora execute

    unzip substitution.zip
    

para criar uma pasta chamada `substitution`. Não é mais necessário manter o arquivo ZIP, portanto, execute

    rm substitution.zip
    

e responda "y" seguido por Enter no prompt para remover o arquivo ZIP que você baixou.

Digite agora

    cd substitution
    

seguido por Enter para mover-se para dentro (ou seja, abrir) aquele diretório. Sua "prompt" agora deve parecer com a abaixo.

    substitution/ $
    

Se tudo correu bem, você deve executar

    ls
    

e visualizar um arquivo chamado `substitution.c`. Executando `code substitution.c` abrirá o arquivo onde você digitá seu código para este conjunto de problemas. Caso contrário, reveja seus passos e tente determinar onde você errou!

Contexto
----------

Em uma cifra de substituição, “codificamos” (ou seja, ocultamos de forma reversível) uma mensagem substituindo cada letra por outra letra. Para isso, usamos uma _chave_: neste caso, um mapeamento de cada uma das letras do alfabeto para a letra à qual ela deve corresponder quando a codificamos. Para “decodificar” a mensagem, o receptor da mensagem precisaria conhecer a chave, para poder reverter o processo: traduzindo o texto codificado (geralmente chamado de _ciphertext_) de volta para a mensagem original (geralmente chamada de _plaintext_).

Uma chave, por exemplo, pode ser a string `NQXPOMAFTRHLZGECYJIUWSKDVB`. Esta chave de 26 caracteres significa que `A` (a primeira letra do alfabeto) deve ser convertida em `N` (o primeiro caractere da chave), `B` (a segunda letra do alfabeto) deve ser convertida em `Q` (o segundo caractere da chave), e assim por diante.

Uma mensagem como `HELLO`, então, seria codificada como `FOLLE`, substituindo cada uma das letras de acordo com o mapeamento determinado pela chave.

Vamos escrever um programa chamado `substitution` que permite que você criptografe mensagens usando uma cifra de substituição. Na ocasião em que o usuário executa o programa, ele deve decidir, fornecendo um argumento de linha de comando, qual deve ser a chave da mensagem secreta que eles fornecerão durante a execução.

Aqui estão alguns exemplos de como o programa pode funcionar. Por exemplo, se o usuário inserir uma chave `YTNSHKVEFXRBAUQZCLWDMIPGJO` e um plaintext `HELLO`:

    $ ./substitution YTNSHKVEFXRBAUQZCLWDMIPGJO
    plaintext:  HELLO
    ciphertext: EHBBQ
    

Aqui está como o programa poderia funcionar se o usuário fornecer uma chave `VCHPRZGJNTLSKFBDQWAXEUYMOI` e um plaintext `hello, world`:

    $ ./substitution VCHPRZGJNTLSKFBDQWAXEUYMOI
    plaintext:  hello, world
    ciphertext: jrssb, ybwsp
    

Observe que nem a vírgula nem o espaço foram substituídos pela cifra. Substitua apenas os caracteres alfabéticos! Observe também que o caso da mensagem original foi preservado. Letras minúsculas permanecem minúsculas, e letras maiúsculas permanecem maiúsculas.

Não importa se os caracteres da própria chave são em letras maiúsculas ou minúsculas. Uma chave de `VCHPRZGJNTLSKFBDQWAXEUYMOI` é funcionalmente idêntica a uma chave de `vchprzgjntlskfbdqwaxeuymoi` (como também é `VcHpRzGjNtLsKfBdQwAxEuYmOi`).

E se um usuário não fornecer uma chave válida? O programa deve explicar com uma mensagem de erro:

    $ ./substitution ABC
    A chave deve conter 26 caracteres.
    

Ou realmente não coopera, não fornecendo um argumento de linha de comando? O programa deve lembrar o usuário de como usar o programa:

    $ ./substitution
    Uso: ./substitution chave
    

Ou realmente, realmente não coopera, fornecendo muitos argumentos de linha de comando? O programa também deve lembrar o usuário de como usar o programa:

    $ ./substitution 1 2 3
    Uso: ./substitution chave
    

<details><summary>Assista a uma gravação</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-HWzT4fngSv4KtdNFgfgpdLxZY" src="https://asciinema.org/a/HWzT4fngSv4KtdNFgfgpdLxZY.js"></script></details>

Especificação
-------------

Projete e implemente um programa denominado `substitution` que criptografa mensagens usando uma cifra de substituição.

*   Implemente seu programa em um arquivo chamado `substitution.c` em um diretório chamado `substitution`.
*   Seu programa deve aceitar um único argumento de linha de comando, a chave a ser usada para a substituição. A própria chave deve ser insensível a maiúsculas e minúsculas, portanto, se qualquer caractere na chave for maiúsculo ou minúsculo, não deve afetar o comportamento do seu programa.
*   Se o seu programa for executado sem argumentos da linha de comando ou com mais de um argumento da linha de comando, seu programa deve imprimir uma mensagem de erro de sua escolha (com `printf`) e retornar de `main` um valor imediatamente igual a` 1` (que tende a significar um erro).
*   Se a chave for inválida (por não conter 26 caracteres, conter qualquer caractere que não seja um caractere alfabético ou não conter cada letra exatamente uma vez), seu programa deve imprimir uma mensagem de erro de sua escolha (com `printf`) e retornar de `main` um valor imediatamente igual a `1`.
*   Seu programa deve imprimir `plaintext:` (sem uma nova linha) e depois solicitar ao usuário uma `string` de texto simples (usando `get_string`).
*   Seu programa deve imprimir `ciphertext:` (sem uma nova linha) seguido pelo criptograma correspondente do texto simples, com cada caractere alfabético do texto simples substituído pelo caractere correspondente no criptograma; caracteres não alfabéticos devem ser impressos sem alterações.
*   Seu programa deve preservar maiúsculas e minúsculas: letras maiúsculas devem permanecer letras maiúsculas; letras minúsculas devem permanecer letras minúsculas.
*   Depois de imprimir o criptograma, você deve imprimir uma nova linha. Seu programa deve, em seguida, sair retornando `0` de `main`.

Você pode encontrar uma ou mais funções declaradas em `ctype.h` que podem ser úteis, de acordo com [manual.cs50.io](https://manual.cs50.io/).

Passo a Passo
-------------

<div class="ratio ratio-16x9" data-video=""><iframe allow="acelerômetro, autoplay, tela cheia, gyroscope, picture-in-picture" allowfullscreen="" class="border" src="https://www.youtube.com/embed/cXAoZAsgxJ4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Como Testar o Código
---------------------

Execute o comando abaixo para avaliar a correção do seu código usando o `check50`. Mas, certifique-se de compilar e testar você mesmo também!

    check50 cs50/problems/2023/x/substitution
    

Execute o comando abaixo para avaliar o estilo do seu código usando o `style50`.

    style50 substitution.c
    

<details><summary>Como usar o <code>debug50</code></summary><p>Deseja rodar o <code class="language-plaintext highlighter-rouge">debug50</code>? Você pode fazer isso da seguinte forma, após compilar com sucesso o seu código com o <code class="language-plaintext highlighter-rouge">make</code>,</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>debug50 ./substitution KEY
</code></pre></div></div>

<p>onde <code class="language-plaintext highlighter-rouge">KEY</code> é a chave que você dá como argumento de linha de comando para o seu programa. Note que rodar</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>debug50 ./substitution
</code></pre></div></div>

<p>vai fazer com que seu programa seja finalizado, idealmente, solicitando ao usuário uma chave.</p></details>

Como Enviar
-------------

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2023/x/substitution"

