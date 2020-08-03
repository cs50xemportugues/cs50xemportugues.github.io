// Implementa pesquisa linear para procurar nomes

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Um array de nomes
    string nomes[] = {"LARA", "BRENDON", "ANDRE", "RAMON"};

    // Procura por LARA
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(nomes[i], "LARA") == 0)
        {
            printf("Encontrado\n");
            return 0;
        }
    }
    printf("Não foi encontrado\n");
    return 1;
}
