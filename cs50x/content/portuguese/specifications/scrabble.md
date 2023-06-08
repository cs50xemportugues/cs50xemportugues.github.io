# Laboratório 2: Scrabble

<div class="alert" data-alert="warning" role="alert"><p>Você pode colaborar com um ou dois colegas neste laboratório, embora seja esperado que cada aluno que estiver em um grupo deste tipo contribua igualmente com o laboratório.</p></div>

Determine qual das duas palavras de Scrabble vale mais.

    $ ./scrabble
    Jogador 1: COMPUTADOR
    Jogador 2: ciência
    Jogador 1 ganhou!

## Primeiros passos

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da sua janela do terminal e execute o comando `cd`. Você deve ver que o "prompt" se parece com o abaixo.

    $

Clique dentro da janela do terminal e execute o seguinte comando

    wget https://cdn.cs50.net/2022/fall/labs/2/scrabble.zip

seguido por Enter para baixar um arquivo ZIP chamado `scrabble.zip` no seu codespace. Tome cuidado para não ignorar o espaço entre `wget` e a URL a seguir, ou qualquer outro caractere, na verdade!

Agora execute

    unzip scrabble.zip

para criar uma pasta chamada `scrabble`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm scrabble.zip

e responder com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd scrabble

seguido de Enter para se movimentar dentro daquele diretório. Seu prompt deverá ser semelhante ao abaixo.

    scrabble/ $

Se tudo correu bem, você deve abrir o arquivo `scrabble.c` executando

    code scrabble.c

Se você tiver algum problema, siga os mesmos passos novamente e veja se consegue determinar onde errou!

## Antecedentes

No jogo de [Scrabble](https://scrabble.hasbro.com/en-us/rules), os jogadores criam palavras para marcar pontos e o número de pontos é a soma dos valores de cada letra na palavra.

<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
      <th>I</th>
      <th>J</th>
      <th>K</th>
      <th>L</th>
      <th>M</th>
      <th>N</th>
      <th>O</th>
      <th>P</th>
      <th>Q</th>
      <th>R</th>
      <th>S</th>
      <th>T</th>
      <th>U</th>
      <th>V</th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>1</td>
      <td>8</td>
      <td>5</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>10</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>8</td>
      <td>4</td>
      <td>10</td>
    </tr>
  </tbody>
</table>

Por exemplo, se quisermos marcar a palavra `Code`, notaremos que nas regras gerais do Scrabble, o `C` vale `3` pontos, o `o` vale `1` ponto, o `d` vale `2` pontos e o `e` vale `1` ponto. Somando esses pontos, obtemos `Code` que vale `3 + 1 + 2 + 1 = 7` pontos.

## Detalhes de Implementação

Complete a implementação de `scrabble.c`, de modo que ela determine o vencedor de um jogo curto semelhante a Scrabble, no qual dois jogadores inserem sua palavra, e o jogador com a maior pontuação vence.

- Observe que armazenamos os valores numéricos de cada letra do alfabeto em um array de inteiros chamado `POINTS`.
  - Por exemplo, `A` ou `a` valem 1 ponto (representado por `POINTS[0]`), `B` ou `b` valem 3 pontos (representado por `POINTS[1]`), etc.
- Observe que criamos um protótipo para uma função auxiliar chamada `compute_score()` que recebe uma string como entrada e retorna um `int`. Sempre que quisermos atribuir valores de pontos a uma determinada palavra, podemos chamar esta função. Observe que este protótipo é necessário para que o C saiba que `compute_score()` existe mais tarde no programa.
- Em `main()`, o programa solicita as duas palavras aos dois jogadores usando a função `get_string()`. Esses valores são armazenados dentro das variáveis `word1` e `word2`.
- Em `compute_score()`, seu programa deve calcular, usando o array `POINTS`, e retornar a pontuação para o argumento do tipo string. Os caracteres que não são letras devem receber zero pontos, e letras maiúsculas e minúsculas devem receber os mesmos valores de pontuação.
  - Por exemplo, `!` vale 0 ponto, enquanto `A` e `a` valem ambos 1 ponto.
  - Embora as regras do Scrabble normalmente exijam que uma palavra esteja no dicionário, não é necessário verificar isso neste problema!
- Em `main()`, seu programa deve imprimir, dependendo das pontuações dos jogadores, `Jogador 1 ganha!`, `Jogador 2 ganha!` ou `Empate!`.

### Passo a Passo

<div class="alert" data-alert="primary" role="alert"><p>Este vídeo foi gravado quando o curso ainda usava o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu codespace, o comportamento dos dois ambientes deve ser em grande parte semelhante!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/RtjxxxlN1gc"></iframe>

### Sugestões

- Você pode achar as funções `isupper()` e `islower()` úteis. Essas funções recebem um caractere como argumento e retornam um valor booleano.
- Para encontrar o valor no enésimo índice de uma matriz chamada `arr`, podemos escrever `arr[n]`. Podemos aplicar isso a strings também, pois elas são matrizes de caracteres.
- Lembre-se de que os computadores representam caracteres usando [ASCII] (https://asciitable.com/), um padrão que representa cada caractere como um número.

<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/USiLkXuXJEg"></iframe></details>

### Como Testar o Seu Código

Seu programa deve se comportar conforme os exemplos abaixo.

```
$ ./scrabble
Jogador 1: Question?
Jogador 2: Question!
Empate!
```

```
$ ./scrabble
Jogador 1: Oh,
Jogador 2: hai!
Jogador 2 ganha!
```

```
$ ./scrabble
Jogador 1: COMPUTADOR
Jogador 2: ciência
Jogador 1 ganha!
```

```
$ ./scrabble
Jogador 1: Scrabble
Jogador 2: wiNNeR
Jogador 1 ganha!
```

Execute o código abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo também!

    check50 cs50/labs/2023/x/scrabble

Execute o código abaixo para avaliar o estilo do seu código usando `style50`.

    style50 scrabble.c

## Como Enviar

No seu terminal, execute o código abaixo para enviar o seu trabalho.

    submit50 cs50/labs/2023/x/scrabble