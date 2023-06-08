## Building the Opposite

Now that your program is (hopefully!) accepting input as prescribed, it’s time for another step.

It turns out it’s a bit easier to build a left-aligned pyramid than right-, a la the below.

    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########

So let’s build a left-aligned pyramid first and then, once that’s working, right-align it instead!

Modify `mario.c` at right such that it no longer simply prints the user’s input but instead prints a left-aligned pyramid of that height.

<details>
  <summary>Hints</summary>
  <ul>
    <li data-marker="*">Keep in mind that a hash is just a character like any other, so you can print it with <code class="language-plaintext highlighter-rouge">printf</code>.</li>
    <li data-marker="*">Just as Scratch has a <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">repeat</code></a> block, so does C have a <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">for</code></a> loop, via which you can iterate some number times. Perhaps on each iteration, <em>i</em>, you could print that many hashes?</li>
    <li data-marker="*">
      <p>You can actually “nest” loops, iterating with one variable (e.g., <code class="language-plaintext highlighter-rouge">i</code>) in the “outer” loop and another (e.g., <code class="language-plaintext highlighter-rouge">j</code>) in the “inner” loop. For instance, here’s how you might print a square of height and width <code class="language-plaintext highlighter-rouge">n</code>, below. Of course, it’s not a square that you want to print!</p>

      <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  for (int i = 0; i &lt; n; i++)

      {
      for (int j = 0; j &lt; n; j++)
      {
      printf("#");
      }
      printf("\n");
      }
      </code></pre></div> </div>

</li>
  </ul>
</details>

## Right-Aligning with Dots

Let’s now right-align that pyramid by pushing its hashes to the right by prefixing them with dots (i.e., periods), a la the below.

    .......#
    ......##
    .....###
    ....####
    ...#####
    ..######
    .#######
    ########

Modify `mario.c` in such a way that it does exactly that!

<details><summary>Hint</summary><p>Notice how the number of dots needed on each line is the “opposite” of the number of that line’s hashes. For a pyramid of height 8, like the above, the first line has but 1 hash and thus 7 dots. The bottom line, meanwhile, has 8 hashes and thus 0 dots. Via what formula (or arithmetic, really) could you print that many dots?</p></details>

### How to Test Your Code

Does your code work as prescribed when you input

- `-1` (or other negative numbers)?
- `0`?
- `1` through `8`?
- `9` or other positive numbers?
- letters or words?
- no input at all, when you only hit Enter?

## Removing the Dots

All that remains now is a finishing flourish! Modify `mario.c` in such a way that it prints spaces instead of those dots!

### How to Test Your Code

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/problems/2023/x/mario/less

Execute the below to evaluate the style of your code using `style50`.

    style50 mario.c

<details><summary>Hint</summary><p>A space is just a press of your space bar, just as a period is just a press of its key! Just remember that <code class="language-plaintext highlighter-rouge">printf</code> requires that you surround both with double quotes!</p></details>

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/mario/less
