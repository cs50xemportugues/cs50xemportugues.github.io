# [NOME](#nome)

free - libera memória alocada dinamicamente

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdlib.h>

## Protótipo

    void free(void *ptr);

Pense em `void *` como significando o endereço de qualquer tipo de valor na memória.

# [DESCRIÇÃO](#descrição)

Esta função libera a memória que foi alocada dinamicamente com `malloc`. Ela espera como entrada o ponteiro que foi retornado por [malloc](malloc).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função não retorna um valor.

# [EXEMPLO](#exemplo)

    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(void)
    {
        char *s = "olá, mundo\n";
        char *t = malloc(strlen(s) + 1);
        if (t != NULL)
        {
            strcpy(t, s);
            printf("%s\n", t);
            free(t);
        }
    }