Página Inicial
=========

Crie uma página inicial simples usando HTML, CSS e JavaScript.

Contexto
----------

A internet permitiu coisas incríveis: podemos usar um mecanismo de busca para pesquisar qualquer coisa imaginável, comunicar com amigos e familiares em todo o mundo, jogar, fazer cursos e muito mais. Mas percebe-se que quase todas as páginas que visitamos foram construídas em três idiomas fundamentais, cada um com um objetivo ligeiramente diferente:

1. HTML, ou _Linguagem de Marcação de Hipertexto_, é usada para descrever o conteúdo de sites;
2. CSS, _Folhas de Estilo em Cascata_, é usada para descrever a estética dos sites; e
3. JavaScript, usado para tornar sites interativos e dinâmicos.

Crie uma página inicial simples que apresente você, seu hobby favorito ou atividade extracurricular, ou qualquer outra coisa de seu interesse.

Introdução
---------------

Faça login em [code.cs50.io] (https://code.cs50.io/), clique na janela do terminal e execute `cd` sozinho. Você deve encontrar que o prompt da sua janela do terminal se parece com o abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/8/homepage.zip
    

para baixar um arquivo ZIP chamado `homepage.zip` em seu espaço de código.

Em seguida, execute

    unzip homepage.zip
    

para criar uma pasta chamada `homepage`. Você não precisa mais do arquivo ZIP, então execute

    rm homepage.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd homepage
    

seguido de Enter para entrar (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    homepage/ $
    

Execute `ls` sozinho e você deverá ver alguns arquivos:

    index.html  styles.css
    

Se você tiver problemas, siga novamente essas etapas e veja se pode determinar onde errou! Você pode iniciar imediatamente um servidor para visualizar seu site executando

    http-server
    

na janela do terminal. Em seguida, clique com o botão de comando (se estiver no Mac) ou com o botão de controle (se estiver no PC) no primeiro link que aparece:

    http-server running on LINK
    

Onde LINK é o endereço do seu servidor.