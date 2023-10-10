# [NOME](#nome)

sprintf - imprimir em uma string

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdio.h>

## Protótipo

    int sprintf(char *str, const char *format, ...);

Observe que `...` representa zero ou mais argumentos adicionais.

# [DESCRIÇÃO](#descrição)

Esta função imprime uma "string formatada" em uma localização na memória. Ela espera como entrada o endereço de um buffer (que deve ser grande o suficiente para caber a string, incluindo seu `\0`), uma "string de formato" que especifica o que imprimir e zero ou mais argumentos subsequentes. A string de formato pode opcionalmente conter "especificações de conversão", marcadores que começam com `%` que especificam como formatar os argumentos subsequentes da função, se houver. Por exemplo, se `buffer` for um array de (no mínimo) 13 bytes e `i` for `50`, esta função poderia formatar uma string da seguinte forma:

    sprintf(buffer, "olá, %s\n", i);

Entre as especificações de conversão suportadas por esta função estão:

| Especificação de Conversão | Tipo     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `char *` |

Para imprimir um sinal de porcentagem real, use `%%`.

Para especificar a "precisão" de um `float` ou um `double`, `%f` pode opcionalmente conter um `.` após o `%`, seguido por um número de casas decimais. Por exemplo, esta função poderia formatar o valor de um terço com uma casa decimal usando `%.1f`, assumindo que `buffer` seja um array de tamanho 4 (no mínimo):

    sprintf(buffer, "%.1f\n", 1.0 / 3.0);

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o número de caracteres impressos.

# [EXEMPLOS](#exemplos)

    #include <stdio.h>

    int main(void)
    {
        char buffer[13];

        int i = 50;
        sprintf(buffer, "Isto é CS%i", i);
        printf("%s\n", buffer);

        float f = 50.0;
        sprintf(buffer, "Isto é CS%.0f", f);
        printf("%s\n", buffer);
    }
