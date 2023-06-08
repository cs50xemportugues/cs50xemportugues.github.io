### Passo a passo

<div class="alert" data-alert="primary" role="alert"><p>Esse vídeo foi gravado quando o curso ainda usava o IDE CS50 para escrever código. Embora a interface possa parecer diferente do seu codespace, o comportamento dos dois ambientes deve ser amplamente semelhante!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/o5Bkc7gtRjo"></iframe>


### Dicas

*   Ao ler o arquivo, você pode achar essa sintaxe útil, com `nome_arquivo` como o nome do seu arquivo e `arquivo` uma variável: <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">with</span> <span class="nf">open</span><span class="p">(</span><span class="n">nome_arquivo</span><span class="p">)</span> <span class="k">as</span> <span class="nb">arquivo</span><span class="p">:</span>
      <span class="n">    leitor</span> <span class="o">=</span> <span class="n">csv</span><span class="p">.</span><span class="nc">DictReader</span><span class="p">(</span><span class="nb">arquivo</span><span class="p">)</span>
</code></pre></div>    </div>
        
    
*   Em Python, para acrescentar algo ao final de uma lista, use a função `.append()`.
    

<details><summary>Não tem certeza sobre como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/Fo7Roe8hw3A"></iframe></details>


### Testando

Seu programa deve se comportar conforme os exemplos abaixo. Como as simulações têm aleatoriedade em cada uma, a saída provavelmente não corresponderá perfeitamente aos exemplos abaixo.

    $ python tournament.py 2018m.csv
    Bélgica: 20,9% de chance de vencer
    Brasil: 20,3% de chance de vencer
    Portugal: 14,5% de chance de vencer
    Espanha: 13,6% de chance de vencer
    Suíça: 10,5% de chance de vencer
    Argentina: 6,5% de chance de vencer
    Inglaterra: 3,7% de chance de vencer
    França: 3,3% de chance de vencer
    Dinamarca: 2,2% de chance de vencer
    Croácia: 2,0% de chance de vencer
    Colômbia: 1,8% de chance de vencer
    Suécia: 0,5% de chance de vencer
    Uruguai: 0,1% de chance de vencer
    México: 0,1% de chance de vencer
    

    $ python tournament.py 2019w.csv
    Alemanha: 17,1% de chance de vencer
    Estados Unidos: 14,8% de chance de vencer
    Inglaterra: 14,0% de chance de vencer
    França: 9,2% de chance de vencer
    Canadá: 8,5% de chance de vencer
    Japão: 7,1% de chance de vencer
    Austrália: 6,8% de chance de vencer
    Países Baixos: 5,4% de chance de vencer
    Suécia: 3,9% de chance de vencer
    Itália: 3,0% de chance de vencer
    Noruega: 2,9% de chance de vencer
    Brasil: 2,9% de chance de vencer
    Espanha: 2,2% de chance de vencer
    China PR: 2,1% de chance de vencer
    Nigéria: 0,1% de chance de vencer
    

*   Você pode estar se perguntando o que aconteceu de verdade nas Copas do Mundo de 2018 e 2019. No campeonato masculino, a França ganhou, derrotando a Croácia na final. A Bélgica derrotou a Inglaterra para ficar em terceiro lugar. No campeonato feminino, os Estados Unidos ganharam, derrotando os Países Baixos na final. A Inglaterra derrotou a Suécia para ficar em terceiro lugar.