### Hints

- If you want to repeatedly re-prompt the user for the value of a variable until some condition is met, you might want to use a `do ... while` loop. For example, recall the following code from lecture, which prompts the user repeatedly until they enter a positive integer. <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">n</span><span class="p">;</span>
  <span class="k">do</span>
  <span class="p">{</span>
  <span class="n">n</span> <span class="o">=</span> <span class="n">get_int</span><span class="p">(</span><span class="s">"Positive Integer: "</span><span class="p">);</span>
  <span class="p">}</span>
  <span class="k">while</span> <span class="p">(</span><span class="n">n</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">);</span>
  </code></pre></div> </div>
  How might you adapt this code to ensure a start size of at least 9, and an end size of at least the start size?

* To declare a new variable, be sure to specify its data type, a name for the variable, and (optionally) what its initial value should be.
  - For example, you might want to create a variable to keep track of how many years have passed.
* To calculate how many years it will take for the population to reach the end size, another loop might be helpful! Inside the loop, you’ll likely want to update the population size according to the formula in the Background, and update the number of years that have passed.
* To print an integer `n` to the terminal, recall that you can use a line of code like <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code> <span class="n">printf</span><span class="p">(</span><span class="s">"The number is %i</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">n</span><span class="p">);</span>
  </code></pre></div> </div>
  to specify that the variable `n` should fill in for the placeholder `%i`.

### How to Test Your Code

Your program should behave per these examples below.

    $ ./population
    Start size: 1200
    End size: 1300
    Years: 1


    $ ./population
    Start size: -5
    Start size: 3
    Start size: 9
    End size: 5
    End size: 18
    Years: 8


    $ ./population
    Start size: 20
    End size: 1
    End size: 10
    End size: 100
    Years: 20


    $ ./population
    Start size: 100
    End size: 1000000
    Years: 115

<details><summary>Not sure how to solve?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/2CcqQnLbGOE"></iframe></details>

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/labs/2023/x/population

Execute the below to evaluate the style of your code using `style50`.

    style50 population.c

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/labs/2023/x/population
