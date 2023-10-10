# [NOME](#nome)

atol - converte uma `string` em um `long`

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdlib.h>

## Protótipo

    long atol(string s);

# [DESCRIÇÃO](#descrição)

Esta função converte um inteiro (positivo ou negativo) de uma `string` (por exemplo, `"50"`) para um `long` (por exemplo, `50`).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o valor de entrada, `s`, como um `long`.

# [EXEMPLO](#exemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("Este é o CS%li\n", atol("50"));
    }
