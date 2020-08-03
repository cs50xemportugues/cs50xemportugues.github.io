// Abstração usando parâmetros

#include <stdio.h>

void atchim(int n);

int main(void)
{
    atchim(3);
}

// Espirra um número n de vezes
void atchim(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("atchim\n");
    }
}
