#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Pontos atribuídos a cada letra do alfabeto
int PONTOS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int calcular_pontuacao(string palavra);

int main(void)
{
    // Obter palavras de entrada de ambos os jogadores
    string palavra1 = get_string("Jogador 1: ");
    string palavra2 = get_string("Jogador 2: ");

    // Pontuar ambas as palavras
    int pontuacao1 = calcular_pontuacao(palavra1);
    int pontuacao2 = calcular_pontuacao(palavra2);

    // TODO: Imprimir o vencedor
}

int calcular_pontuacao(string palavra)
{
    // TODO: Calcular e retornar a pontuação para a palavra
}