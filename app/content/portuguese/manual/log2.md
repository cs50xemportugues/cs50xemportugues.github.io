# [NOME](#nome)

log2 - calcula o logaritmo na base 2 de um número

# [SINÓPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <math.h>

## Protótipo

    double log2(double x);

# [DESCRIÇÃO](#descrição)

Esta função calcula o logaritmo na base 2 de `x`.

# [RETORNO](#retorno)

Esta função retorna, como `double`, o logaritmo na base 2 de `x`.

# [EXEMPLO](#exemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Este é o CS%i\n", (int) log2(1125899906842624));
    }
