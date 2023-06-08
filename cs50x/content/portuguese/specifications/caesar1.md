# Cifra de César

Para este problema, você implementará um programa que criptografa mensagens usando a cifra de César conforme abaixo.

   $./caesar 13
    plaintext:  HELLO
    ciphertext: URYYB
    

## Como começar

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e execute `cd` sozinho. Você deve encontrar que seu "prompt" se parece com o abaixo.

    $

Clique dentro dessa janela do terminal e, em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/2/caesar.zip

seguido de Enter para baixar um arquivo ZIP chamado `caesar.zip` em seu codespace. Tome cuidado para não esquecer o espaço entre `wget` e o URL seguinte, ou qualquer outro caractere!

Agora execute

    unzip caesar.zip

para criar uma pasta chamada `caesar`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm caesar.zip

e responder com "y" seguido de Enter na solicitação para remover o arquivo ZIP baixado.

Agora digite

    cd caesar

seguido de Enter para entrar (ou seja, abrir) nesse diretório. O prompt agora deve se parecer com o abaixo.

    caesar/ $

Se tudo correu bem, você deve executar

    ls

e verá um arquivo chamado `caesar.c`. Executar `code caesar.c` deve abrir o arquivo em que você digitara o código para este conjunto de problemas. Se não, volte seus passos e veja se você pode determinar onde você errou!