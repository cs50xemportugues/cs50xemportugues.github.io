// get_string e printf com %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("Qual é seu nome?\n");
    printf("olá, %s\n", s);
}
