# [NOME](#nome)

strcasecmp - compara duas strings ignorando maiúsculas e minúsculas

# [SINOPSE](#sinopse)

## Arquivos de Cabeçalho

    #include <cs50.h>#include <strings.h>

## Protótipo

    int strcasecmp(string s1, string s2);

# [DESCRIÇÃO](#descrição)

Esta função compara duas strings sem levar em consideração se as letras estão em maiúsculas ou minúsculas.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna

- um `int` menor que `0` se `s1` vier antes de `s2`, ignorando maiúsculas e minúsculas,
- `0` se `s1` for igual a `s2`, ignorando maiúsculas e minúsculas, ou
- um `int` maior que `0` se `s1` vier depois de `s2`, ignorando maiúsculas e minúsculas.

As strings são comparadas utilizando a ordem "ASCIIbetical", baseada nos valores ASCII de seus caracteres. Por exemplo, `"AAA"` viria antes de `"BBB"`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <stdio.h>
    #include <strings.h>

    int main(void)
    {
        string s1 = get_string("s1: ");
        string s2 = get_string("s2: ");
        if (strcasecmp(s1, s2) == 0)
        {
            printf("São iguais, mesmo ignorando maiúsculas e minúsculas.\n");
        }
        else
        {
            printf("São diferentes, mesmo ignorando maiúsculas e minúsculas.\n");
        }
    }