# [NOME](#nome) 

ceil - calcula o teto de um número

# [SINOPSE](#sinopse) 

## Arquivo de cabeçalho

    #include <math.h>

## Protótipo

    double ceil(double x);

# [DESCRIÇÃO](#descrição) 

Esta função retorna o teto de `x`.

# [VALOR DE RETORNO](#valor-de-retorno) 

Esta função retorna, como um `double`, o menor inteiro que não é menor que `x`. Você pode converter com segurança esse valor para um `long` (ou um `int` se ele couber).

# [EXEMPLO](#exemplo) 

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("This is CS%i\n", (int) ceil(49.9));
    }