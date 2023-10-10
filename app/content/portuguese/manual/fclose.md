# [NOME](#nome)

fclose - fechar um arquivo

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdio.h>

## Protótipo

    int fclose(FILE *stream);

# [DESCRIÇÃO](#descrição)

Esta função fecha um arquivo que foi aberto usando [fopen](fopen). Ela espera como entrada o ponteiro para um `FILE` que foi retornado por [fopen](fopen).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna `0` se bem-sucedida e `EOF`, uma constante, em caso de erro.

# [EXEMPLO](#exemplo)

    #inclue <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file != NULL)
        {
            fprintf(file, "This is CS50\n");
            fclose(file);
        }
    }
