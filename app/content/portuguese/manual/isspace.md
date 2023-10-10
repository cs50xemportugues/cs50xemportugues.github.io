# [NOME](#nome)

isspace - verifica se um caractere é um espaço em branco (por exemplo, uma nova linha, espaço ou tabulação)

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <ctype.h>

## Protótipo

    int isspace(char c);

Pense nessa função como recebendo um `char` como entrada.

# [DESCRIÇÃO](#descrição)

Essa função verifica se `c` é um espaço em branco (por exemplo, `\n`, `' '`, ou `'\t'`) ou não.

# [RETORNO](#retorno)

Essa função retorna um valor `int` diferente de zero se `c` for um espaço em branco e `0` se `c` não for um espaço em branco.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isspace(c))
        {
            printf("Sua entrada é um espaço em branco.\n");
        }
        else
        {
            printf("Sua entrada não é um espaço em branco.\n");
        }
    }
