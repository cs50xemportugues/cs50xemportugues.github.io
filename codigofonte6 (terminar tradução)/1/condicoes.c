// Condicionais e operadores relacionais

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Pede ao usuário para informar x
    int x = get_int("x: ");

    // Pede ao usuário para informar y
    int y = get_int("y: ");

    // Compara x e y
    if (x < y)
    {
        printf("x é menor do que y\n");
    }
    else if (x > y)
    {
        printf("x é maior do que y\n");
    }
    else
    {
        printf("x é igual a y\n");
    }
}
