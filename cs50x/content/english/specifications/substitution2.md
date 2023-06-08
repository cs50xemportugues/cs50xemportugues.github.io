
Specification
-------------

Design and implement a program, `substitution`, that encrypts messages using a substitution cipher.

*   Implement your program in a file called `substitution.c` in a directory called `substitution`.
*   Your program must accept a single command-line argument, the key to use for the substitution. The key itself should be case-insensitive, so whether any character in the key is uppercase or lowercase should not affect the behavior of your program.
*   If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error message of your choice (with `printf`) and return from `main` a value of `1` (which tends to signify an error) immediately.
*   If the key is invalid (as by not containing 26 characters, containing any character that is not an alphabetic character, or not containing each letter exactly once), your program should print an error message of your choice (with `printf`) and return from `main` a value of `1` immediately.
*   Your program must output `plaintext:` (without a newline) and then prompt the user for a `string` of plaintext (using `get_string`).
*   Your program must output `ciphertext:` (without a newline) followed by the plaintext’s corresponding ciphertext, with each alphabetical character in the plaintext substituted for the corresponding character in the ciphertext; non-alphabetical characters should be outputted unchanged.
*   Your program must preserve case: capitalized letters must remain capitalized letters; lowercase letters must remain lowercase letters.
*   After outputting ciphertext, you should print a newline. Your program should then exit by returning `0` from `main`.

You might find one or more functions declared in `ctype.h` to be helpful, per [manual.cs50.io](https://manual.cs50.io/).

Walkthrough
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cXAoZAsgxJ4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


How to Test Your Code
---------------------

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/problems/2023/x/substitution
    

Execute the below to evaluate the style of your code using `style50`.

    style50 substitution.c
    

<details><summary>How to Use <code>debug50</code></summary><p>Looking to run <code class="language-plaintext highlighter-rouge">debug50</code>? You can do so as follows, after compiling your code successfully with <code class="language-plaintext highlighter-rouge">make</code>,</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>debug50 ./substitution KEY
</code></pre></div></div>

<p>wherein <code class="language-plaintext highlighter-rouge">KEY</code> is the key you give as a command-line argument to your program. Note that running</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>debug50 ./substitution
</code></pre></div></div>

<p>will (ideally!) cause your program end by prompting the user for a key.</p></details>

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/substitution