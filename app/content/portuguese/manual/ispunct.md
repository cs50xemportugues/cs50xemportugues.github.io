# [NOME](#nome)

ispunct - verifica se um caractere é uma pontuação

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int ispunct(char c);

Pense nessa função como recebendo um `char` como entrada.

# [DESCRIÇÃO](#descrição)

Essa função verifica se `c` é um sinal de pontuação (por exemplo, `'.'`, ou `','`, ou `'!'`, etc.) ou não.

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna um `int` diferente de zero se `c` for uma pontuação e `0` se `c` não for uma pontuação.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input: ");
        if (ispunct(c))
        {
            printf("Sua entrada é uma pontuação.\n");
        }
        else
        {
            printf("Sua entrada não é uma pontuação.\n");
        }
    }
