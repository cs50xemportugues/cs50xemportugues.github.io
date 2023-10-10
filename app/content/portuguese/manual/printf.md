# [NOME](#nome)

printf - imprimir na tela

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdio.h>

## Protótipo

    int printf(string formato, ...);

Observe que `...` representa zero ou mais argumentos adicionais.

# [DESCRIÇÃO](#descrição)

Esta função imprime uma "string formatada" na tela. Ela espera como entrada uma "string de formato" que especifica o que imprimir e zero ou mais argumentos subsequentes. A string de formato pode opcionalmente conter "especificações de conversão", espaços reservados que começam com `%` e especificam como formatar os argumentos subsequentes, se houver. Por exemplo, se `c` for um `char`, essa função pode imprimi-lo da seguinte maneira usando `%c`:

    printf("%c\n", c);

Alternativamente, essa função pode formatar o mesmo valor como um `int` também usando `%i`, como em uma tabela ASCII:

    printf("%c %i\n", c, c);

E essa função também pode imprimir strings sem especificações de conversão:

    printf("olá, mundo\n");

Entre as especificações de conversão suportadas por essa função estão:

| Especificação de Conversão | Tipo     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `string` |

Para imprimir um sinal de porcentagem real, use `%%`.

Para especificar a "precisão" de um `float` ou `double`, `%f` pode opcionalmente conter um `.` após o `%`, seguido por um número de casas decimais. Por exemplo, essa função pode formatar o valor de um terço com uma casa decimal usando `%.1f`:

    printf("%.1f\n", 1.0 / 3.0);

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o número de caracteres impressos.

# [EXEMPLOS](#exemplos)

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        string s = "Isto é CS50";
        printf("%s\n", s);

        int i = 50;
        printf("Isto é CS%i\n", i);

        float f = 50.0;
        printf("Isto é CS%.0f\n", f);
    }
