#include <cs50.h>
#include <stdio.h>

// Número máximo de candidatos
#define MAX 9

// preferences[i][j] é o número de eleitores que preferem o candidato i ao candidato j
int preferences[MAX][MAX];

// locked[i][j] significa que o candidato i está bloqueado em relação ao candidato j
bool locked[MAX][MAX];

// Cada par tem um vencedor e um perdedor
typedef struct
{
    int vencedor;
    int perdedor;
}
par;

// Array de candidatos
string candidatos[MAX];
par pares[MAX * (MAX - 1) / 2];

int numero_de_pares;
int numero_de_candidatos;

// Protótipos de funções
bool votar(int classificacao, string nome, int classificacoes[]);
void registrar_preferencias(int classificacoes[]);
void adicionar_pares(void);
void ordenar_pares(void);
void bloquear_pares(void);
void imprimir_vencedor(void);

int main(int argc, string argv[])
{
    // Verificar uso inválido
    if (argc < 2)
    {
        printf("Uso: tideman [candidato ...]\n");
        return 1;
    }

    // Preencher o array de candidatos
    numero_de_candidatos = argc - 1;
    if (numero_de_candidatos > MAX)
    {
        printf("Número máximo de candidatos é %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < numero_de_candidatos; i++)
    {
        candidatos[i] = argv[i + 1];
    }

    // Limpar o grafo de pares bloqueados
    for (int i = 0; i < numero_de_candidatos; i++)
    {
        for (int j = 0; j < numero_de_candidatos; j++)
        {
            locked[i][j] = false;
        }
    }

    numero_de_pares = 0;
    int numero_de_eleitores = get_int("Número de eleitores: ");

    // Consultar votos
    for (int i = 0; i < numero_de_eleitores; i++)
    {
        // classificacoes[i] é a preferência k-ésima do eleitor
        int classificacoes[numero_de_candidatos];

        // Consultar cada classificação
        for (int j = 0; j < numero_de_candidatos; j++)
        {
            string nome = get_string("Posição %i: ", j + 1);

            if (!votar(j, nome, classificacoes))
            {
                printf("Voto inválido.\n");
                return 3;
            }
        }

        registrar_preferencias(classificacoes);

        printf("\n");
    }

    adicionar_pares();
    ordenar_pares();
    bloquear_pares();
    imprimir_vencedor();
    return 0;
}

// Atualizar as classificações dado um novo voto
bool votar(int classificacao, string nome, int classificacoes[])
{
    // FAZER
    return false;
}

// Atualizar as preferências dado as classificações de um eleitor
void registrar_preferencias(int classificacoes[])
{
    // FAZER
    return;
}

// Registrar pares de candidatos onde um é preferido ao outro
void adicionar_pares(void)
{
    // FAZER
    return;
}

// Ordenar pares em ordem decrescente pela força da vitória
void ordenar_pares(void)
{
    // FAZER
    return;
}

// Bloquear pares no grafo de candidatos em ordem, sem criar ciclos
void bloquear_pares(void)
{
    // FAZER
    return;
}

// Imprimir o vencedor da eleição
void imprimir_vencedor(void)
{
    // FAZER
    return;
}