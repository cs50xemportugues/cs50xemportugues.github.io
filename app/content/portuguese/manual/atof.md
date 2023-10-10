# [NOME](#nome)

atof - converte uma `string` para um `float`

# [SINOPSE](#sinopse)

## Arquivo de cabeçalho

    #include <stdlib.h>

## Protótipo

    float atof(string s);

# [DESCRIÇÃO](#descrição)

Esta função converte um valor de ponto flutuante (positivo ou negativo) de uma `string` (por exemplo, `"50.0"`) para um `float` (por exemplo, `50.0`).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna sua entrada, `s`, como um `float`.

# [EXEMPLO](#exemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("Isto é CS%.0f\n", atof("50.0"));
    }