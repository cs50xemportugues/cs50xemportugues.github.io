
### Getting User Input

Let’s first write some C code that just gets some text input from the user, and prints it back out. Specifically, implement in `readability.c` a `main` function that prompts the user with `"Text: "` using `get_string` and then prints that same text using `printf`. And remember, as you work through this program, that if you make use of any library functions, be sure to `#include` any corresponding header files.

The program should behave per the below.

    $ ./readability
    Text: In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
    In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.

### Letters

Now that you’ve collected input from the user, let’s begin to analyze that input by first counting the number of letters in the text. Consider letters to be uppercase or lowercase alphabetical character, not punctuation, digits, or other symbols.

Add to `readability.c`, below `main`, a function called `count_letters` that takes one argument, a `string` of text, and that returns an `int`, the number of letters in that text. Be sure to add the function’s prototype, too, atop your file, so that `main` knows how to call it. Odds are the prototype should resemble the below:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">count_letters</span><span class="p">(</span><span class="n">string</span> <span class="n">text</span><span class="p">)</span>
</code></pre></div></div>

Then call that function in `main` so that, instead of printing out the text itself, your program now prints the number of letters in the text.

The program should now behave per the below.

    $ ./readability
    Text: Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"
    235 letters

<details><summary>Hint</summary><p>Declared in <code class="language-plaintext highlighter-rouge">ctype.h</code> is a function that you might find helpful, per <a href="https://manual.cs50.io/">manual.cs50.io</a>. If you use it, be sure to include that header file atop your own code!</p></details>

### Words

The Coleman-Liau index cares not only about the number of letters but also about the number of words in a sentence. For the purpose of this problem, we’ll consider any sequence of characters separated by a space to be a word (so a hyphenated word like `"sister-in-law"` should be considered one word, not three).

Add to `readability.c`, below `main`, a function called `count_words` that takes one argument, a `string` of text, and that returns an `int`, the number of words in that text. Be sure to add the function’s prototype, too, atop your file, so that `main` knows how to call it. (We leave its prototype to you!)

Then call that function in `main` so that your program also prints the number of words in the text.

You may assume that a sentence:

- will contain at least one word;
- will not start or end with a space; and
- will not have multiple spaces in a row.

You are, of course, welcome to attempt a solution that will tolerate multiple spaces between words or indeed, no words!

The program should now behave per the below.

    $ ./readability
    Text: It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.
    250 letters
    55 words
