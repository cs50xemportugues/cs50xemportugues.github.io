# [NOME](#nome)

atoi - converte uma `string` em `int`

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdlib.h>

## Protótipo

    int atoi(string s);

# [DESCRIÇÃO](#descricao)

Esta função converte um número inteiro (positivo ou negativo) de uma `string` (por exemplo, `"50"`) para um `int` (por exemplo, `50`).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna sua entrada, `s`, como um `int`.

# [EXEMPLO](#exemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("Este é CS%i\n", atoi("50"));
    }
