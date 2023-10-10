# [NOME](#nome)

malloc - aloca memória dinamicamente

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdlib.h>

## Protótipo

    void *malloc(size_t size);

Pense em `void *` como significando o endereço de qualquer tipo de valor na memória. Pense em `size_t` como um `long`.

# [DESCRIÇÃO](#descrição)

Esta função aloca dinamicamente `size` bytes contíguos de memória (no heap) que podem ser usados para armazenar qualquer tipo de valor.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o endereço do primeiro byte de memória alocado ou `NULL` em casos de erro (como quando não há memória disponível suficiente).

# [EXEMPLO](#exemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *s = malloc(4);
        if (s == NULL)
        {
            return 1;
        }

        s[0] = 'h';
        s[1] = 'i';
        s[2] = '!';
        s[3] = '\0';
        printf("%s\n", s);

        free(s);
        return 0;
    }
