Plurality
=========

Para este programa, você implementará um programa que executa uma eleição de maioria, como abaixo.

    $ ./plurality Alice Bob Charlie
    Número de eleitores: 4
    Voto: Alice
    Voto: Bob
    Voto: Charlie
    Voto: Alice
    Alice
    

Contexto
----------

Eleições vêm em todos os tipos e tamanhos. No Reino Unido, o [Primeiro-Ministro](https://www.parliament.uk/education/about-your-parliament/general-elections/) é oficialmente nomeado pelo monarca, que geralmente escolhe o líder do partido político que ganhou a maioria dos assentos na Câmara dos Comuns. Os Estados Unidos usam um processo de [colégio eleitoral](https://www.archives.gov/federal-register/electoral-college/about.html) multi-etapas em que os cidadãos votam em como cada estado deve distribuir os eleitores que em seguida elegem o presidente.

Talvez a forma mais simples de se realizar uma eleição seja através de um método conhecido como “voto de maioria” (ou primeiro-past-the-post ou winner take all). No voto de maioria, cada eleitor recebe um voto para um candidato. No final da eleição, o candidato com o maior número de votos é declarado o vencedor da eleição.

Começando
---------------

Acesse o [code.cs50.io](https://code.cs50.io/), clique na sua janela de terminal e execute o comando `cd` para verificar. Você deve verificar que o prompt da sua janela de terminal se parece com o abaixo:

    $
    

Em seguida, execute o comando

    wget https://cdn.cs50.net/2022/fall/psets/3/plurality.zip
    

para baixar um arquivo ZIP chamado `plurality.zip` para o seu espaço de códigos.

Em seguida, execute

    unzip plurality.zip
    

para extrair um diretório chamado `plurality`. O arquivo ZIP não será mais necessário. Execute

    rm plurality.zip
    

e responda com “y” seguido de Enter na solicitação para remover o arquivo ZIP que você baixou.

Em seguida, digite

    cd plurality
    

seguido de Enter para mover-se para o diretório. Seu prompt agora deve ser semelhante ao abaixo.

    plurality/ $
    

Se tudo foi bem-sucedido, você deve digitar

    ls
    

e ver um arquivo chamado `plurality.c`. Executar o comando `code plurality.c` deve abrir o arquivo onde você irá digitar o código para este problema. Caso contrário, reveja seus passos e veja se consegue descobrir onde errou!

Compreensão
-------------

Examine `plurality.c` e leia o código distribuído que foi fornecido.

A linha `#define MAX 9` é uma sintaxe usada aqui para significar que `MAX` é uma constante (igual a `9`) que pode ser usada em todo o programa. Aqui, representa o número máximo de candidatos que uma eleição pode ter.

O arquivo define então uma `struct` chamada `candidate`. Cada “candidate” tem dois campos: um `string` chamado `name` representando o nome do candidato e um `int` chamado `votes`, que representa o número de votos que o candidato possui. Em seguida, o arquivo define um array global de `candidates`, em que cada elemento é ele mesmo um `candidate`.

Agora, dê uma olhada na própria função `main`. Veja se você consegue encontrar onde o programa define uma variável global `candidate_count` representando o número de candidatos na eleição, copia argumentos da linha de comando para o array `candidates` e pede ao usuário para digitar o número de eleitores. Em seguida, o programa permite que cada eleitor vote (veja como?), chamando a função `vote` em cada candidato votado. Finalmente, a função `main` chama a função `print_winner` para imprimir o vencedor (ou vencedores) da eleição.

Mas se você olhar mais abaixo no arquivo, perceberá que as funções `vote` e `print_winner` foram deixadas em branco. Essa parte cabe a você concluir!

Especificação
-------------

Conclua a implementação de `plurality.c` de tal maneira que o programa simule uma eleição de maioria.

*   Conclua a função `vote`.
    *   `vote` recebe um único argumento, uma `string` chamada `name`, que representa o nome do candidato que recebeu o voto.
    *   Se `name` corresponder a um dos nomes dos candidatos na eleição, atualize o total de votos desse candidato para incluir o novo voto. A função `vote`, nesse caso, deve retornar `true` para indicar uma cédula bem-sucedida.
    *   Se `name` não corresponder ao nome de nenhum dos candidatos na eleição, nenhuma contagem de votos deve ser ajustada, e a função `vote` deve retornar `false` para indicar uma cédula inválida.
    *   Você pode assumir que nenhum dois candidatos terão o mesmo nome.
*   Conclua a função `print_winner`.
    *   A função deve imprimir o nome do candidato que recebeu a maioria dos votos na eleição e, em seguida, imprimir uma nova linha.
    *   É possível que a eleição possa terminar empatada se vários candidatos tiverem o mesmo número máximo de votos. Nesse caso, você deve imprimir os nomes de cada um dos candidatos vencedores, cada um em uma linha separada.

Você não deve modificar mais nada em `plurality.c` que não seja as implementações das funções `vote` e `print_winner` (e a inclusão de arquivos de cabeçalho adicionais, se desejar).

Utilização
-----

Seu programa deve se comportar conforme os exemplos abaixo.

    $ ./plurality Alice Bob
    Número de eleitores: 3
    Voto: Alice
    Voto: Bob
    Voto: Alice
    Alice
    

    $ ./plurality Alice Bob
    Número de eleitores: 3
    Voto: Alice
    Voto: Charlie
    Voto inválido.
    Voto: Alice
    Alice
    

    $ ./plurality Alice Bob Charlie
    Número de eleitores: 5
    Voto: Alice
    Voto: Charlie
    Voto: Bob
    Voto: Bob
    Voto: Alice
    Alice
    Bob
    

Passo a Passo
-----------


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ftOapzDjEb8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Teste
-------

Certifique-se de testar seu código para se certificar de que ele lida com...

*   Uma eleição com qualquer número de candidatos (até o `MAX` de` 9`)
*   Votação em um candidato pelo nome
*   Votos inválidos para candidatos que não estão na cédula
*   Imprimir o vencedor da eleição se houver apenas um
*   Imprimir o vencedor da eleição se houver vários vencedores

Execute o seguinte para avaliar a correção do seu código usando o `check50`. Mas certifique-se de compilá-lo e testá-lo sozinho também!

    check50 cs50/problems/2023/x/plurality
    

Execute o seguinte para avaliar o estilo do seu código usando o `style50`.

    style50 plurality.c
    

Como Enviar
-------------

Em seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2023/x/plurality