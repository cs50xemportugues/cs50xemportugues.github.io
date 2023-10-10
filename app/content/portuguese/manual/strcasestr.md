# [NOME](#nome)

strstr, strcasestr - localizar uma substring

# [SINOPSE](#sinopse)

strcasestr - localizar uma substring

## Arquivos de Cabeçalho

    #include <cs50.h>

    #define _GNU_SOURCE
    #include <string.h>

## Protótipo

    string strcasestr(string haystack, string needle);

Definir `_GNU_SOURCE` desta maneira permite usar [strcasestr](strcasestr) dentro de `string.h`.

# [DESCRIÇÃO](#descrição)

Esta função procura `needle` em `haystack` (a primeira ocorrência) sem diferenciação de maiúsculas e minúsculas. Em outras palavras, ela determina se (e onde) `needle` é uma substring de `haystack`, ignorando o caso.

# [VALOR DE RETORNO](#valor-de-retorno)

Se `needle` for encontrado em `haystack`, ignorando o caso, esta função retorna a substring de `haystack` que começa com `needle`. (Por exemplo, se `haystack` for `"FOO BAR BAR BAZ"` e `needle` for `"bar"`, esta função retorna `"BAR BAR BAZ"`.) Se `needle` não for encontrado em `haystack`, ignorando o caso, esta função retorna `NULL`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <stdio.h>

    #define _GNU_SOURCE
    #include <string.h>

    int main(void)
    {
        string haystack = "FOO BAR BAR BAZ";
        string needle = "bar";

        string match = strstr(haystack, needle);
        if (match)
        {
            printf("%s\n", match);
        }
    }
