# [NOME](#nome)

isblank - verifica se um caractere está em branco (ou seja, um espaço ou um tab)

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int isblank(char c);

Pense nesta função como recebendo um `char` como entrada.

# [DESCRIÇÃO](#descrição)

Esta função verifica se `c` está em branco (ou seja, `' '` ou `'\t'`) ou não.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna um `int` diferente de zero se `c` estiver em branco e `0` se `c` não estiver em branco.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isblank(c))
        {
            printf("Sua entrada está em branco.\n");
        }
        else
        {
            printf("Sua entrada não está em branco.\n");
        }
    }
