# [NOME](#nome)

strcpy - copia uma string

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <string.h>

## Protótipo

    char *strcpy(char *dest, char *src);

# [DESCRIÇÃO](#descrição)

Esta função copia a string em `src`, incluindo seu caractere terminador `'\0'`, para a memória em `dest`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna `dest`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(void)
    {
        char *s = get_string("s: ");
        if (s != NULL)
        {
            char *t = malloc(strlen(s) + 1);
            if (t != NULL)
            {
                strcpy(t, s);
                printf("s: %s\n", s);
                printf("t: %s\n", t);
            }
        }
    }