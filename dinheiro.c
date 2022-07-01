#include <cs50.h>
#include <stdio.h>

int receber_centavos(void);
int calcular_25_centavos(void);
int calcular_10_centavos(void);
int calcular_5_centavos(void);
int calcular_1_centavos(void);


int main(void)
{
    // Ask how many centavos the customer is owed
    int centavos = receber_centavos();

    // calcular the number of 25_centavos to give the customer
    int 25_centavos = calcular_25_centavos(centavos);
    centavos = centavos - 25_centavos * 25;

    // calcular the number of 10_centavos to give the customer
    int 10_centavos = calcular_10_centavos(centavos);
    centavos = centavos - 10_centavos * 10;

    // calcular the number of 5_centavos to give the customer
    int 5_centavos = calcular_5_centavos(centavos);
    centavos = centavos - 5_centavos * 5;

    // calcular the number of 1_centavos to give the customer
    int 1_centavos = calcular_1_centavos(centavos);
    centavos = centavos - 1_centavos * 1;

    // Soma moedas
    int total_moedas = 25_centavos + 10_centavos + 5_centavos + 1_centavos;

    // Print total number of coins to give the customer
    printf("%i\n", total_moedas);
}

int receber_centavos(void)
{
    // TODO
    return 0;
}

int calcular_25_centavos(int centavos)
{
    // TODO
    return 0;
}

int calcular_10_centavos(int centavos)
{
    // TODO
    return 0;
}

int calcular_5_centavos(int centavos)
{
    // TODO
    return 0;
}

int calcular_1_centavos(int centavos)
{
    // TODO
    return 0;
}
