Uso
---

Aqui estão alguns exemplos de como o programa deve funcionar. Por exemplo, se o usuário omitir um dos argumentos da linha de comando:


    $ ./reverse input.wav
    Uso: ./reverse input.wav output.wav
    

Ou se o usuário omitir ambos os argumentos da linha de comando:

    $ ./reverse
    Uso: ./reverse input.wav output.wav
    

É assim que o programa deve funcionar se o usuário fornecer um arquivo de entrada que não é um arquivo WAV real:


    $ ./reverse image.jpg output.wav
    A entrada não é um arquivo WAV


Você pode assumir que o usuário insere um nome de arquivo de saída válido, como `output.wav`.

Um programa executado com sucesso não deve gerar texto e deve criar um arquivo WAV com o nome especificado pelo usuário que reproduza o áudio do arquivo WAV de entrada ao contrário. Por exemplo:

    $ ./reverse input.wav output.wav
    

Teste
-----

Execute o comando abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilar e testá-lo por si mesmo também!

    check50 cs50/problems/2023/x/reverse
    

Execute o comando abaixo para avaliar o estilo do seu código usando `style50`.

    style50 reverse.c
    

Como Enviar
-----------

No terminal, digite o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/reverse