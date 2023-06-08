Laboratório 4: Volume
=============

Você pode colaborar com um ou dois colegas neste laboratório, embora seja esperado que cada aluno contribua igualmente para o laboratório.

Escreva um programa para modificar o volume de um arquivo de áudio.

    $ ./volume INPUT.wav OUTPUT.wav 2.0
    

Onde `INPUT.wav` é o nome de um arquivo de áudio original e `OUTPUT.wav` é o nome de um arquivo de áudio com um volume que foi escalonado pelo fator fornecido (por exemplo, 2.0).

Arquivos WAV
---------

[Arquivos WAV](https://docs.fileformat.com/audio/wav/) são um formato de arquivo comum para representar áudio. Arquivos WAV armazenam áudio como uma sequência de "amostras": números que representam o valor de algum sinal de áudio em um momento específico no tempo. Arquivos WAV começam com um "cabeçalho" de 44 bytes que contém informações sobre o próprio arquivo, incluindo o tamanho do arquivo, o número de amostras por segundo e o tamanho de cada amostra. Após o cabeçalho, o arquivo WAV contém uma sequência de amostras, cada uma um único número inteiro de 2 bytes (16 bits) que representa o sinal de áudio em um momento específico no tempo.

Escalonar cada valor de amostra por um fator dado tem o efeito de mudar o volume do áudio. Multiplicar cada valor de amostra por 2.0, por exemplo, terá o efeito de dobrar o volume do áudio original. Multiplicar cada amostra por 0,5, por outro lado, terá o efeito de cortar o volume pela metade.

Tipos
-----

Até agora, vimos vários tipos diferentes em C, incluindo `int`, `bool`, `char`, `double`, `float` e `long`. Dentro de um arquivo de cabeçalho chamado `stdint.h`, estão as declarações de vários outros tipos que nos permitem definir muito precisamente o tamanho (em bits) e o sinal (sinalizado ou não sinalizado) de um inteiro. Dois tipos em particular serão úteis para nós neste laboratório.

*   `uint8_t` é um tipo que armazena um inteiro não sinalizado de 8 bits (ou seja, não negativo). Podemos tratar cada byte de um cabeçalho de arquivo WAV como um valor `uint8_t`.
*   `int16_t` é um tipo que armazena um inteiro de 16 bits sinalizado (ou seja, positivo ou negativo). Podemos tratar cada amostra de áudio em um arquivo WAV como um valor `int16_t`.

Introdução
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e execute `cd`. Você deve ver que sua "prompt" se assemelha à abaixo.

    $
    

Clique dentro dessa janela de terminal e execute

    wget https://cdn.cs50.net/2022/fall/labs/4/volume.zip
    

seguido de Enter para baixar um arquivo ZIP chamado `volume.zip` no seu espaço de códigos. Tenha cuidado para não perder o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere!

Agora execute

    unzip volume.zip
    

para criar uma pasta chamada `volume`. Você não precisa mais do arquivo ZIP, então execute

    rm volume.zip
    

e responda com “y” seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd volume
    

seguido de Enter para mover-se para dentro (ou seja, abrir) esse diretório. Sua “prompt” agora deverá se assemelhar à abaixo.

    volume/ $
    

Se tudo correu bem, você deve executar

    ls
    

e verá um arquivo `volume.c` ao lado de um arquivo `input.wav`.

Se encontrar qualquer problema, siga estes mesmos passos novamente e veja se consegue determinar onde errou!

Detalhes da Implementação
----------------------

Complete a implementação do `volume.c`, para que ele altere o volume de um arquivo de som por um fator dado.

*   O programa aceita três argumentos da linha de comando: `input` representa o nome do arquivo de áudio original, `output` representa o nome do novo arquivo de áudio que deve ser gerado e `factor` é o valor pelo qual o volume do arquivo de áudio original deve ser ampliado.
    *   Por exemplo, se o `factor` for `2,0`, então o seu programa deve dobrar o volume do arquivo de áudio em `input` e salvar o arquivo de áudio recém-gerado em `output`.
*   Seu programa deve primeiro ler o cabeçalho do arquivo de entrada e escrever o cabeçalho no arquivo de saída. Lembre-se de que esse cabeçalho sempre tem exatamente 44 bytes de comprimento.
    *   Observe que `volume.c` já define uma variável para você chamada `HEADER_SIZE`, igual ao número de bytes no cabeçalho.
*   Seu programa deve então ler o restante dos dados do arquivo WAV, uma amostra de 16 bits (2 bytes) de cada vez. Seu programa deve multiplicar cada amostra pelo `factor` e escrever a nova amostra no arquivo de saída.
    *   Você pode assumir que o arquivo WAV usará valores de 16 bits assinados como amostras. Na prática, arquivos WAV podem ter números variáveis de bits por amostra, mas assumiremos amostras de 16 bits para este laboratório.
*   Seu programa, se usar `malloc`, não deve vazar nenhuma memória.

### Tutorial

Este vídeo foi gravado quando o curso ainda estava usando o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu espaço de códigos, o comportamento dos dois ambientes deve ser bastante semelhante!

### Dicas

*   É provável que você queira criar um array de bytes para armazenar os dados do cabeçalho do arquivo WAV que você lerá do arquivo de entrada. Usando o tipo `uint8_t` para representar um byte, você pode criar um array de `n` bytes para o cabeçalho com sintaxe como

    uint8_t header[n];
    

substituindo `n` pelo número de bytes. Você pode então usar o `header` como um argumento para `fread` ou `fwrite` para ler do ou escrever para o cabeçalho.

*   É provável que você queira criar um "buffer" para armazenar amostras de áudio que você lerá do arquivo WAV. Usando o tipo `int16_t` para armazenar uma amostra de áudio, você pode criar uma variável de buffer com sintaxe como

     int16_t buffer;
    

Você pode então usar `&buffer` como argumento para `fread` ou `fwrite` para ler ou escrever a partir do buffer. (Lembre-se de que o operador `&` é usado para obter o endereço da variável.)

*   Você pode achar a documentação para [`fread`](https://man.cs50.io/3/fread) e [`fwrite`](https://man.cs50.io/3/fwrite) útil aqui.
    *   Em particular, observe que ambas as funções aceitam os seguintes argumentos:
        *   `ptr`: um ponteiro para a localização na memória para armazenar dados (ao ler de um arquivo) ou de onde escrever dados (ao escrever dados em um arquivo)
        *   `size`: o número de bytes em um item de dados
        *   `nmemb`: o número de itens de dados (cada um com `size` bytes) para ler ou escrever
        *   `stream`: o ponteiro do arquivo a ser lido ou gravado
    *   Conforme sua documentação, `fread` retornará o número de itens de dados lidos com êxito. Você pode achar isso útil para verificar quando chegou ao final do arquivo!

Não sabe como resolver?

### Como testar seu código

Seu programa deve se comportar conforme os exemplos abaixo.

    $ ./volume input.wav output.wav 2.0
    

Quando você ouvir `output.wav` (como clicando com o botão direito em `output.wav` no navegador de arquivos, escolhendo **Download** e depois abrindo o arquivo em um player de áudio no seu computador), ele deve ser dobrar o volume de `input.wav`!

    $ ./volume input.wav output.wav 0.5
    

Quando você ouvir `output.wav`, ele deve ter metade do volume de `input.wav`!

Execute abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo você mesmo também!

    check50 cs50/labs/2023/x/volume
    

Execute abaixo para avaliar o estilo do seu código usando `style50`.

    style50 volume.c
    

Como Enviar
-------------

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/labs/2023/x/volume