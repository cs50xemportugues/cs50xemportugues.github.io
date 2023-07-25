# Olá

## Introdução

Lembre-se de que o Visual Studio Code (também conhecido como VS Code) é um popular "ambiente de desenvolvimento integrado" (IDE) através do qual é possível escrever código. Para que você não precise baixar, instalar e configurar sua própria cópia do VS Code, usaremos uma versão baseada em nuvem que já tem tudo o que você precisa pré-instalado.

Faça login em [code.cs50.io](https://code.cs50.io/) usando sua conta do GitHub. Assim que seu "código espacial" carregar, você deve ver que, por padrão, o VS Code é dividido em três regiões. Na parte superior do VS Code está o "editor de texto", onde você escreverá todos os seus programas. Na parte inferior está uma "janela do terminal", uma interface de linha de comando (CLI) que permite explorar os arquivos e diretórios (também chamados de pastas) do seu espaço de codificação, compilar código e executar programas. E à esquerda está o "explorador de arquivos", uma interface gráfica do usuário (GUI) por meio da qual você também pode explorar os arquivos e diretórios do seu espaço de codificação.

Comece clicando dentro da sua janela do terminal e execute `cd`. Você deve ver que seu "prompt" se parece com o abaixo.

    $

Clique dentro da janela do terminal e digite

    mkdir hello

seguido de Enter para criar um diretório chamado `hello` no seu espaço de codificação. Tome cuidado para não esquecer o espaço entre `mkdir` e `hello` ou qualquer outro caractere!

De agora em diante, executar um comando significa digitá-lo em uma janela do terminal e pressionar Enter. Os comandos são "sensíveis a maiúsculas e minúsculas", portanto, certifique-se de não digitar em maiúsculas quando deveria ser minúsculo ou vice-versa.

Agora execute

    cd hello

para mover-se para dentro desse diretório. Seu prompt deve agora se parecer com o abaixo.

    hello/ $

Se não, retorne e veja se pode determinar onde você errou!

Vamos escrever o seu primeiro programa? Execute

    code hello.c

para criar um novo arquivo chamado `hello.c`, que deve ser aberto automaticamente no editor de texto do seu espaço de codificação. Assim que você salvá-lo com o comando-S (no macOS) ou control-S (no Windows), ele também deverá aparecer no explorador do seu espaço de codificação.

Prossiga escrevendo seu primeiro programa digitando exatamente estas linhas em `hello.c`:

    #include <stdio.h>

    int main(void)
    {
        printf("hello, world\n");
    }

Observe como o VS Code adiciona "sintaxe de destaque" (ou seja, cor) à medida que você digita, embora a escolha de cores do VS Code possa ser diferente deste conjunto de problemas. Essas cores não são realmente salvas dentro do arquivo em si; elas são apenas adicionadas pelo VS Code para destacar certa sintaxe. Se você não tivesse salvado o arquivo como `hello.c` desde o início, o VS Code não saberia (por causa da extensão do nome do arquivo) que você está escrevendo código C, caso em que essas cores estariam ausentes.

## Listando arquivos

Agora, em sua janela do terminal, logo à direita do prompt (`hello/ $`), execute

    ls

Você só deve ver `hello.c`? Isso porque você acabou de listar os arquivos na sua pasta `hello`. Em particular, você executou um comando chamado `ls`, que é uma abreviação para "listar". (É um comando tão frequentemente usado que seus autores o chamaram apenas de `ls` para economizar teclas.) Faz sentido?

## Compilando programas

Agora, antes de podermos executar o programa `hello.c`, lembre-se de que precisamos _compilá-lo_ com um _compilador_, traduzindo-o do _código-fonte_ para o _código de máquina_ (ou seja, zeros e uns). Execute o comando abaixo para fazer isso:

    make hello

E então execute este novamente:

    ls

Desta vez, você não só deve ver `hello.c`, mas também `hello` listado? Você traduziu o código-fonte em `hello.c` para código de máquina em `hello`.

Execute o programa em si executando o abaixo.

    ./hello

Olá, mundo, de fato!

## Obtendo a entrada do usuário

Suficiente para dizer que, não importa como você compile ou execute este programa, ele sempre imprime apenas `hello, world`. Vamos personalizá-lo um pouco, como fizemos em sala de aula.

Modifique este programa de tal forma que ele primeiro solicite ao usuário seu nome e depois imprima `hello, fulano`, onde `fulano` é o nome real dele ou dela.

Como antes, certifique-se de compilar seu programa com:

    make hello

E certifique-se de executar seu programa, testando-o algumas vezes com entradas diferentes, com:

    ./hello

### Tutorial

Aqui está um "tutorial" (ou seja, uma visita guiada) deste problema, se você quiser uma visão geral verbal do que fazer também!

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/LvT8TjHHCRU?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Dicas

#### Não se lembra de como solicitar o nome do usuário?

Lembre-se de que você pode usar `get_string` da seguinte forma, armazenando seu _valor de retorno_ em uma variável chamada `name` do tipo `string`.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">string</span> <span class="n">name</span> <span class="o">=</span> <span class="n">get_string</span><span class="p">(</span><span class="s">"Qual é o seu nome? "</span><span class="p">);</span>
</code></pre></div></div>

#### Não se lembra de como formatar uma string?

Não se lembra de como juntar (ou seja, concatenar) o nome do usuário com uma saudação? Lembre-se de que você pode usar `printf` não apenas para imprimir, mas para formatar uma string (daí o `f` em `printf`), como em:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">printf</span><span class="p">(</span><span class="s">"hello, %s</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">name</span><span class="p">);</span>
</code></pre></div></div>

#### Uso de identificador não declarado?

Vendo o abaixo, talvez acima de outros erros?

    error: use of undeclared identifier 'string'; did you mean 'stdin'?

Lembre-se de que, para usar `get_string`, é necessário incluir `cs50.h` (onde `get_string` é _declarado_) no topo de um arquivo, como em:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">#include</span> <span class="cpf">&lt;cs50.h&gt;</span><span class="cp">
</span></code></pre></div></div>

### Como testar seu código

Execute o abaixo para avaliar a correção do seu código usando `check50`, um programa de linha de comando que produzirá faces felizes sempre que seu código passar nos testes automatizados do CS50 e faces tristes sempre que não passar! Mas certifique-se de compilá-lo e testá-lo você mesmo também!

    check50 cs50/problems/2023/x/hello

Execute o abaixo para avaliar o estilo do seu código usando `style50`, um programa de linha de comando que produz adições (em verde) e exclusões (em vermelho) que você deve fazer ao seu programa para melhorar seu estilo. Se você tiver problemas para ver essas cores, o `style50` suporta outros [modos](https://cs50.readthedocs.io/style50/) também!

    style50 hello.c

## Como Enviar

Em seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/hello