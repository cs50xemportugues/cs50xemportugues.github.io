Recuperar
======

Implemente um programa que recupere JPEGs de uma imagem forense, conforme abaixo.

    $ ./recover card.raw
    

Contexto
----

Antecipando este problema, nos últimos dias tiramos fotos em torno do campus, todas elas foram salvas em uma câmera digital como JPEGs em um cartão de memória. Infelizmente, por algum motivo, as fotos foram todas excluídas! Felizmente, no mundo da computação, “excluído” não significa tanto assim, mas sim “esquecido”. Mesmo que a câmera insista que o cartão está em branco, temos quase certeza de que isso não é bem verdade. Na verdade, estamos esperando (ah, queremos dizer...) que você possa escrever um programa que recupere as fotos para nós!

Embora JPEGs sejam mais complicados que BMPs, eles têm “assinaturas”, padrões de bytes que podem distingui-los de outros formatos de arquivo. Especificamente, os três primeiros bytes de um JPEG são 

    0xff 0xd8 0xff
    
do primeiro ao terceiro byte, da esquerda para a direita. Enquanto isso, o quarto byte é ou `0xe0`, `0xe1`, `0xe2`, `0xe3`, `0xe4`, `0xe5`, `0xe6`, `0xe7`, `0xe8`, `0xe9`, `0xea`, `0xeb`, `0xec`, `0xed`, `0xee`, ou `0xef`. Em outras palavras, os primeiros quatro bits do quarto byte são `1110`.

Ao encontrar esse padrão de quatro bytes em um meio conhecido por armazenar fotos (por exemplo, meu cartão de memória), é provável que demarque o início de um arquivo JPEG. Justo, você pode encontrar esses padrões em algum disco puramente por acaso, então a recuperação de dados não é uma ciência exata.

Felizmente, as câmeras digitais tendem a armazenar fotografias contiguamente em cartões de memória, em que cada foto é armazenada imediatamente após a foto anterior. Consequentemente, o início de um JPEG geralmente demarca o fim de outro. No entanto, as câmeras digitais geralmente inicializam cartões com um sistema de arquivo FAT cujo “tamanho de bloco” é de 512 bytes (B). A implicação é que essas câmeras escrevem apenas nesses cartões em unidades de 512 B. Uma foto de 1 MB (ou seja, 1.048.576 B), por exemplo, ocupa 1048576 ÷ 512 = 2048 “blocos” em um cartão de memória. Assim como uma foto que é um byte menor (ou seja, 1.048.575 B)! O espaço desperdiçado no disco é chamado “espaço vago”. Investigadores forenses muitas vezes olham para os espaços vazios para restos de dados suspeitos.

A implicação de todos esses detalhes é que você, o investigador, provavelmente pode escrever um programa que itera sobre uma cópia do meu cartão de memória, procurando as assinaturas dos JPEGs. Cada vez que você encontrar uma assinatura, pode abrir um novo arquivo para gravar e começar a preenchê-lo com bytes do meu cartão de memória, fechando-o apenas quando encontrar outra assinatura. Além disso, em vez de ler os bytes do meu cartão de memória um por vez, você pode ler 512 de cada vez em um buffer para eficiência. Graças ao FAT, você pode confiar que as assinaturas dos JPEGs estarão “alinhadas em blocos”. Isso significa que você só precisa procurar essas assinaturas nos primeiros quatro bytes de um bloco.

Note que os JPEGs podem abranger blocos contíguos. Caso contrário, nenhum JPEG poderia ser maior que 512 B. Mas o último byte de um JPEG pode não cair no final de um bloco. Lembre-se da possibilidade de espaço vago. Mas não se preocupe. Como este cartão de memória era novo quando comecei a tirar fotos, é provável que tenha sido “zerado” (ou seja, preenchido com 0s) pelo fabricante, caso em que qualquer espaço vago será preenchido com 0s. Está tudo bem se esses 0s finais acabarem nos JPEGs que você recuperar; eles ainda devem ser visualizáveis.

Agora, eu tenho apenas um cartão de memória, mas há muitos de vocês! Então, eu criei uma “imagem forense” do cartão, armazenando seu conteúdo, byte a byte, em um arquivo chamado 'card.raw`. Para que você não perca tempo iterando sobre milhões de 0s desnecessariamente, eu apenas criei uma imagem dos primeiros megabytes do cartão de memória. Mas você deve encontrar que a imagem contém 50 JPEGs.

Começando
----

Acesse [code.cs50.io](https://code.cs50.io/), clique na janela do terminal e execute `cd` sozinho. Você deve encontrar que o seu prompt de janela do terminal se assemelha ao abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/4/recover.zip
    

para baixar um arquivo ZIP chamado `recover.zip` no seu espaço de código.

Agora, execute

    unzip recover.zip
    

para criar uma pasta chamada `recover`. Você não precisa mais do arquivo ZIP, então execute

    rm recover.zip
    

e responda com um “y” seguido de Enter para remover o arquivo ZIP que você baixou.

Agora digite

    cd recover
    

seguido de Enter para mover-se para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o seguinte:

    recuperar/ $
    

Execute `ls` sozinho e você deve ver dois arquivos: `recover.c` e 'cart.raw\`.


Especificação
-----

Implemente um programa chamado `recover` que recupera JPEGs de uma imagem forense.

* Implemente seu programa em um arquivo chamado `recover.c` em um diretório chamado `recover`.
* Seu programa deve aceitar exatamente um argumento de linha de comando, o nome de uma imagem forense da qual recuperar os JPEGs.
* Se o programa não for executado com exatamente um argumento de linha de comando, ele deve lembrar o usuário do uso correto e `main` deve retornar `1`.
* Se a imagem forense não puder ser aberta para leitura, o programa deve informar o usuário disso e `main` deve retornar `1`.
* Os arquivos que você gerar devem ser nomeados como `###.jpg`, onde `###` é um número decimal de três dígitos, começando com `000` para a primeira imagem e contando para cima.
* Se o seu programa usar `malloc`, não pode vazar memória.