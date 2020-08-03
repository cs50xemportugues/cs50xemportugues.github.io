// Abstração e escopo

#include <cs50.h>
#include <stdio.h>

int receber_inteiro_positivo(void);

int main(void)
{
    int i = receber_inteiro_positivo();
    printf("%i\n", i);
}

// Pede ao usuário para informar um inteiro positivo
int receber_inteiro_positivo(void)
{
    int n;
    do
    {
        n = get_int("Inteiro positivo: ");
    }
    while (n < 1);
    return n;
}
