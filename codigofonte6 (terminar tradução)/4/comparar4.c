// Compara duas strings usando strcmp

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Recebe duas strings
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Compara as strings
    if (strcmp(s, t) == 0)
    {
        printf("Iguais\n");
    }
    else
    {
        printf("Diferentes\n");
    }
}
