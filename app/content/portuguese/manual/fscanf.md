# [NOME](#nome)

fscanf - obter entrada de um arquivo

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdio.h>

## Protótipo

    int fscanf(FILE *stream, const char *format, ...);

Observe que `...` representa zero ou mais argumentos adicionais.

# [DESCRIÇÃO](#descrição)

Esta função "lê" um arquivo em busca de valores de tipos especificados. Ela espera como entrada o ponteiro para um `FILE` que foi retornado por [fopen](fopen), uma "string de formato" que especifica o que esperar e zero ou mais argumentos subsequentes, cada um dos quais deve ser um local na memória. A string de formato deve conter geralmente "especificações de conversão", espaços reservados que começam com `%` e especificam quais tipos de valores esperar. Os argumentos subsequentes receberão esses valores. Por exemplo, se `n` for um `int`, esta função pode obter um `int` de um usuário usando `%i`:

    scanf("%i", &n);

Entre as especificações de conversão suportadas por esta função estão:

| Especificação de Conversão | Tipo     |
| ------------------------- | -------- |
| `%c`                      | `char`   |
| `%f`                      | `double` |
| `%f`                      | `float`  |
| `%i`                      | `int`    |
| `%li`                     | `long`   |

Para obter uma única palavra (ou seja, uma sequência de caracteres sem espaço), use `%s`. No entanto, é seguro usar esta função para obter uma palavra de um arquivo usando `%s` apenas se essa palavra tiver um comprimento máximo. Por exemplo, se `file` for um ponteiro para um `FILE` que foi retornado por [fopen](fopen) e `buffer` for um array de 3 bytes, esta função poderá ser usada para obter `"hi"`, incluindo o `'\0'`, mas não `"hi!"`, da seguinte forma:

    fscanf(file, "%s", buffer);

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o número de argumentos que tiveram valores atribuídos ou `EOF`, uma constante definida em `stdio.h`, se o final do arquivo for alcançado.

# [EXEMPLOS](#exemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("hi.txt", "r");
        if (file != NULL)
        {
            char buffer[3];
            fscanf(file, "%s", buffer);
            fclose(file);
            printf("%s\n", buffer);
        }
    }
