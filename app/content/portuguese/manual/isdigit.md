# [NOME](#nome)

isdigit - verifica se um caractere é um dígito.

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int isdigit(char c);

Pense nessa função como recebendo um `char` como entrada.

# [DESCRIÇÃO](#descrição)

Esta função verifica se `c` é um dígito decimal (`'0'` a `'9'`) ou não. Em outras palavras, ela verifica se o valor [ASCII](https://asciichart.com/) de `c` está entre 48 e 57, inclusive.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna um `int` diferente de zero se `c` for um dígito decimal e `0` se `c` não for um dígito decimal.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isdigit(c))
        {
            printf("Sua entrada é um dígito.\n");
        }
        else
        {
            printf("Sua entrada não é um dígito.\n");
        }
    }