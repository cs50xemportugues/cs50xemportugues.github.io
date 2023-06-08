
Specification
-------------

Design and implement a program, `bulbs`, that converts text into instructions for the strip of bulbs on CS50’s stage as follows:

*   Implement your program in a file called `bulbs.c`.
*   Your program must first ask the user for a message using `get_string`.
*   Your program must then convert the given `string` into a series of 8-bit binary numbers, one for each character of the string.
*   You can use the provided `print_bulb` function to print a series of `0`s and `1`s as a series of yellow and black emoji, which represent on and off light bulbs.
*   Each “byte” of 8 symbols should be printed on its own line when outputted; there should be a `\n` after the last “byte” of 8 symbols as well.

<details><summary>Hints for Decimal-to-Binary</summary><p>Let’s walk through an example with the number 4. How would you convert 4 to binary? Start by considering the right-most bit, that which—if on—adds 1 to the number we’re representing. Do you need this bit to be on? Divide 4 by 2 to find out:</p>

`4 / 2 = 2`

<p>2 divides evenly into 4, which tells us there’s no remainder of 1 to worry about. We can safely leave this right-most bit off, then:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>0
</code></pre></div></div>

<p>What about the preceding bit, now, the one just the left of this bit we discovered? To check, let’s follow a similar process, but pick up where we left off. In the previous step, we divided 4 by 2 and got 2. Now, does 2 divide evenly into 2? It does, so there’s no remainder of 2 to worry about:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>00
</code></pre></div></div>

<p>Let’s continue further still. After dividing 2 by 2, we’re left with 1. Diving 1 by 2 leaves a remainder of 1. That means we’ll need to turn this bit on:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>100
</code></pre></div></div>

<p>And now that we’ve divided our number down to 0, we need no further bits to represent it. Notice that we discovered the bits to represent 4 in the opposite order in which we need to print them: we’ll likely need a structure that lets us store these bits, so we can print them forwards later on. And, of course, in your actual code, you’ll be working with <code class="language-plaintext highlighter-rouge">char</code>s of 8 bits, so you’ll want to prepend any needed 0’s.</p>

<p>When checking for remainders, the modulo (<code class="language-plaintext highlighter-rouge">%</code>) operator may come in handy! <code class="language-plaintext highlighter-rouge">4 % 2</code>, for example, returns 0, meaning that 2 divides into 4 with a remainder of 0.</p></details>

