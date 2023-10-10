# [NOME](#nome)

floor - calcular o piso de um número

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <math.h>

## Protótipo

    double floor(double x);

# [DESCRIÇÃO](#descrição)

Esta função retorna o piso de `x`.

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna, como um `double`, o maior valor inteiro que não é maior que `x`. Você pode converter esse valor com segurança para um `long` (ou um `int` se couber).

# [EXEMPLO](#exemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("This is CS%i\n", (int) floor(50.1));
    }
