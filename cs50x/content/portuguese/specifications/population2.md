### Dicas

- Se você deseja re-pedir repetidamente ao usuário o valor de uma variável até que alguma condição seja atendida, pode ser útil usar um loop `do… while`. Por exemplo, relembre o seguinte código da aula, que solicita o usuário repetidamente até que ele digite um número inteiro positivo. <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">n</span><span class="p">;</span>
  <span class="k">do</span>
  <span class="p">{</span>
  <span class="n">n</span> <span class="o">=</span> <span class="n">get_int</span><span class="p">(</span><span class="s">"Positive Integer: "</span><span class="p">);</span>
  <span class="p">}</span>
  <span class="k">while</span> <span class="p">(</span><span class="n">n</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">);</span>
  </code></pre></div> </div>
  Como você pode adaptar este código para garantir um tamanho inicial de pelo menos 9 e um tamanho final de pelo menos o tamanho inicial?

* Para declarar uma nova variável, certifique-se de especificar seu tipo de dados, um nome para a variável e (opcionalmente) qual deve ser seu valor inicial.
  - Por exemplo, você pode querer criar uma variável para acompanhar quantos anos se passaram.
* Para calcular quantos anos levará para a população atingir o tamanho final, outro loop pode ser útil! Dentro do loop, você provavelmente desejará atualizar o tamanho da população de acordo com a fórmula no Contexto e atualizar o número de anos que se passaram.
* Para imprimir um inteiro `n` no terminal, lembre-se de que você pode usar uma linha de código como <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code> <span class="n">printf</span><span class="p">(</span><span class="s">"The number is %i</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">n</span><span class="p">);</span>
  </code></pre></div> </div>
  para especificar que a variável `n` deve ser preenchida no espaço reservado `% i`.

### Como testar seu código

Seu programa deve se comportar de acordo com os exemplos abaixo.

    $ ./population
    Tamanho inicial: 1200
    Tamanho final: 1300
    Anos: 1


    $ ./population
    Tamanho inicial: -5
    Tamanho inicial: 3
    Tamanho inicial: 9
    Tamanho final: 5
    Tamanho final: 18
    Anos: 8


    $ ./population
    Tamanho inicial: 20
    Tamanho final: 1
    Tamanho final: 10
    Tamanho final: 100
    Anos: 20


    $ ./population
    Tamanho inicial: 100
    Tamanho final: 1000000
    Anos: 115

<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/2CcqQnLbGOE"></iframe></details>

Execute o seguinte para avaliar a correção do código usando o `check50`. Mas verifique se você compilou e testou o código também!

    check50 cs50/labs/2023/x/population

Execute o seguinte para avaliar o estilo do código usando o `style50`.

    style50 population.c

## Como Enviar

No terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/labs/2023/x/population
