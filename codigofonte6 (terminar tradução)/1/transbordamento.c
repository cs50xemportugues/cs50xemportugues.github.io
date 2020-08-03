// Transbordamento de inteiro

#include <stdio.h>
#include <unistd.h>

int main(void)
{
    // Duplica o valor de i iterativamente
    for (int i = 1; ; i *= 2)
    {
        printf("%i\n", i);
        sleep(1);
    }
}
