// Troca dois inteiros usando ponteiros

#include <stdio.h>

void trocar(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x é %i, y é %i\n", x, y);
    trocar(&x, &y);
    printf("x é %i, y é %i\n", x, y);
}

void trocar(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
