# Lâmpadas

## Lâmpadas Não-Tão-Quebradas

Durante a palestra, você pode ter percebido o que parecia ser um "bug" no palco da frente, onde algumas das lâmpadas sempre parecem estar apagadas:

![Captura de tela da palestra da semana 2 com uma sequência de lâmpadas](https://cs50.harvard.edu/x/2023/psets/2/bulbs/binary_bulbs.jpg)

Cada sequência de lâmpadas codifica uma mensagem em _binário_, a linguagem que os computadores "falam". Vamos escrever um programa para criar nossas próprias mensagens secretas, talvez que possamos até mesmo pôr em um palco!

## Começando

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e execute o comando `cd` isoladamente. Você deve ver que a "prompt" se parece com o abaixo.

    $

Clique dentro da janela do terminal e depois execute a seguinte linha de comando:

    wget https://cdn.cs50.net/2022/fall/psets/2/bulbs.zip

seguido por Enter para baixar um ZIP chamado `bulbs.zip` em seu espaço de código. Certifique-se de não ignorar o espaço entre `wget` e a URL a seguir, ou qualquer outro caractere!

Agora execute

    unzip bulbs.zip

para criar uma pasta chamada `bulbs`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm bulbs.zip

e responder com "y", seguido por Enter, na prompt para remover o arquivo ZIP que você baixou.

Digite

    cd bulbs

seguido por Enter para se mover para dentro daquele diretório. Sua prompt agora deve se parecer com a abaixo.

    bulbs/ $

Se tudo correu bem, você deve executar

    ls

e ver um arquivo chamado `bulbs.c`. Executando `code bulbs.c` você pode abrir o arquivo onde vai digitar o seu código para este problema. Caso contrário, volte alguns passos e tente determinar onde você errou!

## Detalhes da Implementação

Para escrever nosso programa, primeiro precisamos pensar sobre **bases**.