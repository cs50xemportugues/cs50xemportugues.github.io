
### Using the Key

Now modify `main` in such a way that it converts `argv[1]` to an `int`. You might find `atoi`, declared in `stdlib.h`, to be helpful, per [manual.cs50.io](https://manual.cs50.io/). And then use `get_string` to prompt the user for some plaintext with `"plaintext: "`.

Then, implement a function called, e.g., `rotate`, that takes a `char` as input and also an `int`, and rotates that `char` by that many positions if it’s a letter (i.e., alphabetical), wrapping around from `Z` to `A` (and from `z` to `a`) as needed. If the `char` is not a letter, the function should instead return the same `char` unchanged.


<details><summary>Hints</summary><ul>
  <li data-marker="*">Odds are you’ll want a prototype like:
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">char</span> <span class="nf">rotate</span><span class="p">(</span><span class="kt">char</span> <span class="n">c</span><span class="p">,</span> <span class="kt">int</span> <span class="n">n</span><span class="p">);</span>
</code></pre></div>    </div>
    <p>A function call like</p>
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">rotate</span><span class="p">(</span><span class="sc">'A'</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>or even</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>rotate('A', 27)
</code></pre></div>    </div>
    <p>should thus return <code class="language-plaintext highlighter-rouge">'B'</code>. And a function call like</p>
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">rotate</span><span class="p">(</span><span class="sc">'!'</span><span class="p">,</span> <span class="mi">13</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>should return <code class="language-plaintext highlighter-rouge">'!'</code>.</p>
  </li>
  <li data-marker="*">Recall that you can explicitly “cast” a <code class="language-plaintext highlighter-rouge">char</code> to an <code class="language-plaintext highlighter-rouge">int</code> with <code class="language-plaintext highlighter-rouge">(char)</code>, and an <code class="language-plaintext highlighter-rouge">int</code> to a <code class="language-plaintext highlighter-rouge">char</code> with <code class="language-plaintext highlighter-rouge">(int)</code>. Or you can do so implicitly by simply treating one as the other.</li>
  <li data-marker="*">Odds are you’ll want to subtract the ASCII value of <code class="language-plaintext highlighter-rouge">'A'</code> from any uppercase letters, so as to treat <code class="language-plaintext highlighter-rouge">'A'</code> as <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">'B'</code> as <code class="language-plaintext highlighter-rouge">1</code>, and so forth, while performing arithmetic. And then add it back when done with the same.</li>
  <li data-marker="*">Odds are you’ll want to subtract the ASCII value of <code class="language-plaintext highlighter-rouge">'a'</code> from any lowercase letters, so as to treat <code class="language-plaintext highlighter-rouge">'a'</code> as <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">'b'</code> as <code class="language-plaintext highlighter-rouge">1</code>, and so forth, while performing arithmetic. And then add it back when done with the same.</li>
  <li data-marker="*">You might find some other functions declared in <code class="language-plaintext highlighter-rouge">ctype.h</code> to be helpful, per <a href="https://manual.cs50.io/">manual.cs50.io</a>.</li>
  <li data-marker="*">Odds are you’ll find <code class="language-plaintext highlighter-rouge">%</code> helpful when “wrapping around” arithmetically from a value like <code class="language-plaintext highlighter-rouge">25</code> to <code class="language-plaintext highlighter-rouge">0</code>.</li>
</ul></details>

Then modify `main` in such a way that it prints `"ciphertext: "` and then iterates over every `char` in the user’s plaintext, calling `rotate` on each, and printing the return value thereof.

<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">printf</code> can print a <code class="language-plaintext highlighter-rouge">char</code> using <code class="language-plaintext highlighter-rouge">%c</code>.</li>
  <li data-marker="*">If you’re not seeing any output at all when you call <code class="language-plaintext highlighter-rouge">printf</code>, odds are it’s because you’re printing characters outside of the valid ASCII range from 0 to 127. Try printing characters temporarily as numbers (using <code class="language-plaintext highlighter-rouge">%i</code> instead of <code class="language-plaintext highlighter-rouge">%c</code>) to see what values you’re printing!</li>
</ul></details>

