# [NOME](#nome)

get_double - solicita ao usuário um `double`

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <cs50.h>

## Protótipo

    double get_double(string prompt, ...);

# [DESCRIÇÃO](#descrição)

Essa função solicita ao usuário um `double`. Se o usuário inserir qualquer coisa além de um `double` (ou um valor que não possa ser ajustado em um `double`), a função solicita ao usuário novamente.

Essa função espera pelo menos um argumento, `prompt`. Se o `prompt` contiver algum código de formato, semelhante ao [printf](printf), essa função aceita argumentos adicionais também, um por código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna a entrada do usuário o mais precisamente possível como um `double`.

# [EXEMPLO](#exemplo)

    #include <cs50.h>
    #include <stdio.h>
    int main(void)
    {
        double d = get_double("Entrada: ");
        printf("Saída: %f\n", d);
    }

# [VEJA TAMBÉM](#veja-também)

> get_char(3), get_float(3), get_int(3), get_long(3),
> get_string(3), printf(3)