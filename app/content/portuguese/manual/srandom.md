# [NOME](#nome)

srandom - semeia a geração de números pseudorrandômicos

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #define _DEFAULT_SOURCE
    #include <stdlib.h>

## Protótipo

    void srandom(unsigned int seed);

Um `unsigned int` deve ser não negativo.

Definir `_DEFAULT_SOURCE` dessa forma permite o uso de [srandom](srandom) dentro de `stdlib.h`.

# [DESCRIÇÃO](#descrição)

Essa função altera a sequência de números pseudorrandômicos gerados por [random](random). Ela deve ser chamada (apenas uma vez) antes de fazer qualquer chamada para [random](random). Em outras palavras, se você chamar [srandom](srandom) pela primeira vez com uma `seed` de `1`, chamadas subsequentes para [random](random) retornarão valores diferentes do que se você chamar [srandom](srandom) pela primeira vez com uma `seed` de `2`.

Em vez de codificar um valor fixo para `seed`, é comum passar o valor de retorno de [time](/2/time) (que muda a cada segundo) para [srandom](srandom).

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função não retorna um valor.

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

Chamando `time` com um argumento `NULL`, uma constante definida em `stdlib.h`, retorna o tempo atual em segundos.