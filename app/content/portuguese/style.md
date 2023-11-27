# Guia de Estilo para C

Não há uma única maneira correta de estilizar o código. Mas definitivamente existem muitas maneiras erradas (ou, pelo menos, ruins). Mesmo assim, o CS50 pede que você siga as convenções abaixo para que possamos analisar de forma confiável o estilo do seu código. Da mesma forma, as empresas normalmente adotam suas próprias convenções corporativas para o estilo.

## Comprimento da Linha

Por convenção, o comprimento máximo de uma linha de código em C é de 80 caracteres, o que está historicamente fundamentado em monitores de tamanho padrão em terminais de computadores mais antigos, que podiam exibir 24 linhas verticalmente e 80 caracteres horizontalmente. Embora a tecnologia moderna tenha tornado obsoleta a necessidade de manter linhas limitadas a 80 caracteres, ainda é uma diretriz que deve ser considerada um "limite flexível", e uma linha de 100 caracteres deve ser realmente a mais longa que você escreve em C, caso contrário, os leitores geralmente precisarão rolar. Se você precisar de mais de 100 caracteres, pode ser hora de repensar os nomes de suas variáveis ou o design geral!

    // As próximas linhas de código primeiro solicitam ao usuário que forneça dois valores inteiros e, em seguida, multiplicam esses dois valores inteiros juntos para que possam ser usados mais tarde no programa
    int primeiro_valor_inteiro_coletado_do_usuario = get_int("Digite um número inteiro: ");
    int segundo_valor_inteiro_coletado_do_usuario = get_int("Mais um número inteiro, por favor: ");
    int produto_dos_dois_valores_inteiros_do_usuario = primeiro_valor_inteiro_coletado_do_usuario * segundo_valor_inteiro_coletado_do_usuario;

Em outras linguagens, especialmente JavaScript, é significativamente mais difícil restringir as linhas a um comprimento máximo; lá, seu objetivo deve ser quebrar as linhas (como via `\n`) em locais que maximizem a legibilidade e a clareza.

## Comentários

Os comentários tornam o código mais legível, não apenas para os outros (por exemplo, seu TF), mas também para você, especialmente quando horas, dias, semanas, meses ou anos passam entre a escrita e a leitura do seu próprio código. Comentar muito pouco é ruim. Comentar demais é ruim. Qual é o ponto ideal? Comentar a cada poucas linhas de código (ou seja, blocos interessantes) é uma diretriz razoável. Tente escrever comentários que respondam a uma ou ambas estas perguntas:

1. O que este bloco faz?
2. Por que implementei este bloco desta forma?

Dentro das funções, use "comentários embutidos" e mantenha-os curtos (por exemplo, uma linha), caso contrário, fica difícil distinguir os comentários do código, mesmo com realce de sintaxe. Coloque o comentário acima da(s) linha(s) a que se aplica. Não é necessário escrever frases completas, mas faça a primeira palavra do comentário em maiúsculas (a menos que seja o nome de uma função, variável ou similar) e deixe um espaço entre `//` e o primeiro caractere do seu comentário, como em:

    // Converter Fahrenheit para Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

Em outras palavras, não faça isso:

    //Converter Fahrenheit para Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

Ou isso:

    // converter Fahrenheit para Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

Ou isso:

    float c = 5.0 / 9.0 * (f - 32.0); // Converter Fahrenheit para Celsius

No topo de seus arquivos .c e .h, deve haver um comentário que resuma o que seu programa (ou aquele arquivo específico) faz, como em:

    // Diz olá para o mundo

No topo de cada uma de suas funções (exceto, talvez, `main`), deve haver um comentário que resuma o que sua função está fazendo, como em:

    // Retorna o quadrado de n
    int quadrado(int n)
    {
        return n * n;
    }

## Cabeçalhos de Biblioteca

Quaisquer cabeçalhos de biblioteca que você incluir devem ser listados em ordem alfabética, como em:

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

Isso facilita a visualização rápida, especialmente em uma lista longa, se você incluiu um cabeçalho.

## Condições

As condições devem ser estilizadas da seguinte forma:

    if (x > 0)
    {
        printf("x é positivo\n");
    }
    else if (x < 0)
    {
        printf("x é negativo\n");
    }
    else
    {
        printf("x é zero\n");
    }

Note como:

- as chaves se alinham bem, cada uma em sua própria linha, tornando perfeitamente claro o que está dentro do bloco;
- há um único espaço após cada `if`;
- cada chamada para `printf` é recuada com 4 espaços;
- existem espaços simples ao redor do `>` e ao redor do `<`; e
- não há espaço imediatamente após cada `(` ou imediatamente antes de cada `)`.

Para economizar espaço, alguns programadores gostam de manter a primeira chave na mesma linha que a própria condição, mas não recomendamos, pois é mais difícil de ler, então não faça isso:

    if (x < 0) {
        printf("x é negativo\n");
    } else if (x < 0) {
        printf("x é negativo\n");
    }

E definitivamente não faça isso:

    if (x < 0)
        {
        printf("x é negativo\n");
        }
    else
        {
        printf("x é negativo\n");
        }

## Switches

Declare um `switch` da seguinte forma:

    switch (n)
    {
        case -1:
            printf("n é -1\n");
            break;

        case 1:
            printf("n é 1\n");
            break;

        default:
            printf("n não é nem -1 nem 1\n");
            break;
    }

Observe como:

- cada chave é colocada em sua própria linha;
- há um único espaço após `switch`;
- não há espaço imediatamente após cada `(` ou imediatamente antes de cada `)`;
- os casos do `switch` são indentados com 4 espaços;
- os corpos dos casos são indentados ainda mais com 4 espaços; e
- cada `case` (incluindo o `default`) termina com um `break`.

## Funções

De acordo com [C99](http://en.wikipedia.org/wiki/C99), certifique-se de declarar `main` da seguinte forma:

    int main(void)
    {

    }

ou, se estiver usando a Biblioteca CS50, com:

    #include <cs50.h>

    int main(int argc, string argv[])
    {

    }

ou com:

    int main(int argc, char *argv[])
    {

    }

ou até com:

    int main(int argc, char **argv)
    {

    }

Não declare `main` desta forma:

    int main()
    {

    }

ou assim:

    void main()
    {

    }

ou assim:

    main()
    {

    }

Quanto às suas próprias funções, certifique-se de defini-las da mesma forma, com cada chave em sua própria linha e com o tipo de retorno na mesma linha do nome da função, assim como fizemos com `main`.

## Indentação

Indente seu código quatro espaços de cada vez para deixar claro quais blocos de código estão dentro de outros. Se você usar a tecla Tab do seu teclado para fazer isso, certifique-se de que o editor de texto esteja configurado para converter tabs (`\t`) em quatro espaços, caso contrário, seu código pode não ser exibido corretamente no computador de outra pessoa, já que `\t` é renderizado de forma diferente em editores diferentes. (Se estiver usando [CS50 IDE](https://ide.cs50.io/), é aceitável usar Tab para indentação, em vez de pressionar repetidamente a barra de espaço do seu teclado, uma vez que nós já o configuramos para converter `\t` em quatro espaços.)

Aqui está um código com uma boa indentação:

    // Imprime argumentos da linha de comando um por linha
    printf("\n");
    for (int i = 0; i < argc; i++)
    {
        for (int j = 0, n = strlen(argv[i]); j < n; j++)
        {
            printf("%c\n", argv[i][j]);
        }
        printf("\n");
    }

## Loops

### for

Sempre que precisar de variáveis temporárias para iteração, use `i`, depois `j`, depois `k`, a menos que nomes mais específicos tornem seu código mais legível:

    for (int i = 0; i < LIMIT; i++)
    {
        for (int j = 0; j < LIMIT; j++)
        {
            for (int k = 0; k < LIMIT; k++)
            {
                // Faça algo
            }
        }
    }

Se você precisar de mais de três variáveis para iteração, pode ser hora de repensar seu design!

### while

Declare loops `while` da seguinte forma:

    while (condition)
    {
        // Faça algo
    }

Observe como:

- cada chave é colocada em sua própria linha;
- há um único espaço após `while`;
- não há espaço imediatamente após o `(` ou imediatamente antes do `)`; e
- o corpo do loop (um comentário neste caso) é indentado com 4 espaços.

### do ... while

Declare loops `do ... while` da seguinte forma:

    do
    {
        // Faça algo
    }
    while (condition);

Observe como:

- cada chave é colocada em sua própria linha;
- há um único espaço após `while`;
- não há espaço imediatamente após o `(` ou imediatamente antes do `)`; e
- o corpo do loop (um comentário neste caso) é indentado com 4 espaços.

## Ponteiros

Ao declarar um ponteiro, escreva o `*` ao lado da variável, como em:

    int *p;

Não o escreva ao lado do tipo, como em:

    int* p;

## Variáveis

Porque o CS50 usa [C99](http://en.wikipedia.org/wiki/C99), não defina todas as suas variáveis no início das suas funções, mas sim quando e onde você realmente precisa delas. Além disso, escopo suas variáveis da maneira mais restrita possível. Por exemplo, se `i` é necessário apenas para um loop, declare `i` dentro do próprio loop:

    for (int i = 0; i < LIMIT; i++)
    {
        printf("%i\n", i);
    }

Embora seja aceitável usar variáveis como `i`, `j` e `k` para iteração, a maioria das suas variáveis deve ter nomes mais específicos. Se você estiver somando alguns valores, por exemplo, chame sua variável de `sum`. Se o nome da sua variável exigir duas palavras (por exemplo, `is_ready`), coloque um sublinhado entre elas, uma convenção popular em C, embora não tanto em outras linguagens.

Se declarar várias variáveis do mesmo tipo de uma vez, é aceitável declará-las juntas, como em:

    int quarters, dimes, nickels, pennies;

Apenas não inicialize algumas e deixe outras não inicializadas, como em:

    int quarters, dimes = 0, nickels = 0 , pennies;

Também tenha cuidado ao declarar ponteiros separadamente de não-ponteiros, como em:

    int *p;
    int n;

Não declare ponteiros na mesma linha que não-ponteiros, como em:

    int *p, n;

## Estruturas

Declare uma `struct` como um tipo da seguinte forma, com cada chave em sua própria linha e membros indentados nela, e o nome do tipo também em sua própria linha:

    typedef struct
    {
        string name;
        string dorm;
    }
    student;

Se a `struct` contiver como membro um ponteiro para outra `struct` semelhante, declare a `struct` com um nome idêntico ao tipo, sem usar sublinhados:

    typedef struct node
    {
        int n;
        struct node *next;
    }
