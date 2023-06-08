
### Counting Command-Line Arguments

Whatever your pseudocode, let’s first write only the C code that checks whether the program was run with a single command-line argument before adding additional functionality.

Specifically, modify `main` in `caesar.c` in such a way that, if the user provides no command-line arguments, or two or more, the function prints `"Usage: ./caesar key\n"` and then returns `1`, effectively exiting the program. If the user provides exactly one command-line argument, the program should print nothing and simply return `0`. The program should thus behave per the below.

    $ ./caesar
    Usage: ./caesar key


    $ ./caesar 1 2 3
    Usage: ./caesar key


    $ ./caesar 1

<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that you can print with <code class="language-plaintext highlighter-rouge">printf</code>.</li>
  <li data-marker="*">Recall that a function can return a value with <code class="language-plaintext highlighter-rouge">return</code>.</li>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">argc</code> contains the number of command-line arguments passed to a program, plus the program’s own name.</li>
</ul></details>

### Checking the Key

Now that your program is (hopefully!) accepting input as prescribed, it’s time for another step.

Add to `caesar.c`, below `main`, a function called, e.g., `only_digits` that takes a `string` as an argument and returns `true` if that `string` contains only digits, `0` through `9`, else it returns `false`. Be sure to add the function’s prototype above `main` as well.

<details><summary>Hints</summary><ul>
  <li data-marker="*">Odds are you’ll want a prototype like:
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">only_digits</span><span class="p">(</span><span class="n">string</span> <span class="n">s</span><span class="p">);</span>
</code></pre></div>    </div>
    <p>And be sure to include <code class="language-plaintext highlighter-rouge">cs50.h</code> atop your file, so that the compiler recognizes <code class="language-plaintext highlighter-rouge">string</code> (and <code class="language-plaintext highlighter-rouge">bool</code>).</p>
  </li>
  <li data-marker="*">Recall that a <code class="language-plaintext highlighter-rouge">string</code> is just an array of <code class="language-plaintext highlighter-rouge">char</code>s.</li>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">strlen</code>, declared in <code class="language-plaintext highlighter-rouge">string.h</code>, calculates the length of a <code class="language-plaintext highlighter-rouge">string</code>.</li>
  <li data-marker="*">You might find <code class="language-plaintext highlighter-rouge">isdigit</code>, declared in <code class="language-plaintext highlighter-rouge">ctype.h</code>, to be helpful, per <a href="https://manual.cs50.io/">manual.cs50.io</a>. But note that it only checks one <code class="language-plaintext highlighter-rouge">char</code> at a time!</li>
</ul></details>


Then modify `main` in such a way that it calls `only_digits` on `argv[1]`. If that function returns `false`, then `main` should print `"Usage: ./caesar key\n"` and return `1`. Else `main` should simply return `0`. The program should thus behave per the below:

```
$ ./caesar 42
```
```
$ ./caesar banana
Usage: ./caesar key
```