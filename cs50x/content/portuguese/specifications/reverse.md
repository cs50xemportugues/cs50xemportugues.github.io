Reverse
=======

Implementar um programa que inverta um arquivo WAV, conforme abaixo.

    ./reverse input.wav output.wav
    

Background
----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/J9iyqMwYtG4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Em "Fire on High", do Electric Light Orchestra, há algo um pouco diferente sobre o primeiro minuto da música. Se você ouvir, soará como se o áudio estivesse tocando de trás para frente. Como se constata, se você reproduzir a seção inicial da música ao contrário, ouvirá o seguinte:

_"The music is reversible. Time is not. Turn back, turn back!"_

Estranho, certo? Essa é uma técnica chamada "backmasking", ou esconder mensagens na música que só podem ser ouvidas quando a música é tocada de trás para frente. Muitos artistas usaram (ou foram suspeitos de usar) essa técnica em suas músicas. Para investigar o backmasking, pedimos que você escreva um programa que possa inverter arquivos WAV para nós!

Ao contrário dos arquivos de áudio MP3, os arquivos WAV não são comprimidos. Isso torna os arquivos muito mais fáceis de editar e manipular, o que é útil para a tarefa em questão. Para aprender um pouco mais sobre arquivos WAV, precisamos dar uma olhada mais de perto no formato de arquivo WAV.

Getting Started
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da sua janela do terminal e execute `cd` sozinho. Você deve ver que seu "prompt" se parece com o abaixo.

    $
    

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/psets/4/reverse.zip
    

Seguido de Enter, para baixar um arquivo ZIP chamado `reverse.zip` no seu código. Não perca o espaço entre `wget` e a URL a seguir, ou qualquer outro caractere!

Agora execute

    unzip reverse.zip
    

Para criar uma pasta chamada `reverse`. Você não precisa mais do arquivo ZIP, então execute

    rm reverse.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd reverse
    

Seguido de Enter para se mover para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    reverse/ $
    

Se tudo correu bem, você deve executar

    ls
    

e ver um arquivo chamado `reverse.c`. Executar `code reverse.c` deve abrir o arquivo onde você digitará seu código para este conjunto de problemas. Se isso não acontecer, volte seus passos e descubra onde você errou!

### O formato do arquivo WAV

Observe que, na imagem abaixo, um arquivo WAV é dividido em três partes. Cada parte tem alguns blocos de dados dentro dela.

A primeira parte contém informações sobre o tipo de arquivo. Em particular, veja como o bloco "Formato de Arquivo" na primeira parte soletra 'W' 'A' 'V' 'E' nos bytes 8 a 11, para indicar que o arquivo é um arquivo WAV.

A segunda parte contém informações sobre os dados de áudio que virão a seguir, incluindo quantos "canais" de áudio estão presentes e quantos bits estão em cada "amostra" de áudio. Os arquivos de áudio têm 1 canal quando são "monofônicos": se você usar fones de ouvido, ouvirá o mesmo áudio em seu ouvido esquerdo e direito. Os arquivos de áudio têm 2 canais quando são "estereofônicos": ouvindo com fones de ouvido, você ouvirá áudio ligeiramente diferente em seu ouvido esquerdo e direito, criando uma sensação de amplitude. As amostras são os fragmentos individuais de bits que compõem o áudio que você ouve. Com mais bits por amostra, um arquivo de áudio pode ter maior clareza (à custa do uso de mais memória!).

Por fim, a terceira parte contém os dados de áudio em si - aquelas amostras mencionadas acima.

Tudo antes dos dados de áudio é considerado parte do "cabeçalho" do arquivo WAV. Lembre-se de que um cabeçalho de arquivo é simplesmente alguns metadados sobre o arquivo. Neste caso, o cabeçalho tem 44 bytes de comprimento.

![WAV Header](https://cs50.harvard.edu/x/2023/psets/4/reverse/WAV_header.png)

Uma explicação mais técnica dos cabeçalhos de WAV pode ser encontrada [aqui](http://soundfile.sapp.org/doc/WaveFormat/), que é o recurso que inspirou esta imagem. Observe que incluímos um arquivo, `wav.h`, que implementa todos esses detalhes para você em uma estrutura chamada `WAVHEADER`.

Especificação
-------------

Vamos escrever um programa chamado `reverse` que nos permite reverter um arquivo WAV fornecido pelo usuário e criar um novo arquivo WAV que contém o áudio reverso resultante. Para simplificar, limitaremos os arquivos que lidamos ao formato WAV. No momento em que o usuário executa o programa, ele deve fornecer, usando dois argumentos de linha de comando, o nome do arquivo de entrada a ser lido e revertido, e o nome do arquivo de saída em que o áudio resultante deve ser salvo. Um programa executado com sucesso não deve produzir nenhum texto e deve criar um arquivo WAV com o nome especificado pelo usuário que toca o áudio do arquivo WAV de entrada na ordem reversa. Por exemplo:

    $ ./reverse input.wav output.wav

Em `reverse.c`, você notará que algumas bibliotecas úteis foram incluídas, bem como um arquivo de cabeçalho, `wav.h`. Você provavelmente achará isso útil ao implementar seu programa. Deixamos oito `TODO`s e duas funções auxiliares para você preencher e recomendamos que você resolva-os de 1 a 8.

* No primeiro `TODO`, você deve garantir que o programa aceite dois argumentos de linha de comando: o nome do arquivo WAV de entrada e o nome do arquivo WAV de saída. Se o programa não atender a essas condições, você deve imprimir uma mensagem de erro apropriada e retornar `1`, encerrando o programa.
    <ul>
      <li data-marker="+">Dica
        <ul>
          <li data-marker="*">Lembre-se de que o número de argumentos de linha de comando pode ser encontrado nas variáveis <code class="language-plaintext highlighter-rouge">argc</code> passadas para a função <code class="language-plaintext highlighter-rouge">main</code> quando o programa é executado.</li>
          <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">argv[0]</code> contém o nome do programa como o primeiro argumento da linha de comando.</li>
        </ul>
      </li>
    </ul>
* No segundo `TODO`, você deve abrir o arquivo de entrada. Precisamos abrir o arquivo de entrada no modo "somente leitura", já que leremos apenas dados do arquivo de entrada. Pode ser prudente verificar se o arquivo foi aberto com sucesso. Caso contrário, você deve imprimir uma mensagem de erro apropriada e retornar `1`, encerrando o programa. Devemos adiar a abertura do arquivo de saída, para não criar um novo arquivo WAV antes de saber se o arquivo de entrada é válido!
    <ul>
      <li data-marker="+">Dica
        <ul>
          <li data-marker="*">Se o primeiro `TODO` for implementado corretamente, é seguro supor que podemos fazer referência ao nome do arquivo de entrada usando <code class="language-plaintext highlighter-rouge">argv[1]</code>.</li>
          <li data-marker="*">Lembre-se de que, qualquer arquivo que abrimos, também precisamos fechar quando terminarmos de usá-lo. Isso pode significar adicionar código em outro lugar no programa.</li>
        </ul>
      </li>
    </ul>
* No terceiro `TODO`, você deve ler o cabeçalho do arquivo de entrada. Lembre-se de que, em `wav.h`, já implementamos uma estrutura que pode armazenar um cabeçalho de arquivo WAV. Como escrevemos `#include "wav.h"` no topo de `reverse.c`, você também pode usar a estrutura `WAVHEADER`.
    
* No quarto `TODO`, você deve concluir a função `check_format`. `check_format` recebe um único argumento, um `WAVHEADER` chamado `header`, representando uma estrutura contendo o cabeçalho do arquivo de entrada. Se `header` indicar que o arquivo é de fato um arquivo WAV, a função `check_format` deve retornar `true`. Se não, `check_format` deve retornar `false`. Para verificar se um arquivo é do formato WAV, podemos comparar os elementos do cabeçalho do arquivo de entrada aos que esperaríamos de um arquivo WAV. É suficiente mostrar que os caracteres marcadores "WAVE" são encontrados no membro `format` da estrutura `WAVHEADER` (consulte [Background](#background) para obter mais detalhes sobre os cabeçalhos de arquivos WAV).
    
* No quinto `TODO`, agora é seguro abrir o arquivo de saída para gravação. Ainda é prudente verificar se o arquivo foi aberto com sucesso.
    <ul>
      <li data-marker="+">Dicas
        <ul>
          <li data-marker="*">Se o primeiro `TODO` for implementado corretamente, é seguro supor que podemos fazer referência ao nome do arquivo de saída usando <code class="language-plaintext highlighter-rouge">argv[2]</code>.</li>
          <li data-marker="*">Lembre-se de que, qualquer arquivo que abrimos, também precisamos fechar quando terminarmos de usá-lo. Isso pode significar adicionar código em outro lugar no programa.</li>
        </ul>
      </li>
    </ul>

Este pode ser um bom lugar para parar e testar se o seu programa se comporta como o esperado. Se implementado corretamente, seu programa deve abrir um novo arquivo quando executado com os argumentos de linha de comando adequados.

Se a qualquer momento você achar necessário excluir um arquivo, execute o seguinte comando em seu diretório de trabalho atual.

    $ rm nome_do_arquivo.wav

Se você não deseja ser solicitado a confirmar cada exclusão, execute o comando abaixo.

    $ rm -f nome_do_arquivo.wav

Apenas tome cuidado com a opção `-f`, pois ela faz a exclusão sem perguntar.

* Em seguida, agora que o tipo de arquivo foi verificado, o sexto `TODO` nos diz para escrever o cabeçalho no arquivo de saída. O arquivo WAV revertido ainda terá a mesma estrutura de arquivo subjacente do arquivo de entrada (mesmo tamanho, número de canais, bits por amostra, etc.), então é suficiente copiar o cabeçalho que lemos do arquivo de entrada no terceiro `TODO` para o arquivo de saída.
    
* No sétimo `TODO`, você deve implementar a função `get_block_size`. `get_block_size`, como `check_format`, recebe um único argumento: é um `WAVHEADER` chamado `header`, representando a estrutura que contém o cabeçalho do arquivo de entrada. `get_block_size` deve retornar um inteiro representando o **tamanho do bloco** do arquivo WAV fornecido, em bytes. Podemos pensar em um _bloco_ como uma unidade de dados auditivos. Para áudio, calculamos o tamanho de cada bloco com o seguinte cálculo: **número de canais** multiplicado por **bytes por amostra**. Felizmente, o cabeçalho contém todas as informações necessárias para calcular esses valores. Certifique-se de fazer referência à seção [Background](#background) para uma explicação mais detalhada sobre o que esses valores significam e como eles são armazenados. Veja também `wav.h`, para determinar quais membros de `WAVHEADER` podem ser úteis.
<ul>
<li

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

