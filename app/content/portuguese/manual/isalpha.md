# [NOME](#nome)

isalpha - verifica se um caractere é alfabético

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int isalpha(char c);

Pense nessa função como recebendo um `char` como entrada.

# [DESCRIÇÃO](#descrição)

Essa função verifica se `c` é alfabético (ou seja, uma letra) ou não.

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna um `int` diferente de zero se `c` for alfabético e `0` se `c` não for alfabético.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Digite: ");
        if (isalpha(c))
        {
            printf("Sua entrada é alfabética.\n");
        }
        else
        {
            printf("Sua entrada não é alfabética.\n");
        }
    }