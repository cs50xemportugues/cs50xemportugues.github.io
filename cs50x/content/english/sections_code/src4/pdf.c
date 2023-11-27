#include <cs50.h>
#include <stdio.h>
#include <stdint.h>

int main(int argc, string argv[])
{
    FILE *input = fopen(argv[1], "r");

    uint8_t buffer[4];

    fread(buffer, 1, 4, input);

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", buffer[i]);
    }

    fclose(input);
}