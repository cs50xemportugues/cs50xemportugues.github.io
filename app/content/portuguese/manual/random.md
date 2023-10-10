# [NOME](#nome)

random - gera um número pseudoaleatório

# [SINÓPSE](#sinopse)

## Arquivo de cabeçalho

    #define _DEFAULT_SOURCE#include <stdlib.h>

## Protótipo

    long random(void);

Definir `_DEFAULT_SOURCE` dessa maneira permite usar `random` dentro de `stdlib.h`.

# [DESCRIÇÃO](#descrição)

Essa função gera um número pseudoaleatório entre `0` e `RAND_MAX`, incluindo o próprio `RAND_MAX`, onde `RAND_MAX` é uma constante definida em `stdlib.h`.

Para retornar um valor de ponto flutuante pseudoaleatório entre `0.0` e `1.0`, exclusivamente, ao invés disso, é comum dividir o valor de retorno de [random](random) por `(double) RAND_MAX + 1`, como em:

    float number = random() / ((double) RAND_MAX + 1);

Para retornar um número inteiro pseudoaleatório entre `0` e `N`, exclusivamente, onde `N` é algum número inteiro, é comum dividir o valor de retorno de [random](random) por `(double) RAND_MAX + 1` e em seguida multiplicar o quociente por `N`, como em:

    int number = (random() / ((double) RAND_MAX + 1)) * N;

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna o número gerado pseudoaleatoriamente como um `long`.

# [EXEMPLO](#exemplo)

    #define _DEFAULT_SOURCE
    #include <stdlib.h>

    #include <stdio.h>
    #include <time.h>

    int main(void)
    {
        srandom(time(NULL));
        printf("%lu\n", random());
        printf("%lu\n", random());
        printf("%lu\n", random());
    }

Chamar `time` com uma entrada `NULL`, uma constante definida em `stdlib.h`, retorna o tempo atual em segundos.