// Simula herança genética de tipo sanguíneo

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Cada pessoa tem dois pais e dois alelos
typedef struct pessoa
{
    struct pessoa *pais[2];
    char alelos[2];
}
pessoa;

const int GERACOES = 3;
const int TAMANHO_RECUO = 4;

pessoa *criar_familia(int geracoes);
void imprimir_familia(pessoa *p, int geracao);
void liberar_familia(pessoa *p);
char alelo_aleatorio();

int main(void)
{
    // Semente do gerador de números aleatórios
    srand(time(0));

    // Criar uma nova família com três gerações
    pessoa *p = criar_familia(GERACOES);

    // Imprimir árvore genealógica de tipos sanguíneos
    imprimir_familia(p, 0);

    // Liberar memória
    liberar_familia(p);
}

// Criar um novo indivíduo com `gerações`
pessoa *criar_familia(int geracoes)
{
    // TODO: Alocar memória para nova pessoa

    // Se ainda há gerações para criar
    if (geracoes > 1)
    {
        // Criar dois pais novos para a pessoa atual chamando recursivamente criar_familia
        pessoa *pai0 = criar_familia(geracoes - 1);
        pessoa *pai1 = criar_familia(geracoes - 1);

        // TODO: Definir ponteiros dos pais para a pessoa atual

        // TODO: Atribuir alelos aleatórios para a pessoa atual baseado nos alelos dos pais

    }

    // Se não há mais gerações para criar
    else
    {
        // TODO: Definir ponteiros dos pais como NULO

        // TODO: Atribuir alelos aleatórios

    }

    // TODO: Retornar pessoa recém-criada
    return NULL;
}

// Liberar `p` e todos os ancestrais de `p`.
void liberar_familia(pessoa *p)
{
    // TODO: Lidar com o caso base

    // TODO: Liberar pais recursivamente

    // TODO: Liberar filho

}

// Imprimir cada membro da família e seus alelos.
void imprimir_familia(pessoa *p, int geracao)
{
    // Lidar com o caso base
    if (p == NULL)
    {
        return;
    }

    // Imprimir recuo
    for (int i = 0; i < geracao * TAMANHO_RECUO; i++)
    {
        printf(" ");
    }

    // Imprimir pessoa
    if (geracao == 0)
    {
        printf("Filho (Geração %i): tipo sanguíneo %c%c\n", geracao, p->alelos[0], p->alelos[1]);
    }
    else if (geracao == 1)
    {
        printf("Pai (Geração %i): tipo sanguíneo %c%c\n", geracao, p->alelos[0], p->alelos[1]);
    }
    else
    {
        for (int i = 0; i < geracao - 2; i++)
        {
            printf("Tataravô-");
        }
        printf("Avô (Geração %i): tipo sanguíneo %c%c\n", geracao, p->alelos[0], p->alelos[1]);
    }

    // Imprimir pais da geração atual
    imprimir_familia(p->pais[0], geracao + 1);
    imprimir_familia(p->pais[1], geracao + 1);
}

// Escolhe aleatoriamente um alelo de tipo sanguíneo.
char alelo_aleatorio()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
