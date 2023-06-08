Detalhes da Implementação
-------------------------

Complete a implementação do arquivo `inheritance.c`, para criar uma família de tamanho especificado e atribuir alelos de tipo sanguíneo a cada membro da família. A geração mais velha terá alelos atribuídos aleatoriamente a eles.

* A função `create_family` recebe um inteiro (`generations`) como entrada e deve alocar (por meio de `malloc`) uma `person` para cada membro da família desse número de gerações, retornando um ponteiro para a `person` na geração mais nova.
    * Por exemplo, `create_family(3)` deve retornar um ponteiro para uma pessoa com dois pais, onde cada pai também tem dois pais.
    * Cada `person` deve ter `alleles` atribuídos a eles. A geração mais velha deve ter alelos escolhidos aleatoriamente (por meio da função `random_allele`), e gerações mais jovens devem herdar um alelo (escolhido aleatoriamente) de cada pai.
    * Cada `person` deve ter `parents` atribuídos a eles. A geração mais velha deve ter ambos os `parents` definidos como `NULL`, e gerações mais jovens devem ter `parents` sendo uma matriz de dois ponteiros, cada um apontando para um pai diferente.

Dividimos a função `create_family` em alguns `TODO`s para você completar.

* Primeiro, você deve alocar memória para uma nova pessoa. Lembre-se de que você pode usar `malloc` para alocar memória e `sizeof(person)` para obter o número de bytes para alocar.
* Em seguida, incluímos uma condição para verificar se `generations > 1`.
    * Se `generations > 1`, há mais gerações que ainda precisam ser alocadas. Já criamos dois novos `parents`, `parent0` e `parent1`, chamando `create_family` recursivamente. Sua função `create_family` deve definir os ponteiros dos pais da nova pessoa que você criou. Finalmente, atribua ambos os `alleles` para a nova pessoa escolhendo aleatoriamente um alelo de cada pai.
    * Caso contrário (se `generations == 1`), não haverá dados dos pais para essa pessoa. Ambos `parents` de sua nova pessoa devem ser definidos como `NULL`, e cada `allele` deve ser gerado aleatoriamente.
* Finalmente, sua função deve retornar um ponteiro para a `person` que foi alocada.

A função `free_family` deve aceitar como entrada um ponteiro para uma `person`, desalocar a memória dessa pessoa e, em seguida, desalocar recursivamente a memória de todos os seus ancestrais.

* Como essa é uma função recursiva, você deve lidar primeiro com o caso base. Se a entrada para a função for `NULL`, nada precisa ser desalocado, então sua função pode retornar imediatamente.
* Caso contrário, você deve desalocar recursivamente ambos os pais da pessoa antes de desalocar a criança.

### Tutorial

<div class="alert" data-alert="primary" role="alert"><p>Este vídeo foi gravado quando o curso ainda usava o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu codespace, o comportamento dos dois ambientes deve ser semelhante!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/9p7ddI3ozTY"></iframe>


### Dicas

* Você pode achar a função `rand()` útil para atribuir alelos aleatoriamente. Esta função retorna um inteiro entre `0` e `RAND_MAX`, ou `2147483647`.
    * Em particular, para gerar um número pseudoaleatório que é `0` ou `1`, você pode usar a expressão `rand() % 2`.
* Lembre-se de que, para alocar memória para uma pessoa específica, podemos usar `malloc(n)`, que leva um tamanho como argumento e alocará `n` bytes de memória.
* Lembre-se de que, para acessar uma variável por meio de um ponteiro, podemos usar a notação de seta.
    * Por exemplo, se `p` for um ponteiro para uma pessoa, então um ponteiro para o primeiro pai deste pessoa pode ser acessado por `p->parents[0]`.

<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/H7LULatPwcQ"></iframe></details>


### Como Testar Seu Código

Ao executar `./inheritance`, seu programa deve aderir às regras descritas no background. A criança deve ter dois alelos, um de cada pai. Os pais devem ter dois alelos, um de cada um de seus pais.

Por exemplo, no exemplo abaixo, a criança na Geração 0 recebeu um alelo O de ambos os pais da Geração 1. O primeiro pai recebeu um A do primeiro avô e um O do segundo avô. Da mesma forma, o segundo pai recebeu um O e um B de seus avós.

   ```
$ ./inheritance
    Criança (geração 0): tipo sanguíneo OO
        Pai (geração 1): tipo sanguíneo AO
            Avô (geração 2): tipo sanguíneo OA
            Avô (geração 2): tipo sanguíneo BO
        Pai (geração 1): tipo sanguíneo OB
            Avô (geração 2): tipo sanguíneo AO
            Avô (geração 2): tipo sanguíneo BO
   ```

Execute o comando abaixo para avaliar a correção do seu código usando `check50`. Mas lembre-se de compilar e testá-lo também!

    `check50 cs50/labs/2023/x/inheritance`

Execute o comando abaixo para avaliar o estilo do seu código usando `style50`.

    `style50 inheritance.c`

Como Enviar o Trabalho
-------------------------

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    `submit50 cs50/labs/2023/x/inheritance`