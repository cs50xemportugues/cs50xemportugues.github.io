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