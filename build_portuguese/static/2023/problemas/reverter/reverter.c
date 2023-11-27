#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int verificar_formato(CABECALHOWAV cabecalho);
int obter_tamanho_bloco(CABECALHOWAV cabecalho);

int main(int argc, char *argv[])
{
    // Garantir uso adequado
    // FAZER #1

    // Abrir arquivo de entrada para leitura
    // FAZER #2

    // Ler o cabeçalho
    // FAZER #3

    // Utilizar verificar_formato para garantir formato WAV
    // FAZER #4

    // Abrir arquivo de saída para escrita
    // FAZER #5

    // Escrever cabeçalho no arquivo
    // FAZER #6

    // Utilizar obter_tamanho_bloco para calcular o tamanho do bloco
    // FAZER #7

    // Escrever áudio invertido no arquivo
    // FAZER #8
}

int verificar_formato(CABECALHOWAV cabecalho)
{
    // FAZER #4
    return 0;
}

int obter_tamanho_bloco(CABECALHOWAV cabecalho)
{
    // FAZER #7
    return 0;
}