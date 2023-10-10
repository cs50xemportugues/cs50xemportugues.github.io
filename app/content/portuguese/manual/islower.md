# [NOME](#nome)

islower - verifica se um caractere é minúsculo

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int islower(char c);

Pense nessa função como recebendo um `char` como entrada.

# [DESCRIÇÃO](#descrição)

Esta função verifica se `c` é uma letra minúscula (`'a'` a `'z'`) ou não. Em outras palavras, ela verifica se o valor [ASCII](https://asciichart.com/) de `c` está entre 97 e 122, inclusive.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna um `int` diferente de zero se `c` for uma letra minúscula e `0` se `c` não for uma letra minúscula.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (islower(c))
        {
            printf("Sua entrada é uma letra minúscula.\n");
        }
        else
        {
            printf("Sua entrada não é uma letra minúscula.\n");
        }
    }