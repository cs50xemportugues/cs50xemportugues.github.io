# [NOME](#nome)

get_int - solicita ao usuário um `int`

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <cs50.h>

## Protótipo

    int get_int(string prompt, ...);

# [DESCRIÇÃO](#descrição)

Esta função solicita ao usuário um `int`. Se o usuário inserir qualquer coisa que não seja um `int` (ou um valor que não possa ser armazenado em um `int`), a função solicitará ao usuário novamente.

Esta função espera pelo menos um argumento, `prompt`. Se `prompt` contiver quaisquer códigos de formato, como [printf](printf), esta função também aceitará argumentos adicionais, um para cada código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna a entrada do usuário como um `int`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        int i = get_int("Entrada:  ");
        printf("Saída: %i\n", i);
    }

# [VEJA TAMBÉM](#veja-também)

>     get_char(3), get_double(3), get_float(3), get_long(3),
>     get_string(3), printf(3)