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