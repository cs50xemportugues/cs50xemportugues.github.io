// Modifica o volume de um arquivo de áudio

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Número de bytes no cabeçalho .wav
const int TAMANHO_CABECALHO = 44;

int main(int argc, char *argv[])
{
    // Verifica os argumentos da linha de comando
    if (argc != 4)
    {
        printf("Uso: ./volume input.wav output.wav fator\n");
        return 1;
    }

    // Abre os arquivos e determina o fator de escala
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Não foi possível abrir o arquivo.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Não foi possível abrir o arquivo.\n");
        return 1;
    }

    float fator = atof(argv[3]);

    // TODO: Copie o cabeçalho do arquivo de entrada para o arquivo de saída

    // TODO: Leia as amostras do arquivo de entrada e escreva os dados atualizados no arquivo de saída

    // Fecha os arquivos
    fclose(input);
    fclose(output);
}
