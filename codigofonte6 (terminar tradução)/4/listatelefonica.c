// Salva nomes e números para um arquivo CSV

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Abre arquivo CSV
    FILE *arquivo = fopen("listatelefonica.csv", "a");
    if (!arquivo)
    {
        return 1;
    }

    // Recebe nome e número
    string nome = get_string("Nome: ");
    string numero = get_string("Número: ");

    // Imprime nome e número no arquivo
    fprintf(arquivo, "%s,%s\n", nome, numero);

    // Fecha arquivo
    fclose(arquivo);
}
