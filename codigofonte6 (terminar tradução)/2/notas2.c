// Calcula a média de três números usando um array e uma constante

#include <cs50.h>
#include <stdio.h>

const int N = 3;

int main(void)
{
    // Notas
    int notas[N];
    notas[0] = 72;
    notas[1] = 73;
    notas[2] = 33;

    // Imprime a média
    printf("Média: %i\n", (notas[0] + notas[1] + notas[2]) / N);
}
