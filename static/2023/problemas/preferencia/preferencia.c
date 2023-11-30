#include <cs50.h>
#include <stdio.h>

// Número máximo de eleitores e candidatos
#define MAX_ELEITORES 100
#define MAX_CANDIDATOS 9

// preferences[i][j] é a j-ésima preferência do eleitor i
int preferencias[MAX_ELEITORES][MAX_CANDIDATOS];

// Candidatos têm nome, contagem de votos e status de eliminado
typedef struct
{
    string nome;
    int votos;
    bool eliminado;
}
candidato;

// Array de candidatos
candidato candidatos[MAX_CANDIDATOS];

// Números de eleitores e candidatos
int num_eleitores;
int num_candidatos;

// Protótipos de funções
bool voto(int eleitor, int classificacao, string nome);
void tabular(void);
bool imprimir_vencedor(void);
int encontrar_min(void);
bool empate(int min);
void eliminar(int min);

int main(int argc, string argv[])
{
    // Verificar uso inválido
    if (argc < 2)
    {
        printf("Uso: runoff [candidato ...]\n");
        return 1;
    }

    // Preencher array de candidatos
    num_candidatos = argc - 1;
    if (num_candidatos > MAX_CANDIDATOS)
    {
        printf("Número máximo de candidatos é %i\n", MAX_CANDIDATOS);
        return 2;
    }
    for (int i = 0; i < num_candidatos; i++)
    {
        candidatos[i].nome = argv[i + 1];
        candidatos[i].votos = 0;
        candidatos[i].eliminado = false;
    }

    num_eleitores = get_int("Número de eleitores: ");
    if (num_eleitores > MAX_ELEITORES)
    {
        printf("Número máximo de eleitores é %i\n", MAX_ELEITORES);
        return 3;
    }

    // Continuar perguntando votos
    for (int i = 0; i < num_eleitores; i++)
    {

        // Perguntar cada classificação
        for (int j = 0; j < num_candidatos; j++)
        {
            string nome = get_string("Classificação %i: ", j + 1);

            // Registrar voto, a menos que seja inválido
            if (!voto(i, j, nome))
            {
                printf("Voto inválido.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Continuar realizando votações até que haja um vencedor
    while (true)
    {
        // Calcular votos restantes para os candidatos
        tabular();

        // Verificar se a eleição foi vencida
        bool venceu = imprimir_vencedor();
        if (venceu)
        {
            break;
        }

        // Eliminar candidatos em último lugar
        int minimo = encontrar_min();
        bool empate = empate(minimo);

        // Se houver empate, todos ganham
        if (empate)
        {
            for (int i = 0; i < num_candidatos; i++)
            {
                if (!candidatos[i].eliminado)
                {
                    printf("%s\n", candidatos[i].nome);
                }
            }
            break;
        }

        // Eliminar candidatos com o mínimo de votos
        eliminar(minimo);

        // Resetar contagem de votos para zero
        for (int i = 0; i < num_candidatos; i++)
        {
            candidatos[i].votos = 0;
        }
    }
    return 0;
}

// Registrar preferência se o voto for válido
bool voto(int eleitor, int classificacao, string nome)
{
    // FAZER
    return false;
}

// Tabular votos para candidatos não eliminados
void tabular(void)
{
    // FAZER
    return;
}

// Imprimir o vencedor da eleição, se houver um
bool imprimir_vencedor(void)
{
    // FAZER
    return false;
}

// Retornar o número mínimo de votos que qualquer candidato restante tem
int encontrar_min(void)
{
    // FAZER
    return 0;
}

// Retornar verdadeiro se a eleição está empatada entre todos os candidatos, falso caso contrário
bool empate(int min)
{
    // FAZER
    return false;
}

// Eliminar o candidato (ou candidatos) em último lugar
void eliminar(int min)
{
    // FAZER
    return;
}