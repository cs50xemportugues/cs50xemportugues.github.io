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