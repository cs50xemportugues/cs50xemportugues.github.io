# Lab 1: Crescimento Populacional

<div class="alert" data-alert="warning" role="alert"><p>Você pode colaborar com um ou dois colegas nesta prática, porém espera-se igual contribuição de todos os alunos envolvidos.</p></div>

Determinar quanto tempo leva para uma população atingir um tamanho particular.

    $ ./population
    Tamanho inicial da população: 100
    Tamanho final da população: 200
    Anos: 9

## Contexto

Digamos que há uma população de `n` lhamas. A cada ano, `n / 3` novas lhamas nascem e `n / 4` lhamas morrem.

Por exemplo, se começarmos com `n = 1200` lhamas, então no primeiro ano, `1200 / 3 = 400` novas lhamas nasceriam e `1200 / 4 = 300` lhamas morreriam. Ao final daquele ano, teríamos `1200 + 400 - 300 = 1300` lhamas.

Para outro exemplo, se começarmos com `n = 1000` lhamas, ao final do ano, teríamos `1000 / 3 = 333,33` novas lhamas. Como não se pode ter uma fração de uma lhama, iremos arredondar o número de lhamas para baixo e teríamos `333` novas lhamas nascidas. `1000 / 4 = 250` lhamas morreriam, então teríamos um total de `1000 + 333 - 250 = 1083` lhamas ao final do ano.

## Como Começar

Lembre-se de que o Visual Studio Code, ou VS Code, é um popular "ambiente integrado de desenvolvimento" (IDE) no qual se pode escrever código. Para não ser necessário baixar, instalar e configurar o próprio VS Code, utilizaremos uma versão baseada em nuvem que já tem tudo o que precisa pré-instalado.

1. Faça login na plataforma [code.cs50.io](https://code.cs50.io/) usando a sua conta do GitHub e siga as instruções na tela para configurar o seu próprio “codespace” para o Visual Studio Code. Uma vez carregado o seu codespace, você verá que o VS Code é dividido por default em três regiões. Na parte superior do VS Code está o “editor de texto”, no qual você escreverá todos os seus programas. Na parte inferior está a “janela de terminal”, que é a interface de linha de comando (CLI) que permite explorar os arquivos e diretórios (também conhecidos como pastas) do seu codespace, compilar o código e executar programas. E à esquerda está o explorador de arquivos, que é uma interface gráfica do usuário (GUI) por meio da qual também se pode explorar os arquivos e diretórios do your codespace.
2. Uma vez que o seu codespace tenha carregado, feche todas as guias de **Boas-vindas** que possam ter sido abertas por default.
3. Faça login na plataforma [submit.cs50.io](https://submit.cs50.io) usando a sua conta do GitHub e clique em **Authorize cs50** para ativar o `check50`.
4. Execute o comando `update50` na janela do terminal do seu codespace para garantir que a ferramenta esteja atualizada e, se solicitado, clique em **Rebuild now**.

Depois de concluído, comece clicando dentro da janela do terminal e execute o comando `cd`. Você verá que o "prompt" é parecido com o seguinte.

$

Clique dentro da janela do terminal e digite

    mkdir population

seguido de Enter para criar um diretório chamado `population` no seu codespace. Tome cuidado para não ignorar o espaço entre `mkdir` e `population`, nem nenhum outro caractere.

A partir de agora, executar (ou seja, rodar) um comando significa escrever o comando em uma janela do terminal e pressionar Enter. Os comandos diferenciam maiúsculas de minúsculas, portanto, tenha certeza de não escrever em maiúscula quando quiser minúscula e vice-versa.

Execute agora

    cd population

para se mover para dentro (ou seja, abrir) esse diretório. O prompt agora deve se parecer com o seguinte.

    population/ $

Clique dentro da janela do terminal e digite

    wget https://cdn.cs50.net/2022/fall/labs/1/population.c

seguido de Enter para baixar um arquivo modelo chamado `population.c` no seu codespace. Tome cuidado para não ignorar o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere. Se tudo ocorrer bem, execute

    ls

e verifique se há um arquivo chamado `population.c`. Executar `code population.c` deve abrir o arquivo que você usará para digitar seu código nesta prática. Se isso não acontecer, volte e confira se você seguiu os passos corretamente.

## Detalhes da Implementação

Complete a implementação do `population.c`, para que ele calcule o número de anos necessários para que a população cresça do tamanho inicial para o tamanho final.

- Seu programa deve primeiro solicitar ao usuário um tamanho de população de início.
  - Se o usuário inserir um número menor que 9 (o tamanho populacional mínimo permitido), o usuário deve ser solicitado novamente a inserir um tamanho inicial populacional até que seja inserido um número maior ou igual a 9. (Se começarmos com menos de 9 lhamas, a população estagnar rapidamente!)
- Seu programa deve, então, solicitar ao usuário um tamanho de população final.
  - Se o usuário inserir um número menor do que o tamanho de população inicial, o usuário deve ser solicitado novamente a inserir um tamanho de população final até que seja inserido um número que seja maior ou igual ao tamanho de população inicial. (Afinal, queremos que a população de lhamas cresça!)
- Seu programa deve então calcular o número (inteiro) de anos necessários para que a população atinja pelo menos o tamanho desejado.
- Finalmente, seu programa deve imprimir o número de anos necessários para que a população de lhamas atinja o tamanho desejado, digitando no terminal `Anos: n`, onde `n` representa o número de anos.

### Passo a Passo

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/dZmtRHHUB1M"></iframe>

### Dicas

- Se você deseja re-pedir repetidamente ao usuário o valor de uma variável até que alguma condição seja atendida, pode ser útil usar um loop `do… while`. Por exemplo, relembre o seguinte código da aula, que solicita o usuário repetidamente até que ele digite um número inteiro positivo. <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">n</span><span class="p">;</span>
  <span class="k">do</span>
  <span class="p">{</span>
  <span class="n">n</span> <span class="o">=</span> <span class="n">get_int</span><span class="p">(</span><span class="s">"Positive Integer: "</span><span class="p">);</span>
  <span class="p">}</span>
  <span class="k">while</span> <span class="p">(</span><span class="n">n</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">);</span>
  </code></pre></div> </div>
  Como você pode adaptar este código para garantir um tamanho inicial de pelo menos 9 e um tamanho final de pelo menos o tamanho inicial?

* Para declarar uma nova variável, certifique-se de especificar seu tipo de dados, um nome para a variável e (opcionalmente) qual deve ser seu valor inicial.
  - Por exemplo, você pode querer criar uma variável para acompanhar quantos anos se passaram.
* Para calcular quantos anos levará para a população atingir o tamanho final, outro loop pode ser útil! Dentro do loop, você provavelmente desejará atualizar o tamanho da população de acordo com a fórmula no Contexto e atualizar o número de anos que se passaram.
* Para imprimir um inteiro `n` no terminal, lembre-se de que você pode usar uma linha de código como <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code> <span class="n">printf</span><span class="p">(</span><span class="s">"The number is %i</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">n</span><span class="p">);</span>
  </code></pre></div> </div>
  para especificar que a variável `n` deve ser preenchida no espaço reservado `% i`.

### Como testar seu código

Seu programa deve se comportar de acordo com os exemplos abaixo.

    $ ./population
    Tamanho inicial: 1200
    Tamanho final: 1300
    Anos: 1


    $ ./population
    Tamanho inicial: -5
    Tamanho inicial: 3
    Tamanho inicial: 9
    Tamanho final: 5
    Tamanho final: 18
    Anos: 8


    $ ./population
    Tamanho inicial: 20
    Tamanho final: 1
    Tamanho final: 10
    Tamanho final: 100
    Anos: 20


    $ ./population
    Tamanho inicial: 100
    Tamanho final: 1000000
    Anos: 115

<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/2CcqQnLbGOE"></iframe></details>

Execute o seguinte para avaliar a correção do código usando o `check50`. Mas verifique se você compilou e testou o código também!

    check50 cs50/labs/2023/x/population

Execute o seguinte para avaliar o estilo do código usando o `style50`.

    style50 population.c

## Como Enviar

No terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/labs/2023/x/population


