# [NOME](#nome)

strstr - localiza uma substring

# [SINOPSE](#sinopse)

## Arquivos de Cabeçalho

    #include <cs50.h>
    #include <string.h>

## Protótipo

    string strstr(string haystack, string needle);

# [DESCRIÇÃO](#descrição)

Essa função procura por `needle` em `haystack` (a primeira ocorrência). Em outras palavras, ela determina se (e onde) `needle` é uma substring de `haystack`.

# [VALOR RETORNADO](#valor-retornado)

Se `needle` for encontrado em `haystack`, essa função retorna a substring de `haystack` que começa com `needle`. (Por exemplo, se `haystack` for `"foo bar bar baz"` e `needle` for `"bar"`, essa função retorna `"bar bar baz"`.) Se `needle` não for encontrado em `haystack`, essa função retorna `NULL`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <string.h>
    #include <stdio.h>

    int main(void)
    {
        string haystack = "foo bar bar baz";
        string needle = "bar";

        string match = strstr(haystack, needle);
        if (match)
        {
            printf("%s\n", match);
        }
    }
