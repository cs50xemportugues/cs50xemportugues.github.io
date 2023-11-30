#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Máximo de candidatos
#define MAX 9

// Candidatos têm nome e quantidade de votos
typedef struct
{
    string nome;
    int votos;
}
candidato;

// Array de candidatos
candidato candidatos[MAX];

// Quantidade de candidatos
int quantidade_candidatos;

// Protótipos de funções
bool votar(string nome);
void imprimir_vencedor(void);

int main(int argc, string argv[])
{
    // Verificar uso inválido
    if (argc < 2)
    {
        printf("Uso: pluralidade [candidato ...]\n");
        return 1;
    }

    // Popular o array de candidatos
    quantidade_candidatos = argc - 1;
    if (quantidade_candidatos > MAX)
    {
        printf("O número máximo de candidatos é %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < quantidade_candidatos; i++)
    {
        candidatos[i].nome = argv[i + 1];
        candidatos[i].votos = 0;
    }

    int quantidade_eleitores = get_int("Número de eleitores: ");

    // Loop em todos os eleitores
    for (int i = 0; i < quantidade_eleitores; i++)
    {
        string nome = get_string("Vote: ");

        // Verificar voto inválido
        if (!votar(nome))
        {
            printf("Voto inválido.\n");
        }
    }

    // Exibir o vencedor da eleição
    imprimir_vencedor();
}

// Atualizar a quantidade de votos dado um novo voto
bool votar(string nome)
{
    // FAZER
    return false;
}

// Exibir o vencedor (ou vencedores) da eleição
void imprimir_vencedor(void)
{
    // FAZER
    return;
}