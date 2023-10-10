# [NOME](#nome)

fprintf - imprime em um arquivo

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdio.h>

## Protótipo

    int fprintf(FILE *stream, const char *format, ...);

Observe que `...` representa nenhum ou mais argumentos adicionais.

# [DESCRIÇÃO](#descrição)

Essa função imprime uma "string formatada" em um arquivo. Ela espera como entrada um ponteiro para um `FILE` que foi retornado pela função [fopen](fopen), uma "string de formatação" que especifica o que imprimir e nenhum ou mais argumentos subsequentes. A string de formatação pode opcionalmente conter "especificações de conversão", espaços reservados que começam com `%` que especificam como formatar os argumentos subsequentes da função, se houver. Por exemplo, se `arquivo` é um ponteiro para um `FILE` e `c` é um `char`, essa função pode imprimir o último no primeiro da seguinte maneira usando `%c`:

    fprintf(arquivo, "%c\n", c);

Alternativamente, essa função também pode formatar o mesmo valor como um `int` usando `%i`, como em uma tabela ASCII:

    fprintf(arquivo, "%c %i\n", c, c);

E essa função também pode imprimir strings sem especificações de conversão:

    fprintf(arquivo, "olá, mundo\n");

Entre as especificações de conversão suportadas por essa função estão:

| Especificação de Conversão | Tipo       |
| ------------------------- | ---------- |
| `%c`                      | `char`     |
| `%f`                      | `double`   |
| `%f`                      | `float`    |
| `%i`                      | `int`      |
| `%li`                     | `long`     |
| `%s`                      | `char *`   |

Para imprimir o símbolo de porcentagem (`%`) literalmente, use `%%`.

Para especificar a "precisão" de um `float` ou `double`, `%f` pode opcionalmente conter um `.` após o `%`, seguido de um número de casas decimais. Por exemplo, essa função pode formatar o valor de um terço com uma casa decimal usando `%.1f`:

    fprintf(arquivo, "%.1f\n", 1.0 / 3.0);

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna o número de caracteres impressos.

# [EXEMPLOS](#exemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *arquivo = fopen("cs50.txt", "w");
        if (arquivo == NULL)
        {
            return 0;
        }

        char *s = "This is CS50";
        fprintf(arquivo, "%s\n", s);

        int i = 50;
        fprintf(arquivo, "This is CS%i\n", i);

        float f = 50.0;
        fprintf(arquivo, "This is CS%.0f\n", f);

        fclose(arquivo);
        return 0;
    }
