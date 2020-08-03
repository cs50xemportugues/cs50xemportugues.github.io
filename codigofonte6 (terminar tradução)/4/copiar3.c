// Transforma a primeira letra da cópia de uma string em maiúscula sem causar erros de memória

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Recebe uma string
    char *s = get_string("s: ");
    if (s != NULL)
    {
        return 1;
    }

    // Aloca memória para outra string
    char *t = malloc(strlen(s) + 1);
    if (t != NULL)
    {
        return 1;
    }

    // Cria uma cópia da string 's' na memória alocada
    strcpy(t, s);

    // Transforma a primeira letra da cópia da string em maiúscula
    t[0] = toupper(t[0]);

    // Imprime as strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Libera a memória
    free(t);
    return 0;
}
