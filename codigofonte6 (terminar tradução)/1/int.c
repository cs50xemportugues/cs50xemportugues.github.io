// get_int e printf com %i

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int idade = get_int("Qual é sua idade?\n");
    printf("Você tem pelo menos %i dias de idade.\n", idade * 365);
}
