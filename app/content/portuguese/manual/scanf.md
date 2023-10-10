# [NOME](#nome)

scanf - obter entrada de um usuário

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdio.h>

## Protótipo

    int scanf(const char *format, ...);

Observe que `...` representa zero ou mais argumentos adicionais.

# [DESCRIÇÃO](#descrição)

Esta função "lê" a entrada do teclado de um usuário para valores de tipos especificados. Ela espera como entrada uma "string de formato" que especifica o que esperar e zero ou mais argumentos subsequentes, cada um dos quais deve ser uma localização na memória. A string de formato deve conter geralmente "especificações de conversão", espaços reservados que começam com `%` que especificam quais tipos de valores esperar. Os argumentos subsequentes receberão esses valores. Por exemplo, se `n` é um `int`, esta função pode obter um `int` de um usuário usando `%i`:

    scanf("%i", &n);

Entre as especificações de conversão suportadas por essa função estão:

| Especificação de conversão | Tipo     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |

Não é seguro usar esta função para obter uma string de um usuário usando `%s`, pois a entrada do usuário pode exceder a capacidade do argumento que seria atribuído a esse valor.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o número de argumentos que foram atribuídos valores ou `EOF`, uma constante definida em `stdio.h`, em casos de erro.

# [EXEMPLOS](#exemplos)

    #include <stdio.h>

    int main(void)
    {
        int i;
        printf("Entrada: ");
        scanf("%i", &i);
        printf("Saída: %i\n", i);
    }
