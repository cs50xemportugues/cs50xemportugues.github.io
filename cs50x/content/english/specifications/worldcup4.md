
### Walkthrough

<div class="alert" data-alert="primary" role="alert"><p>This video was recorded when the course was still using CS50 IDE for writing code. Though the interface may look different from your codespace, the behavior of the two environments should be largely similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/o5Bkc7gtRjo"></iframe>


### Hints

*   When reading in the file, you may find this syntax helpful, with `filename` as the name of your file and `file` as a variable. <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">with</span> <span class="nf">open</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="k">as</span> <span class="nb">file</span><span class="p">:</span>
      <span class="n">    reader</span> <span class="o">=</span> <span class="n">csv</span><span class="p">.</span><span class="nc">DictReader</span><span class="p">(</span><span class="nb">file</span><span class="p">)</span>
</code></pre></div>    </div>
        
    
*   In Python, to append to the end of a list, use the `.append()` function.
    

<details><summary>Not sure how to solve?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/Fo7Roe8hw3A"></iframe></details>


### Testing

Your program should behave per the examples below. Since simulations have randomness within each, your output will likely not perfectly match the examples below.

    $ python tournament.py 2018m.csv
    Belgium: 20.9% chance of winning
    Brazil: 20.3% chance of winning
    Portugal: 14.5% chance of winning
    Spain: 13.6% chance of winning
    Switzerland: 10.5% chance of winning
    Argentina: 6.5% chance of winning
    England: 3.7% chance of winning
    France: 3.3% chance of winning
    Denmark: 2.2% chance of winning
    Croatia: 2.0% chance of winning
    Colombia: 1.8% chance of winning
    Sweden: 0.5% chance of winning
    Uruguay: 0.1% chance of winning
    Mexico: 0.1% chance of winning
    

    $ python tournament.py 2019w.csv
    Germany: 17.1% chance of winning
    United States: 14.8% chance of winning
    England: 14.0% chance of winning
    France: 9.2% chance of winning
    Canada: 8.5% chance of winning
    Japan: 7.1% chance of winning
    Australia: 6.8% chance of winning
    Netherlands: 5.4% chance of winning
    Sweden: 3.9% chance of winning
    Italy: 3.0% chance of winning
    Norway: 2.9% chance of winning
    Brazil: 2.9% chance of winning
    Spain: 2.2% chance of winning
    China PR: 2.1% chance of winning
    Nigeria: 0.1% chance of winning
    

*   You might be wondering what actually happened at the 2018 and 2019 World Cups! For Men’s, France won, defeating Croatia in the final. Belgium defeated England for the third place position. For Women’s, the United States won, defeating the Netherlands in the final. England defeated Sweden for the third place position.