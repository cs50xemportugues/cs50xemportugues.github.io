DNA
===

Implemente um programa que identifique uma pessoa baseada em seu DNA, como abaixo.

    $ python dna.py databases/large.csv sequences/5.txt
    Lavender
    

Introdução
----------

Faça login no [code.cs50.io] (https://code.cs50.io/), clique na janela do terminal e execute `cd` isoladamente. Você deve ver que o prompt da janela do seu terminal se parece com o abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/6/dna.zip
    

para baixar um ZIP chamado `dna.zip` no seu espaço de códigos.

Em seguida, execute

    unzip dna.zip
    

para criar uma pasta chamada `dna`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm dna.zip
    

e responder com "y" seguido por Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd dna
    

seguido de Enter para mover-se para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve ser semelhante ao abaixo.

    dna/ $
    

Execute `ls` sozinho e você deve ver alguns arquivos e pastas:

    databases/ dna.py sequences/
    

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde deu errado!