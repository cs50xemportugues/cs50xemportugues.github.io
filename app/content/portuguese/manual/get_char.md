# [NOME](#nome)

get_char - solicita ao usuário um `char`

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <cs50.h>

## Protótipo

    char get_char(string prompt, ...);

# [DESCRIÇÃO](#descrição)

Essa função solicita ao usuário um `char`. Se o usuário inserir mais ou menos que um `char`, a função solicitará novamente ao usuário.

Essa função espera pelo menos um argumento, `prompt`. Se `prompt` contiver algum código de formato, como [printf](printf), essa função aceita argumentos adicionais, um por código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna a entrada do usuário como um `char`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        char c = get_char("Entrada:  ");
        printf("Saída: %c.\n", c);
    }

# [VEJA TAMBÉM](#veja-também)

>     get_double(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)