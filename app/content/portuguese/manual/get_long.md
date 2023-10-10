# [NOME](#nome)

get_long - solicita ao usuário um `long`

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <cs50.h>

## Protótipo

    long get_long(string prompt, ...);

# [DESCRIÇÃO](#descrição)

Esta função solicita ao usuário um `long`. Se o usuário inserir qualquer valor que não seja um `long` (ou um valor que não possa ser armazenado em um `long`), a função solicitará ao usuário novamente.

Esta função espera pelo menos um argumento, `prompt`. Se `prompt` contiver algum código de formato, como [printf](printf), esta função também aceitará argumentos adicionais, um por código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna a entrada do usuário como um `long`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        long l = get_long("Entrada:  ");
        printf("Saída: %li\n", l);
    }

# [VEJA TAMBÉM](#veja-também)

>     get_char(3), get_double(3), get_float(3), get_int(3), get_string(3),
>     printf(3)