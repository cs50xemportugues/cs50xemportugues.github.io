
### Sentences

The last piece of information that the Coleman-Liau formula cares about, in addition to the number of letters and words, is the number of sentences. Determining the number of sentences can be surprisingly trickly. You might first imagine that a sentence is just any sequence of characters that ends with a period, but of course sentences could end with an exclamation point or a question mark as well. But of course, not all periods necessarily mean the sentence is over. For instance, consider the sentence below.

    Mr. and Mrs. Dursley, of number four Privet Drive, were proud to say that they were perfectly normal, thank you very much.

This is just a single sentence, but there are three periods! For this problem, we’ll ask you to ignore that subtlety: you should consider any sequence of characters that ends with a `.` or a `!` or a `?` to be a sentence (so for the above “sentence”, you should count it as three sentences). In practice, sentence boundary detection needs to be a little more intelligent to handle these cases, but we’ll not worry about that for now.

Add to `readability.c`, below `main`, a function called `count_sentences` that takes one argument, a `string` of text, and that returns an `int`, the number of sentences in that text. Be sure to add the function’s prototype, too, atop your file, so that `main` knows how to call it. (We again leave its prototype to you!)

Then call that function in `main` so that your program also prints the number of sentences in the text.

The program should now behave per the below.

    $ ./readability
    Text: When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.
    295 letters
    70 words
    3 sentences

### Putting it All Together

Now it’s time to put all the pieces together! Recall that the Coleman-Liau index is computed using the formula:

    index = 0.0588 * L - 0.296 * S - 15.8

where `L` is the average number of letters per 100 words in the text, and `S` is the average number of sentences per 100 words in the text.

Modify `main` in `readability.c` so that instead of outputting the number of letters, words, and sentences, it instead outputs (only) the grade level as defined by the Coleman-Liau index (e.g. `"Grade 2"` or `"Grade 8" or the like`). Be sure to round the resulting index number to the nearest `int`!

<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">round</code> is declared in <code class="language-plaintext highlighter-rouge">math.h</code>, per <a href="https://manual.cs50.io/">manual.cs50.io</a>!</li>
  <li data-marker="*">Recall that, when dividing values of type <code class="language-plaintext highlighter-rouge">int</code> in C, the result will also be an <code class="language-plaintext highlighter-rouge">int</code>, with any remainder (i.e., digits after the decimal point) discarded. Put another way, the result will be “truncated.” You might want to cast your one or more values to <code class="language-plaintext highlighter-rouge">float</code> before performing division when calculating <code class="language-plaintext highlighter-rouge">L</code> and <code class="language-plaintext highlighter-rouge">S</code>!</li>
</ul></details>

If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output `"Grade 16+"` instead of outputting an exact index number. If the index number is less than 1, your program should output `"Before Grade 1"`.
