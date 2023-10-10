# [NOME](#nome)

time - obter tempo em segundos

# [SINOPSIS](#sinopsis)

## Arquivo de cabeçalho

    #include <time.h>

## Protótipo

    long time(NULL);

Pense nessa função como retornando um `long` como saída e aceitando apenas `NULL` como entrada.

# [DESCRIÇÃO](#descrição)

Esta função obtém a data e hora atual em segundos desde 1º de janeiro de 1970, 00:00:00 UTC, também conhecido como Epoch.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o número de segundos desde 1º de janeiro de 1970, 00:00:00 UTC.

# [EXEMPLO](#exemplo)

    #include <stdio.h>
    #include <time.h>

    int main(void)
    {
        printf("A hora atual é %li.\n", time(NULL));
    }
