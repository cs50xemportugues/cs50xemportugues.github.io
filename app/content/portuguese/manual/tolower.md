# [NOME](#nome)

tolower - converte um `char` para minúsculo

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int tolower(char c);

Pense nesta função como recebendo um `char` como entrada.

# [DESCRIÇÃO](#descrição)

Esta função converte `c` para minúsculo.

# [VALOR DE RETORNO](#valor-de-retorno)

Se `c` for uma letra maiúscula (`A` a `Z`), esta função retorna o equivalente em minúsculo (`a` a `z`). Se `c` não for uma letra maiúscula, esta função retorna o próprio `c`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada:  ");
        printf("Saída: %c\n", tolower(c));
    }
