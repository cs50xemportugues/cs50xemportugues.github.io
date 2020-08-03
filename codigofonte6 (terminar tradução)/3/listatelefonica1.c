// Implementa uma lista telefônica usando structs

#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string nome;
    string numero;
}
pessoa;

int main(void)
{
    pessoa pessoas[4];

    pessoas[0].nome = "LARA";
    pessoas[0].numero = "98765-0100";

    pessoas[1].nome = "BRENDON";
    pessoas[1].numero = "98765-0101";

    pessoas[2].nome = "ANDRE";
    pessoas[2].numero = "98765-0102";

    pessoas[3].nome = "RAMON";
    pessoas[3].numero = "98765-0103";

    // Procura por ANDRE
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(pessoas[i].nome, "LARA") == 0)
        {
            printf("Encontrado %s\n", pessoas[i].numero);
            return 0;
        }
    }
    printf("Não encontrado\n");
    return 1;
}
