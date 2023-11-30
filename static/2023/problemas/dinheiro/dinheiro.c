#include <cs50.h>
#include <stdio.h>

int obter_centavos(void);
int calcular_quartos(int centavos);
int calcular_dimes(int centavos);
int calcular_niqueis(int centavos);
int calcular_centavos(int centavos);

int main(void)
{
    // Perguntar quantos centavos o cliente deve receber
    int centavos = obter_centavos();

    // Calcular a quantidade de quartos a serem dados ao cliente
    int quartos = calcular_quartos(centavos);
    centavos = centavos - quartos * 25;

    // Calcular a quantidade de dimes a serem dados ao cliente
    int dimes = calcular_dimes(centavos);
    centavos = centavos - dimes * 10;

    // Calcular a quantidade de níqueis a serem dados ao cliente
    int niqueis = calcular_niqueis(centavos);
    centavos = centavos - niqueis * 5;

    // Calcular a quantidade de centavos a serem dados ao cliente
    int centavos = calcular_centavos(centavos);
    centavos = centavos - centavos * 1;

    // Somar as moedas
    int moedas = quartos + dimes + niqueis + centavos;

    // Imprimir o total de moedas a ser dados ao cliente
    printf("%i\n", moedas);
}

int obter_centavos(void)
{
    // FAZER
    return 0;
}

int calcular_quartos(int centavos)
{
    // FAZER
    return 0;
}

int calcular_dimes(int centavos)
{
    // FAZER
    return 0;
}

int calcular_niqueis(int centavos)
{
    // FAZER
    return 0;
}

int calcular_centavos(int centavos)
{
    // FAZER
    return 0;
}