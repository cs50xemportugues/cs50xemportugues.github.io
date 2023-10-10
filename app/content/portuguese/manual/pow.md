# [NOME](#nome)

pow - elevar um número a uma potência

# [SINOPSE](#sinopse)

## Arquivo de cabeçalho

    #include <math.h>

## Protótipo

    double pow(double x, double y);

# [DESCRIÇÃO](#descrição)

Esta função eleva `x` à potência de `y`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna, como um `double`, `x` elevado à potência de `y`.

# [EXEMPLO](#exemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Um inteiro de 32 bits pode armazenar %li valores possíveis.\n", (long) pow(2, 32));
    }
