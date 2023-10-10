# [NOME](#nome)

get_string - solicita ao usuário uma `string`

# [SINOPSE](#sinopse)

## Arquivo de cabeçalho

    #include <cs50.h>

## Protótipo

    string get_string(string prompt, ...);

# [DESCRIÇÃO](#descrição)

Essa função solicita ao usuário uma `string`.

Essa função espera pelo menos um argumento, `prompt`. Se `prompt` contiver algum código de formato, como em [printf](printf), essa função também aceita argumentos adicionais, um por código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna a entrada do usuário como uma `string`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        string s = get_string("Entrada:  ");
        printf("Saída: %s\n", s);
    }

# [VEJA TAMBÉM](#veja-também)

>     get_char(3), get_double(3), get_float(3), get_int(3),
>     get_long(3), printf(3)