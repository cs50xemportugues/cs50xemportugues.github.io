# [NOME](#nome)

fread - lê bytes de um arquivo

# [SINOPSE](#sinopse)

## Arquivo de Cabeçalho

    #include <stdio.h>

## Protótipo

    size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);

Pense em `void *` como representando o endereço do primeiro byte de qualquer tipo de dado. Pense em `size_t` como um `long`.

# [DESCRIÇÃO](#descrição)

Essa função lê dados de um arquivo que foi aberto via [fopen](fopen). Ela espera como entrada:

- `ptr`, que é o endereço (do primeiro byte) da memória para a qual os dados serão lidos,
- `size`, que é o tamanho (em bytes) do tipo de dado a ser lido,
- `nmemb`, que é o número desses tipos a serem lidos de uma vez, e
- `stream`, que é o ponteiro para um `FILE` retornado por [fopen](fopen).

Por exemplo, se estiver lendo um `char` de cada vez, `size` seria `sizeof(char)` (ou seja, `1`), e `nmemb` seria `1`.

# [VALOR DE RETORNO](#valor-de-retorno)

Essa função retorna o número de itens lidos, que é igual ao número de bytes lidos quando `size` é `1`.

Se ocorrer um erro ou o final do arquivo for atingido, essa função poderá retornar um valor menor que `nmemb` ou até mesmo `0`.

O arquivo aberto "lembra" o número de bytes que foram lidos com sucesso, de modo que chamadas subsequentes a essa função para `stream` retornarão bytes após os já lidos.

# [EXEMPLOS](#exemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *arquivo = fopen("cs50.txt", "r");
        if (arquivo != NULL)
        {
            char c;
            while (fread(&c, sizeof(char), 1, arquivo))
            {
                printf("%c", c);
            }
            fclose(arquivo);
        }
    }
