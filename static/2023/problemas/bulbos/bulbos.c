#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void imprimir_lampada(int bit);

int main(void)
{
    // TO-DO
}

void imprimir_lampada(int bit)
{
    if (bit == 0)
    {
        // Emoji escuro
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Emoji claro
        printf("\U0001F7E1");
    }
}