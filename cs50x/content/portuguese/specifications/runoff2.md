Começando
---------------

Faça login no [code.cs50.io] (https://code.cs50.io/), clique na janela do terminal e execute `cd` por si só. Você deve ver que o prompt da janela do terminal se parece com o abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/3/runoff.zip
    

para baixar um ZIP chamado `runoff.zip` em seu espaço de código.

Em seguida, execute

    unzip runoff.zip
    

para criar uma pasta chamada `runoff`. Você não precisa mais do arquivo ZIP, portanto, execute

    rm runoff.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd runoff
    

seguido de Enter para se mover para (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    runoff/ $
    

Se tudo ocorreu conforme o esperado, você deve executar

    ls
    

e ver um arquivo chamado `runoff.c`. A execução de `code runoff.c` deve abrir o arquivo onde você digitará seu código para este problema definido. Caso contrário, volte seus passos e veja se pode determinar onde saiu errado!

Entendendo
-------------

Vamos dar uma olhada em `runoff.c`. Estamos definindo duas constantes: `MAX_CANDIDATES` para o número máximo de candidatos na eleição e `MAX_VOTERS` para o número máximo de eleitores na eleição.

Em seguida, temos uma matriz bidimensional `preferences`. A matriz `preferences [i]` representará todas as preferências para o eleitor número `i` e o número inteiro `preferences [i] [j]` aqui armazenará o índice do candidato que é a j-ésima preferência para o eleitor 'i'.

Em seguida, temos uma `struct` chamada `candidate`. Cada `candidate` tem um campo de `string` para o seu `nome`, e um `int` representando o número de `votes` que eles têm no momento, e um valor `bool` chamado `eliminated` que indica se o candidato foi eliminado da eleição. A matriz `candidates` acompanhará todos os candidatos na eleição.

O programa também tem duas variáveis globais: `voter_count` e `candidate_count`.

Agora no `main`. Observe que, após determinar o número de candidatos e o número de eleitores, o loop de votação principal começa, dando a cada eleitor uma chance de votar. À medida que o eleitor insere suas preferências, a função `vote` é chamada para acompanhar todas as preferências. Se em algum momento a cédula for considerada inválida, o programa é encerrado.

Depois que todas as votos forem feitas, outro loop começa: este vai manter a repetição do processo de votação até que haja um vencedor, verificando o último candidato.

A primeira chamada aqui é para uma função chamada `tabulate`, que deve procurar todas as preferências dos eleitores e calcular os totais de votos atuais, verificando o candidato da escolha principal de cada eleitor que ainda não foi eliminado. Em seguida, a função `print_winner` deve imprimir o vencedor, se houver um; se houver, o programa acabou. Mas caso contrário, o programa precisa determinar o menor número de votos que qualquer pessoa ainda na eleição recebeu (por meio da chamada à função `find_min`). Se for descoberto que todas as pessoas na eleição empataram com o mesmo número de votos (como determinado pela função `is_tie`), a eleição é declarada um empate; caso contrário, o candidato (ou candidatos) em último lugar é eliminado da eleição por meio de uma chamada à função `eliminate`.

Se você olhar um pouco mais abaixo no arquivo, verá que essas funções - `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` e `eliminate` - ficam todas a seu cargo para serem concluídas!