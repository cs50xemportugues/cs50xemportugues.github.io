# [NOME](#nome)

realloc - realocar memória dinamicamente

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdlib.h>

## Protótipo

    void *realloc(void *ptr, size_t size);

Pense no `void *` como significando o endereço de qualquer tipo de valor na memória. Pense em `size_t` como um `long`.

# [DESCRIÇÃO](#descrição)

Essa função redimensiona dinamicamente um bloco de memória que foi retornado por `malloc`, cujo endereço do primeiro byte é `ptr`, para ter `size` bytes contíguos, movendo (e copiando) os bytes originais na memória conforme necessário.

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna o endereço do primeiro byte do bloco realocado (que pode ou não ser o mesmo que `ptr`) ou `NULL` em caso de erros (como quando não há memória suficiente disponível).

# [EXEMPLO](#exemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *s = malloc(3);
        if (s == NULL)
        {
            return 1;
        }

        s[0] = 'h';
        s[1] = 'i';
        s[2] = '\0';
        printf("%s\n", s);

        char *tmp = realloc(s, 4);
        if (tmp == NULL)
        {
            free(s);
            return 1;
        }
        s = tmp;

        s[2] = '!';
        s[3] = '\0';
        printf("%s\n", s);

        free(s);
        return 0;
    }
