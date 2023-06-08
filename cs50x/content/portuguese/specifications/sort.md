Laboratório 3: Ordenação
===========


<div class="alert" data-alert="warning" role="alert"><p>Você pode colaborar com um ou dois colegas neste laboratório, mas espera-se que cada aluno do grupo contribua igualmente para o laboratório.</p></div>

Analise três programas de ordenação para determinar quais algoritmos eles usam.

Contexto
----------

Lembre-se da aula que vimos alguns algoritmos para ordenar uma sequência de números: ordenação por seleção, ordenação por bolha e ordenação por fusão.

* A ordenação por seleção percorre as porções não ordenadas de uma lista, selecionando o menor elemento a cada vez e movendo-o para sua localização correta.
* A ordenação por bolha compara pares de valores adjacentes um de cada vez e os troca se estiverem na ordem incorreta. Isso continua até que a lista esteja ordenada.
* A ordenação por fusão divide recursivamente a lista em dois repetidamente e depois mescla as listas menores de volta em uma maior na ordem correta.

Começando
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e, em seguida, execute o comando `cd` sozinho. Você deve encontrar um prompt semelhante abaixo.

    $
    

Clique dentro dessa janela do terminal e, em seguida, execute

    wget https://cdn.cs50.net/2022/fall/labs/3/sort.zip
    

seguido de Enter para baixar um arquivo ZIP chamado `sort.zip` em seu workspace. Cuidado para não ignorar o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere para aquela questão!

Agora execute

    unzip sort.zip
    

para criar uma pasta chamada `sort`. Você não precisará mais do arquivo ZIP, portanto, execute

    rm sort.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Digite agora

    cd sort
    

seguido de Enter para se mover para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    sort/ $
    

Se tudo correu bem, execute

    ls
    

e você deve ver uma coleção de arquivos `.txt` juntos com os programas executáveis `sort1`, `sort2` e `sort3`.

Se você tiver algum problema, siga esses mesmos passos novamente e veja se consegue determinar onde ocorreu o erro!

Instruções
------------

Foram fornecidos a você três programas C já compilados, `sort1`, `sort2` e `sort3`. Cada um desses programas implementa um algoritmo de ordenação diferente: ordenação por seleção, ordenação por bolha ou ordenação por fusão (embora não necessariamente nessa ordem!). Sua tarefa é determinar qual algoritmo de classificação é usado por cada arquivo.

* Os arquivos `sort1`, `sort2` e `sort3` são arquivos binários e, portanto, você não conseguirá visualizar o código-fonte C de cada um. Para avaliar qual classificação implementa qual algoritmo, execute as classificações em diferentes listas de valores.
* Vários arquivos `.txt` são fornecidos a você. Esses arquivos contêm `n` linhas de valores, reversos, misturados ou ordenados.
    * Por exemplo, o arquivo `reversed10000.txt` contém 10000 linhas de números que estão reversos do `10000`, enquanto o arquivo `random10000.txt` contém 10000 linhas de números que estão em ordem aleatória.
* Para executar a classificação nos arquivos de texto, no terminal, execute `./[nome_do_programa] [arquivo_de_texto.txt]`. Certifique-se de ter usado o comando `cd` para entrar no diretório `sort`!
    * Por exemplo, para classificar `reversed10000.txt` com `sort1`, execute `./sort1 reversed10000.txt`.
* Você pode achar útil cronometrar suas classificações. Para fazer isso, execute `time ./[sort_file] [arquivo_de_texto.txt]`.
    * Por exemplo, você poderia executar `time ./sort1 reversed10000.txt` para rodar `sort1` em 10.000 números invertidos. No final da saída do terminal, você pode olhar o tempo `real` para ver quanto tempo realmente se passou enquanto o programa estava em execução.
* Registre suas respostas em `answers.txt`, juntamente com uma explicação para cada programa, preenchendo os espaços em branco marcados `TODO`.

### Passo a Passo


<div class="alert" data-alert="primary" role="alert"><p>Este vídeo foi gravado quando o curso ainda estava usando o CS50 IDE para escrever código. Embora a interface possa ser diferente do seu workspace, o comportamento dos dois ambientes deve ser em grande parte similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-Bhxxw6JKKY"></iframe>


### Sugestões

* Os diferentes tipos de arquivos `.txt` podem ajudá-lo a determinar qual classificação é qual. Considere como cada algoritmo se comporta com uma lista já ordenada. E uma lista invertida? Ou uma lista embaralhada? Pode ajudar a trabalhar através de uma lista menor de cada tipo e seguir cada processo de classificação.

<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/uOYhrBs37j0"></iframe></details>


### Como verificar suas respostas

Execute o abaixo para avaliar a correção de suas respostas usando `check50`. Mas certifique-se de preencher também suas explicações, que o `check50` não verificará aqui!

    check50 cs50/labs/2023/x/sort
    

Como Enviar
-------------

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/labs/2023/x/sort"