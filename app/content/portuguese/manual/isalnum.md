# [NOME](#nome)

isalnum - verifica se um caractere é alfanumérico

# [SINOPSIS](#sinopsis)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int isalnum(char c);

Pense nesta função como recebendo um `char` como entrada.

# [DESCRIPÇÃO](#descripcao)

Esta função verifica se `c` é alfanumérico (ou seja, uma letra ou um número) ou não.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna um `int` diferente de zero se `c` for alfanumérico e `0` se `c` não for alfanumérico.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isalnum(c))
        {
            printf("Sua entrada é alfanumérica.\n");
        }
        else
        {
            printf("Sua entrada não é alfanumérica.\n");
        }
    }