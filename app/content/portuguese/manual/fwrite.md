# [NOME](#nome)

fwrite - escreve bytes em um arquivo

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdio.h>

## Protótipo

    size_t fwrite(void *ptr, size_t size, size_t nmemb, FILE *stream);

Pense em `void *` como representando o endereço do primeiro byte de qualquer tipo de dado. Pense em `size_t` como um `long`.

# [DESCRIÇÃO](#descrição)

Esta função escreve dados em um arquivo que foi aberto por meio de [fopen](fopen). Ela recebe como entrada:

- `ptr`, que é o endereço (do primeiro byte) da memória de onde ler os dados,
- `size`, que é o tamanho (em bytes) do tipo de dado para escrever,
- `nmemb`, que é o número desses tipos para escrever de uma só vez, e
- `stream`, que é o ponteiro para um `FILE` retornado por [fopen](fopen).

Por exemplo, se estiver escrevendo um `char` por vez, `size` seria `sizeof(char)` (ou seja, `1`), e `nmemb` seria `1`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna o número de itens escritos, que é igual ao número de bytes escritos quando `size` é `1`.

Se ocorrer um erro, ou o final do arquivo for alcançado, esta função pode retornar um valor menor que `nmemb` ou até mesmo `0`.

# [EXEMPLOS](#exemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *input = fopen("input.txt", "r");
        if (input == NULL)
        {
            return 1;
        }

        FILE *output = fopen("output.txt", "w");
        if (output == NULL)
        {
            fclose(input);
            return 1;
        }

        char c;
        while (fread(&c, sizeof(char), 1, input))
        {
            fwrite(&c, sizeof(char), 1, output);
        }

        fclose(input);
        fclose(output);
    }
