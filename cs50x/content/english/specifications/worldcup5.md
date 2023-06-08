
Number of Simulations
---------------------

Once you’re sure your code is correct, let’s tinker with the value of `N`, the constant at the top of our file, to adjust the number of times we simulate the tournament. More tournament simulations will give us more accurate predictions (why?), at the cost of time.

We can time programs by prepending their execution at the command-line with `time`. For example, with `N` set to 1000 (the default) execute

    time python tournament.py 2018m.csv
    

or

    time python tournament.py 2019w.csv
    

which should output something like

    real    0m0.037s
    user    0m0.028s
    sys     0m0.008s
    

though your own times might vary.

Pay attention to the **real** metric, which is the time, in total, it took `tournament.py` to run. And notice that you’re given time in minutes and seconds, with accuracy to thousandths of a second.

In `answers.txt`, keep track of how long it takes `tournament.py` to simulate…

*   10 (ten) tournaments
*   100 (one hundred) tournaments
*   1000 (one thousand) tournaments
*   10000 (ten thousand) tournaments
*   100000 (one hundred thousand) tournaments
*   1000000 (one million) tournaments

Each time you adjust `N`, record the **real** time in the appropriate TODO in `answers.txt` by using the same `0m0.000s` format. After timing each scenario, answer the two follow-up questions by overwriting the given TODO:

*   Which predictions, if any, proved incorrect as you increased the number of simulations?
*   Suppose you’re charged a fee for each second of compute time your program uses. After how many simulations would you call the predictions “good enough”?


<details><summary>See a correctly formatted <code>answers.txt</code></summary><div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Times:

10 simulations: 0m0.028s
100 simulations: 0m0.030s
1000 simulations: 0m0.041s
10000 simulations: 0m0.139s
100000 simulations: 0m1.031s
1000000 simulations: 0m11.961s

Questions:

Which predictions, if any, proved incorrect as you increased the number of simulations?:

With a small number of simulations...

Suppose you're charged a fee for each second of compute time your program uses.
After how many simulations would you call the predictions "good enough"?:

It seems like the predictions stabilized after about...

</code></pre></div></div></details>