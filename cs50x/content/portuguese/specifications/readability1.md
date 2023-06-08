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