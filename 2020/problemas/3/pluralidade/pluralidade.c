#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Número máximo de candidatos
#define MAX 9

// Candidatos possuem um nome e número de votos
typedef struct
{
    string nome;
    int votos;
}
candidato;


// Vetor de candidatos
candidato candidatos[MAX];

// Número de candidatos
int numero_candidatos;

// Protótipos das funções
bool voto(string nome);
void imprimir_vencedor(void);

int main(int argc, string argv[])
{
    // Checa uso incorreto
    if (argc < 2)
    {
        printf("Uso correto: pluralidade [candidato ...]\n");
        return 1;
    }

    // Preenche vetor de candidatos
    numero_candidatos = argc - 1;
    if (numero_candidatos > MAX)
    {
        printf("O número máximo de candidatos é %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < numero_candidatos; i++)
    {
        candidatos[i].nome = argv[i + 1];
        candidatos[i].votos = 0;
    }

    int numero_votantes = get_int("Número de votantes: ");

    // Recebe os votos
    for (int i = 0; i < numero_votantes; i++)
    {
        string nome = get_string("Voto: ");

        // Checa se o voto é inválido
        if (!voto(nome))
        {
            printf("Voto inválido.\n");
        }
    }

    // Exibe o vencedor da eleição
    imprimir_vencedor();
}

// Atualiza o número total de votos ao receber um novo voto
bool voto(string nome)
{
    // À FAZER
    return false;
}

// Imprime o vencedor (ou vencedores) da eleição
void imprimir_vencedor(void)
{
    // À FAZER
    return;
}

