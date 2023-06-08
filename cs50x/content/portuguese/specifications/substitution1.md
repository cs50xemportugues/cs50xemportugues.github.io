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