# [NOME](#nome)

toupper - converte um `char` para maiúscula

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int toupper(char c);

Pense nesta função como recebendo um `char` como entrada.

# [DESCRIÇÃO](#descrição)

Esta função converte `c` para maiúscula.

# [VALOR DE RETORNO](#valor-de-retorno)

Se `c` for uma letra minúscula (`a` a `z`), esta função retorna seu equivalente em maiúscula (`A` a `Z`). Se `c` não for uma letra minúscula, esta função retorna `c` ele mesmo.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada:  ");
        printf("Saída: %c\n", toupper(c));
    }
