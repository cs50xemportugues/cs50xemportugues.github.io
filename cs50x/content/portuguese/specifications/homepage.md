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

Especificação
-------------

Implemente no diretório `homepage` um site que deve:

*   Conter pelo menos quatro páginas `.html` diferentes, sendo uma delas `index.html` (a página principal do seu site), e deve ser possível ir de qualquer página do seu site para qualquer outra página seguindo um ou mais hiperlinks.
*   Usar pelo menos dez (10) tags HTML distintas além de `<html>`, `<head>`, `<body>` e `<title>`. Usar alguma tag (por exemplo, `<p>`) várias vezes ainda conta como apenas uma (1) das dez!
*   Integrar uma ou mais funcionalidades do Bootstrap em seu site. Bootstrap é uma biblioteca popular (que vem com muitas classes CSS e mais) através da qual você pode embelezar seu site. Consulte [a documentação do Bootstrap](https://getbootstrap.com/docs/5.2/) para começar. Em particular, você pode achar alguns [componentes do Bootstrap](https://getbootstrap.com/docs/5.2/components/) interessantes. Para adicionar o Bootstrap ao seu site, é suficiente incluir <div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"stylesheet"</span> <span class="na">href=</span><span class="s">"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"</span> <span class="na">integrity=</span><span class="s">"sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;</span>
<span class="nt">&lt;script </span><span class="na">src=</span><span class="s">"https://code.jquery.com/jquery-3.5.1.slim.min.js"</span> <span class="na">integrity=</span><span class="s">"sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;&lt;/script&gt;</span>
<span class="nt">&lt;script </span><span class="na">src=</span><span class="s">"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"</span> <span class="na">integrity=</span><span class="s">"sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;&lt;/script&gt;</span>
</code></pre></div></div> em `<head>` de suas páginas, abaixo da qual você também pode incluir <div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;link</span> <span class="na">href=</span><span class="s">"styles.css"</span> <span class="na">rel=</span><span class="s">"stylesheet"</span><span class="nt">&gt;</span>
</code></pre></div>    </div>
      
    
    para vincular seu próprio CSS.
    
*   Ter pelo menos um arquivo de folha de estilo de sua própria criação, `styles.css`, que usa pelo menos cinco (5) seletores CSS diferentes (por exemplo, tag (`example`), classe (`.example`), ou ID (`#example`)), e dentro dele usar um total de pelo menos cinco (5) propriedades CSS diferentes, como `font-size` ou `margin`; e
*   Integrar uma ou mais funcionalidades do JavaScript em seu site para torná-lo mais interativo. Por exemplo, você pode usar JavaScript para adicionar alertas, ter um efeito em intervalos recorrentes ou adicionar interatividade a botões, menus suspensos ou formulários. Fique à vontade para ser criativo!
*   Certifique-se de que seu site fique agradável nos navegadores tanto em dispositivos móveis quanto em laptops e desktops.

Teste
-----

Se você quiser ver como seu site está enquanto você trabalha, você pode executar `http-server`. Clique com o botão direito ou controle no primeiro link apresentado pelo http-server, que deve abrir sua página da web em uma nova guia. Então, você deve ser capaz de atualizar a guia que contém sua página da web para ver suas últimas alterações.

Lembre também que, abrindo as Ferramentas de Desenvolvedor no Google Chrome, você pode _simular_ a visita à sua página em um dispositivo móvel clicando no ícone em forma de telefone à esquerda de **Elementos** na janela das ferramentas de desenvolvedor, ou, uma vez que a guia Ferramentas do desenvolvedor já esteja aberta, digitando `Ctrl`+`Shift`+`M` em um PC ou `Cmd`+`Shift`+`M` em um Mac, em vez de precisar visitar o site em um dispositivo móvel separadamente!

Avaliação
---------

Não há `check50` para esta tarefa! Em vez disso, a correção do seu site será avaliada com base em se você atende aos requisitos especificados acima e se seu HTML está bem formado e é válido. Para garantir que suas páginas estejam, você pode usar este [Markup Validation Service](https://validator.w3.org/#validate_by_input), copiando e colando seu HTML diretamente na caixa de texto fornecida. Tenha cuidado para eliminar quaisquer avisos ou erros sugeridos pelo validador antes de enviar!

Considere também:

*   se a estética do seu site é tal que ele é intuitivo e simples para um usuário navegar;
*   se seu CSS foi definido em arquivos CSS separados; e
*   se você evitou repetição e redundância, "cascateando" propriedades de estilo de tags pai.

Infelizmente, `style50` não suporta arquivos HTML, portanto, é incumbido que você indente e alinhe suas tags HTML de forma limpa. Saiba também que você pode criar um comentário HTML com:

    <!-- Comentário aqui -->

Mas comentar seu código HTML não é tão imperativo como é quando se comenta o código em C ou Python, por exemplo. Você também pode comentar seu CSS, em arquivos CSS, com:

    /* Comentário aqui */
    

Dicas
-----

Para guias bastante abrangentes sobre as linguagens apresentadas neste problema, confira estes tutoriais:

*   [HTML](https://www.w3schools.com/html/)
*   [CSS](https://www.w3schools.com/css/)
*   [JavaScript](https://www.w3schools.com/js/)

Como enviar
-----------

No terminal, execute o código abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/homepage"

