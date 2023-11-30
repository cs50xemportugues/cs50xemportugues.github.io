#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

// cada um dos nossos arquivos de texto contém 1000 palavras
#define TAMANHOLISTA 1000

// valores para cores e pontuação (EXATA == letra certa, lugar certo; PRÓXIMA == letra certa, lugar errado; ERRADA == letra errada)
#define EXATA 2
#define PRÓXIMA 1
#define ERRADA 0

// códigos de cor ANSI para letras cercadas
#define VERDE   "\e[38;2;255;255;255;1m\e[48;2;106;170;100;1m"
#define AMARELO  "\e[38;2;255;255;255;1m\e[48;2;201;180;88;1m"
#define VERMELHO     "\e[38;2;255;255;255;1m\e[48;2;220;20;60;1m"
#define RESETA   "\e[0;39m"

// protótipos de função definidos pelo usuário
string obter_palpite(int tamanhopalavra);
int verificar_palavra(string palpite, int tamanhopalavra, int status[], string escolha);
void imprimir_palavra(string palpite, int tamanhopalavra, int status[]);

int main(int argc, string argv[])
{
    // garantir o uso correto
    // FAZER #1

    int tamanhopalavra = 0;

    // garantir que argv[1] seja 5, 6, 7 ou 8 e armazenar esse valor em tamanhopalavra
    // FAZER #2

    // abrir arquivo correto, cada arquivo tem exatamente TAMANHOLISTA palavras
    char nome_arquivo[6];
    sprintf(nome_arquivo, "%i.txt", tamanhopalavra);
    FILE *wordlist = fopen(nome_arquivo, "r");
    if (wordlist == NULL)
    {
        printf("Erro ao abrir o arquivo %s.\n", nome_arquivo);
        return 1;
    }

    // carregar o arquivo de palavras em uma matriz de tamanho TAMANHOLISTA
    char opcoes[TAMANHOLISTA][tamanhopalavra + 1];

    for (int i = 0; i < TAMANHOLISTA; i++)
    {
        fscanf(wordlist, "%s", opcoes[i]);
    }

    // selecionar pseudorandomicamente uma palavra para este jogo
    srand(time(NULL));
    string escolha = opcoes[rand() % TAMANHOLISTA];

    // permitir mais um palpite do que o comprimento da palavra
    int palpites = tamanhopalavra + 1;
    bool ganhou = false;

    // imprimir cumprimento, usando códigos de cor ANSI para demonstrar
    printf(VERDE"Este é o WORDLE50"RESET"\n");
    printf("Você tem %i tentativas para adivinhar a palavra de %i letras que estou pensando\n", palpites, tamanhopalavra);

    // laço principal do jogo, uma iteração para cada palpite
    for (int i = 0; i < palpites; i++)
    {
        // obter palpite do usuário
        string palpite = obter_palpite(tamanhopalavra);

        // matriz para armazenar o status do palpite, inicialmente definida como zero
        int status[tamanhopalavra];

        // definir todos os elementos da matriz status inicialmente como 0, ou seja, ERRADA
        // FAZER #4

        // calcular a pontuação para o palpite
        int pontuação = verificar_palavra(palpite, tamanhopalavra, status, escolha);

        printf("Palpite %i: ", i + 1);
        
        // imprimir o palpite
        imprimir_palavra(palpite, tamanhopalavra, status);

        // se eles acertaram exatamente, definir o loop como terminado
        if (pontuação == EXATA * tamanhopalavra)
        {
            ganhou = true;
            break;
        }
    }

    // imprimir o resultado do jogo
    // FAZER #7

    // é isso, pessoal!
    return 0;
}

string obter_palpite(int tamanhopalavra)
{
    string palpite = "";

    // garantir que os usuários realmente forneçam um palpite do comprimento correto
    // FAZER #3

    return palpite;
}

int verificar_palavra(string palpite, int tamanhopalavra, int status[], string escolha)
{
    int pontuação = 0;

    // comparar o palpite com a escolha e pontuar conforme apropriado, armazenando os pontos em status
    // FAZER #5

    // DICAS
    // iterar sobre cada letra do palpite
        // iterar sobre cada letra da escolha
            // comparar a letra atual do palpite com a letra atual da escolha
                // se elas estiverem na mesma posição na palavra, marcar EXATA pontos (verde) e parar para não comparar mais essa letra
                // se estiver na palavra, mas não no lugar certo, marcar PERTO ponto (amarelo)
        // controlar a pontuação total somando os pontos individuais de cada letra acima

    return pontuação;
}

void imprimir_palavra(string palpite, int tamanhopalavra, int status[])
{
    // imprimir palavra caractere a caractere com codificação de cores corretas, em seguida, redefinir a fonte do terminal para normal
    // FAZER #6

    printf("\n");
    return;
}