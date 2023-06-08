Dicas
-----

Para comparar duas strings ignorando as diferenças entre letras maiúsculas e minúsculas, você pode usar a função [`strcasecmp`](https://man.cs50.io/3/strcasecmp), declarada em `strings.h`! Você também deve garantir que sua função de hash não leve em consideração as diferenças entre letras maiúsculas e minúsculas, para que as palavras "foo" e "FOO" tenham o mesmo valor de hash.

Por fim, certifique-se de liberar toda memória alocada em `load` ao implementar a função `unload`! Lembre-se de que `valgrind` é seu novo melhor amigo. Saiba que `valgrind` verifica vazamentos de memória enquanto seu programa está em execução, então, certifique-se de fornecer argumentos na linha de comando caso queira que `valgrind` analise `speller` enquanto você usa um dicionário e/ou texto específico, como abaixo. É melhor usar um texto curto, senão `valgrind` pode demorar bastante para rodar.

    valgrind ./speller texts/cat.txt
    

Se você executar `valgrind` sem especificar um `texto` para `speller`, suas implementações de `load` e `unload` não serão chamadas (e, portanto, não serão analisadas).

Se não tiver certeza de como interpretar a saída do `valgrind`, basta pedir ajuda ao `help50`:

    help50 valgrind ./speller texts/cat.txt
    

Testando
--------

Como verificar se o programa está identificando as palavras incorretas? Bem, você pode consultar a chave de respostas que está no diretório `keys`, que está dentro do diretório `speller`. Por exemplo, dentro do arquivo `keys/lalaland.txt`, há todas as palavras que o seu programa _deveria_ considerar como incorretas.

Então, você pode executar seu programa em um texto em uma janela e, em outra janela, executar a solução da equipe no mesmo texto, como abaixo.

    ./speller texts/lalaland.txt
    ./speller50 texts/lalaland.txt
    

E então você pode comparar as janelas visualmente lado a lado. Porém, isso pode ficar tedioso rapidamente. Portanto, você pode querer redirecionar a saída do programa para um arquivo, como abaixo.

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt
    

Em seguida, você pode comparar ambos os arquivos lado a lado na mesma janela com um programa como `diff`, como abaixo.

    diff -y student.txt staff.txt
    

Ou então, para economizar tempo, você pode comparar a saída do seu programa (supondo que você redirecionou-a para, por exemplo, `student.txt`) com uma das chaves de resposta sem executar a solução da equipe, como abaixo.

    diff -y student.txt keys/lalaland.txt
    

Se a saída do seu programa corresponder às da equipe, o `diff` exibirá duas colunas que devem ser idênticas, exceto talvez pelos tempos de execução na parte inferior. Entretanto, se as colunas diferirem, você verá um `>` ou `|` onde elas diferem. Por exemplo, se você vir

    MISSPELLED WORDS                                                MISSPELLED WORDS
    
    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L
    

isso significa que seu programa (cuja saída está à esquerda) não considera que `Thelonious` ou `MIA` sejam palavras incorretas, mesmo que a saída da equipe (à direita) considere, como é mostrado pela ausência de, digamos, `Thelonious` na coluna da esquerda e pela presença de `Thelonious` na coluna da direita.

### `check50`

Para testar seu código de maneira menos manual (embora ainda não exaustiva), você também pode executar o comando abaixo.

    check50 cs50/problems/2023/x/speller
    

Observe que `check50` também verifica vazamentos de memória, portanto, certifique-se de que você tenha executado o `valgrind` também.

### style50

Execute o comando abaixo para avaliar o estilo de seu código usando o `style50`.

    style50 dictionary.c
    

Solução da equipe
-----------------

Como avaliar a velocidade (e a correção) do seu código? Bem, como sempre, sinta-se a vontade para brincar com a solução da equipe e comparar seus resultados, como abaixo.

    ./speller50 texts/lalaland.txt
    

Enviar
------

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/speller"