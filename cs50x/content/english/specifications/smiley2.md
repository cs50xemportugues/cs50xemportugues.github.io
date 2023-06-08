
How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/labs/2023/x/smiley
    

<details><summary>Want to see the staff's solution?</summary><div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">#include</span> <span class="cpf">"helpers.h"</span><span class="cp">
</span>
<span class="kt">void</span> <span class="nf">colorize</span><span class="p">(</span><span class="kt">int</span> <span class="n">height</span><span class="p">,</span> <span class="kt">int</span> <span class="n">width</span><span class="p">,</span> <span class="n">RGBTRIPLE</span> <span class="n">image</span><span class="p">[</span><span class="n">height</span><span class="p">][</span><span class="n">width</span><span class="p">])</span>
<span class="p">{</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">height</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span>
    <span class="p">{</span>
        <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">width</span><span class="p">;</span> <span class="n">j</span><span class="o">++</span><span class="p">)</span>
        <span class="p">{</span>
            <span class="c1">// Make black pixels turn red</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtRed</span> <span class="o">==</span> <span class="mh">0x00</span> <span class="o">&amp;&amp;</span> <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtGreen</span> <span class="o">==</span> <span class="mh">0x00</span> <span class="o">&amp;&amp;</span> <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtBlue</span> <span class="o">==</span> <span class="mh">0x00</span><span class="p">)</span>
            <span class="p">{</span>
                <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtRed</span> <span class="o">=</span> <span class="mh">0xff</span><span class="p">;</span>
            <span class="p">}</span>
        <span class="p">}</span>
    <span class="p">}</span>
<span class="p">}</span>
</code></pre></div></div></details>