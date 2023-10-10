# [NOME](#name)

strlen - calcula o comprimento de uma string

# [SINOPSE](#sinopse)

strlen - calcula o comprimento de uma string

## Arquivos de Cabeçalho

    #include <cs50.h>
    #include <string.h>

## Protótipo

    int strlen(string s);

# [DESCRIÇÃO](#descrição)

Esta função calcula o comprimento de `s`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o número de caracteres em `s`, excluindo o byte NUL de terminação (ou seja, `'\0'`).

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        string s = get_string("Entrada:  ");
        printf("Saída: ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            printf("%c", s[i]);
        }
        printf("\n");
    }