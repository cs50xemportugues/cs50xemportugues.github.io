Número de simulações
---------------------

Depois de ter certeza de que seu código está correto, vamos brincar com o valor de `N`, constante no topo do arquivo, para ajustar o número de vezes que simulamos o torneio. Mais simulações de torneios nos darão previsões mais precisas (por quê?), mas ao custo de tempo.

Podemos cronometrar programas adicionando sua execução na linha de comando com `time`. Por exemplo, com `N` ajustado para 1000 (o padrão), execute

    time python tournament.py 2018m.csv
    

ou

    time python tournament.py 2019w.csv
    

o que deve produzir algo como

    real    0m0.037s
    user    0m0.028s
    sys     0m0.008s
    

embora seus próprios tempos possam variar.

Preste atenção na métrica **real**, que é o tempo total que `tournament.py` levou para ser executado. E observe que você recebe o tempo em minutos e segundos, com precisão de milésimos de segundo.

No arquivo `answers.txt`, acompanhe quanto tempo leva para `tournament.py` simular...

*   10 (dez) torneios
*   100 (cem) torneios
*   1000 (mil) torneios
*   10000 (dez mil) torneios
*   100000 (cem mil) torneios
*   1000000 (um milhão) de torneios

Cada vez que você ajustar `N`, registre o tempo **real** na tarefa correspondente em `answers.txt`, usando o mesmo formato `0m0.000s`. Depois de cronometrar cada cenário, responda às duas perguntas de acompanhamento, sobrescrevendo a tarefa fornecida:

*   Quais previsões, se houver, se mostraram incorretas à medida que você aumentou o número de simulações?
*   Suponha que você seja cobrado por cada segundo do tempo de computação que seu programa usa. Depois de quantas simulações você consideraria as previsões "suficientemente boas"?

<details><summary>Veja um arquivo <code>answers.txt</code> formatado corretamente</summary><div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Tempos:

10 simulações: 0m0.028s
100 simulações: 0m0.030s
1000 simulações: 0m0.041s
10000 simulações: 0m0.139s
100000 simulações: 0m1.031s
1000000 simulações: 0m11.961s

Perguntas:

Quais previsões, se houver, se mostraram incorretas à medida que você aumentou o número de simulações?:

Com um pequeno número de simulações...

Suponha que você seja cobrado por cada segundo do tempo de computação que seu programa usa. Depois de quantas simulações você consideraria as previsões "suficientemente boas"?:

Parece que as previsões se estabilizaram depois de cerca de...

</code></pre></div></div></details>