# [NOME](#nome)

fopen - abre um arquivo

# [SINOPSE](#sinopse)

## Arquivo de cabeçalho

    #include <stdio.h>

## Protótipo

    FILE *fopen(const char *caminho_arquivo, const char *modo);

# [DESCRIÇÃO](#descrição)

Esta função abre um arquivo, `caminho_arquivo`. Os valores suportados para `modo` incluem:

- `"r"`, se estiver abrindo o arquivo para leitura,
- `"w"`, se estiver abrindo o arquivo para escrita, e
- `"a"`, se estiver abrindo o arquivo para anexar.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta função retorna um ponteiro para um `FILE` representando o arquivo aberto ou, em caso de erro (como quando `caminho_arquivo` não existe), `NULL`.

# [EXEMPLOS](#exemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *arquivo = fopen("cs50.txt", "w");
        if (arquivo != NULL)
        {
            fprintf(arquivo, "Este é o CS50\n");
            fclose(arquivo);
        }
    }
