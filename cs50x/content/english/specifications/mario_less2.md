## Pseudocode

First, execute

    cd

to ensure you’re in your codespace’s default directory.

Then, execute

    cd mario-less

to change to your `mario-less` directory.

Then, execute

    code pseudocode.txt

to open the file called `pseudocode.txt` inside that directory.

Write in `pseudocode.txt` some pseudocode that implements this program, even if not (yet!) sure how to write it in code. There’s no one right way to write pseudocode, but short English sentences suffice. Recall how we wrote [pseudocode for finding someone in a phone book](https://docs.google.com/presentation/d/1X3AMSenwZGSE6WxGpzoALAfMg2hmh1LYIJp3N2a1EYI/edit#slide=id.g41907da2bc_0_265). Odds are your pseudocode will use (or imply using!) one or more functions, conditionals, Boolean expressions, loops, and/or variables.

<details><summary>Spoiler</summary><p>There’s more than one way to do this, so here’s just one!</p>

<ol>
  <li>Prompt user for height</li>
  <li>If height is less than 1 or greater than 8 (or not an integer at all), go back one step</li>
  <li>Iterate from 1 through height:
    <ol>
      <li>On iteration <em>i</em>, print <em>i</em> hashes and then a newline</li>
    </ol>
  </li>
</ol>

<p>It’s okay to edit your own after seeing this pseudocode here, but don’t simply copy/paste ours into your own!</p></details>

## Prompting for Input

Whatever your pseudocode, let’s first write only the C code that prompts (and re-prompts, as needed) the user for input. Open the file called `mario.c` inside of your `mario` directory. (Remember how?)

Now, modify `mario.c` in such a way that it prompts the user for the pyramid’s height, storing their input in a variable, re-prompting the user again and again as needed if their input is not a positive integer between 1 and 8, inclusive. Then, simply print the value of that variable, thereby confirming (for yourself) that you’ve indeed stored the user’s input successfully, a la the below.

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
    Stored: 4

<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that you can compile your program with <code class="language-plaintext highlighter-rouge">make</code>.</li>
  <li data-marker="*">Recall that you can print an <code class="language-plaintext highlighter-rouge">int</code> with <code class="language-plaintext highlighter-rouge">printf</code> using <code class="language-plaintext highlighter-rouge">%i</code>.</li>
  <li data-marker="*">Recall that you can get an integer from the user with <code class="language-plaintext highlighter-rouge">get_int</code>.</li>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">get_int</code> is declared in <code class="language-plaintext highlighter-rouge">cs50.h</code>.</li>
  <li data-marker="*">Recall that we prompted the user for a positive integer in lecture using a <code class="language-plaintext highlighter-rouge">do while</code> loop in <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight"><code class="language-plaintext highlighter-rouge">mario.c</code></a>.</li>
</ul></details>
