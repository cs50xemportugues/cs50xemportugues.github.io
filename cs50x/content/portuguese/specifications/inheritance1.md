Laboratório 5: Herança
==================

<div class="alert" data-alert="warning" role="alert"><p>Você pode colaborar com um ou dois colegas neste laboratório, embora seja esperado que todos os estudantes em tal grupo contribuam igualmente para o laboratório.</p></div>

Simule a herança dos tipos sanguíneos de cada membro de uma família.

    $ ./inheritance
    Criança (Geração 0): tipo sanguíneo OO
        Pai (Geração 1): tipo sanguíneo AO
            Avô (Geração 2): tipo sanguíneo OA
            Avó (Geração 2): tipo sanguíneo BO
        Pai (Geração 1): tipo sanguíneo OB
            Avô (Geração 2): tipo sanguíneo AO
            Avó (Geração 2): tipo sanguíneo BO
    
    

Contexto
----------

O tipo sanguíneo de uma pessoa é determinado por dois alelos (ou seja, diferentes formas de um gene). Os três alelos possíveis são A, B e O, dos quais cada pessoa tem dois (possivelmente iguais, possivelmente diferentes). Cada um dos pais de uma criança passa aleatoriamente um de seus dois alelos de tipo sanguíneo para a criança. As possíveis combinações de tipo sanguíneo são: OO, OA, OB, AO, AA, AB, BO, BA e BB.

Por exemplo, se um dos pais tem tipo sanguíneo AO e o outro tem tipo sanguíneo BB, então os possíveis tipos sanguíneos da criança seriam AB e OB, dependendo de qual alelo é recebido de cada pai. Da mesma forma, se um dos pais tem tipo sanguíneo AO e o outro OB, então os possíveis tipos sanguíneos da criança seriam AO, OB, AB e OO.

Iniciando
---------------

Abra o [VS Code] (https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e execute `cd` sozinho. Você deve encontrar que o "prompt" se parece com o abaixo.

    $
    

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/labs/5/inheritance.zip
    

seguido por Enter para baixar um ZIP chamado `inheritance.zip` em seu espaço de códigos. Cuidado para não ignorar o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere!

Agora execute

    unzip inheritance.zip
    

para criar uma pasta chamada `inheritance`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm inheritance.zip
    

e responda com “y” seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd inheritance
    

seguido de Enter para mover-se para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    inheritance/ $
    

Se tudo correu bem, você deve executar

    ls
    

e deve ver `inheritance.c`.

Se você encontrar algum problema, siga essas mesmas etapas novamente e veja se pode determinar onde errou!

Entendendo
-------------

Dê uma olhada no código distribuído em `inheritance.c`.

Observe a definição de um tipo chamado `person`. Cada pessoa tem um array de dois `parents`, cada um dos quais é um ponteiro para outra estrutura `person`. Cada pessoa também tem um array de dois `alleles`, cada um dos quais é um `char` (ou `'A'`, `'B'` ou `'O'`).

Agora, dê uma olhada na função`main`. A função começa por "seeding" (ou seja, fornecendo alguma entrada inicial para) um gerador de números aleatórios, que usaremos mais tarde para gerar alelos aleatórios. A função `main`, então, chama a função `create_family` para simular a criação de structs `person` para uma família de três gerações (ou seja, uma pessoa, seus pais e seus avós). Nós, então, chamamos `print_family` para imprimir cada um desses membros da família e seus tipos sanguíneos. Finalmente, a função chama `free_family` para `liberar` qualquer memória que tenha sido previamente alocada com `malloc`.

As funções `create_family` e `free_family` são deixadas a você para escrever!