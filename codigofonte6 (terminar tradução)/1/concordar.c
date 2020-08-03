// Operadores lógicos

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Pergunta ao usuário se ele concorda
    char c = get_char("Você concorda?\n");

    // Checa se usuário concordou
    if (c == 'S' || c == 's')
    {
        printf("Concordou.\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("Não concordou.\n");
    }
}
