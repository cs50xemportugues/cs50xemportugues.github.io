
## Background

Supposedly, Caesar (yes, that Caesar) used to “encrypt” (i.e., conceal in a reversible way) confidential messages by shifting each letter therein by some number of places. For instance, he might write A as B, B as C, C as D, …, and, wrapping around alphabetically, Z as A. And so, to say HELLO to someone, Caesar might write IFMMP instead. Upon receiving such messages from Caesar, recipients would have to “decrypt” them by shifting letters in the opposite direction by the same number of places.

The secrecy of this “cryptosystem” relied on only Caesar and the recipients knowing a secret, the number of places by which Caesar had shifted his letters (e.g., 1). Not particularly secure by modern standards, but, hey, if you’re perhaps the first in the world to do it, pretty secure!

Unencrypted text is generally called _plaintext_. Encrypted text is generally called _ciphertext_. And the secret used is called a _key_.

To be clear, then, here’s how encrypting `HELLO` with a key of `1` yields `IFMMP`:

<table>
  <thead>
    <tr>
      <th>plaintext</th>
      <th><code class="language-plaintext highlighter-rouge">H</code></th>
      <th><code class="language-plaintext highlighter-rouge">E</code></th>
      <th><code class="language-plaintext highlighter-rouge">L</code></th>
      <th><code class="language-plaintext highlighter-rouge">L</code></th>
      <th><code class="language-plaintext highlighter-rouge">O</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+ key</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>= ciphertext</td>
      <td><code class="language-plaintext highlighter-rouge">I</code></td>
      <td><code class="language-plaintext highlighter-rouge">F</code></td>
      <td><code class="language-plaintext highlighter-rouge">M</code></td>
      <td><code class="language-plaintext highlighter-rouge">M</code></td>
      <td><code class="language-plaintext highlighter-rouge">P</code></td>
    </tr>
  </tbody>
</table>

More formally, Caesar’s algorithm (i.e., cipher) encrypts messages by “rotating” each letter by `k` positions. More formally, if `p` is some plaintext (i.e., an unencrypted message), <code>p<sub>i</sub></code> is the <code>i<sup>th</sup></code> character in `p`, and `k` is a secret key (i.e., a non-negative integer), then each letter, <code>c<sub>i</sub></code>, in the ciphertext, `c`, is computed as

<code>c<sub>i</sub> = (p<sub>i</sub> + k) % 26</code>

wherein `% 26` here means “remainder when dividing by 26.” This formula perhaps makes the cipher seem more complicated than it is, but it’s really just a concise way of expressing the algorithm precisely. Indeed, for the sake of discussion, think of A (or a) as `0`, B (or b) as `1`, …, H (or h) as `7`, I (or i) as `8`, …, and Z (or z) as `25`. Suppose that Caesar just wants to say `Hi` to someone confidentially using, this time, a key, `k`, of 3. And so his plaintext, `p`, is `Hi`, in which case his plaintext’s first character, <code>p<sub>0</sub></code>, is `H` (aka 7), and his plaintext’s second character, <code>p<sub>1</sub></code>, is `i` (aka 8). His ciphertext’s first character, <code>c<sub>0</sub></code>, is thus `K`, and his ciphertext’s second character, <code>c<sub>i</sub></code>, is thus `L`. Make sense?

Let’s write a program called `caesar` that enables you to encrypt messages using Caesar’s cipher. At the time the user executes the program, they should decide, by providing a command-line argument, what the key should be in the secret message they’ll provide at runtime. We shouldn’t necessarily assume that the user’s key is going to be a number; though you may assume that, if it is a number, it will be a positive integer.

Here are a few examples of how the program might work. For example, if the user inputs a key of `1` and a plaintext of `HELLO`:

    $ ./caesar 1
    plaintext:  HELLO
    ciphertext: IFMMP

Here’s how the program might work if the user provides a key of `13` and a plaintext of `hello, world`:

    $ ./caesar 13
    plaintext:  hello, world
    ciphertext: uryyb, jbeyq

Notice that neither the comma nor the space were “shifted” by the cipher. Only rotate alphabetical characters!

How about one more? Here’s how the program might work if the user provides a key of `13` again, with a more complex plaintext:

    $ ./caesar 13
    plaintext:  be sure to drink your Ovaltine
    ciphertext: or fher gb qevax lbhe Binygvar

<details><summary>Why?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/9K4FsAHB-C8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

Notice that the case of the original message has been preserved. Lowercase letters remain lowercase, and uppercase letters remain uppercase.

And what if a user doesn’t cooperate, providing a command-line argument that isn’t a number? The program should remind the user how to use the program:

    $ ./caesar HELLO
    Usage: ./caesar key

Or really doesn’t cooperate, providing no command-line argument at all? The program should remind the user how to use the program:

    $ ./caesar
    Usage: ./caesar key

Or really, really doesn’t cooperate, providing more than one command-line argument? The program should remind the user how to use the program:

    $ ./caesar 1 2 3
    Usage: ./caesar key

<details><summary>Watch a Recording</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-JnlhDTjc264WfGSoNxc0hsjEY" src="https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY.js"></script></details>
