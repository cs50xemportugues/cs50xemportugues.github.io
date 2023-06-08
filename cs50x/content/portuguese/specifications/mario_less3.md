## Construindo o Contrário

Agora que seu programa está (esperançosamente!) aceitando a entrada como prescrita, é hora de dar outro passo.

Acontece que é um pouco mais fácil construir uma pirâmide alinhada à esquerda do que à direita, como abaixo.

    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########

Então, vamos construir uma pirâmide alinhada à esquerda primeiro e, depois que funcionar, alinhá-la à direita!

Modifique o arquivo `mario.c` de forma que não imprima mais a entrada do usuário, mas em vez disso imprima uma pirâmide de altura alinhada à esquerda.

<details>
  <summary>Dicas</summary>
  <ul>
    <li data-marker="*">Lembre-se de que um hash é apenas um caractere como qualquer outro, portanto, você pode imprimi-lo com <code class="language-plaintext highlighter-rouge">printf</code>.</li>
    <li data-marker="*">Assim como o Scratch tem um bloco <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">repeat</code></a>, o C também tem um loop <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">for</code></a>, por meio do qual você pode iterar algumas vezes. Talvez em cada iteração, <em>i</em>, você pudesse imprimir tantos hashes?</li>
    <li data-marker="*">
      <p>Na verdade, você pode “aninhar” loops, iterando com uma variável (por exemplo, <code class="language-plaintext highlighter-rouge">i</code>) no loop "externo" e outra (por exemplo, <code class="language-plaintext highlighter-rouge">j</code>) no loop "interno". Por exemplo, aqui está como você pode imprimir um quadrado de altura e largura <code class="language-plaintext highlighter-rouge">n</code>, abaixo. Claro, não é um quadrado que você deseja imprimir!</p>

      <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  for (int i = 0; i &lt; n; i++)

      {
      for (int j = 0; j &lt; n; j++)
        {
          printf("#");
        }
        printf("\n");
      }
      </code></pre></div> </div>

</li>
  </ul>
</details>

## Alinhando à Direita com Pontos

Agora vamos alinhar à direita essa pirâmide empurrando seus hashes para a direita, prefixando-os com pontos (ou seja, períodos), como abaixo.

    .......#
    ......##
    .....###
    ....####
    ...#####
    ..######
    .#######
    ########

Modifique `mario.c` de forma que ele faça exatamente isso!

<details><summary>Dica</summary><p>Observe como o número de pontos necessários em cada linha é o “oposto” do número de hashes daquela linha. Para uma pirâmide de altura 8, como a acima, a primeira linha tem apenas 1 hash e, portanto, 7 pontos. Enquanto isso, a linha inferior tem 8 hashes e assim 0 pontos. Através de que fórmula (ou aritmética, realmente) você poderia imprimir tantos pontos?</p></details>

### Como Testar seu Código

O seu código funciona conforme prescrito quando você insere:

- `-1` (ou outros números negativos)?
- `0`?
- De `1` a `8`?
- `9` ou outros números positivos?
- letras ou palavras?
- nenhuma entrada, quando você só pressiona Enter?

## Removendo os Pontos

Tudo o que resta agora é um acabamento! Modifique `mario.c` de tal maneira que ele imprima espaços em vez desses pontos!

### Como Testar seu Código

Execute o abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo também!

    check50 cs50/problems/2023/x/mario/less

Execute o abaixo para avaliar o estilo do seu código usando `style50`.

    style50 mario.c

<details><summary>Dica</summary><p>Um espaço é apenas uma tecla pressionada em sua barra de espaço, assim como um ponto é apenas uma tecla pressionada em sua tecla! Mas lembre-se de que <code class="language-plaintext highlighter-rouge">printf</code> requer que você envolva as duas com aspas duplas!</p></details>

## Como Enviar

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/mario/less
"