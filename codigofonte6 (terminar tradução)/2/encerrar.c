// Retorna um valor explicitamente dentro main

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("falta um argumento de linha de comando\n");
        return 1;
    }
    printf("olá, %s\n", argv[1]);
    return 0;
}
