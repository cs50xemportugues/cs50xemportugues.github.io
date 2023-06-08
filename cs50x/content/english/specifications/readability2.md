
## Background

According to [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), E.B. White’s _Charlotte’s Web_ is between a second- and fourth-grade reading level, and Lois Lowry’s _The Giver_ is between an eighth- and twelfth-grade reading level. What does it mean, though, for a book to be at a particular reading level?

Well, in many cases, a human expert might read a book and make a decision on the grade (i.e., year in school) for which they think the book is most appropriate. But an algorithm could likely figure that out too!

So what sorts of traits are characteristic of higher reading levels? Well, longer words probably correlate with higher reading levels. Likewise, longer sentences probably correlate with higher reading levels, too.

A number of “readability tests” have been developed over the years that define formulas for computing the reading level of a text. One such readability test is the _Coleman-Liau index_. The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text. The formula is

    index = 0.0588 * L - 0.296 * S - 15.8

where `L` is the average number of letters per 100 words in the text, and `S` is the average number of sentences per 100 words in the text.

Let’s write a program called `readability` that takes a text and determines its reading level. For example, if user types in a line of text from Dr. Seuss, the program should behave as follows:

    $ ./readability
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3

The text the user inputted has 65 letters, 4 sentences, and 14 words. 65 letters per 14 words is an average of about 464.29 letters per 100 words (because 65 / 14 \* 100 = 464.29). And 4 sentences per 14 words is an average of about 28.57 sentences per 100 words (because 4 / 14 \* 100 = 28.57). Plugged into the Coleman-Liau formula, and rounded to the nearest integer, we get an answer of 3 (because 0.0588 \* 464.29 - 0.296 \* 28.57 - 15.8 = 3): so this passage is at a third-grade reading level.

Let’s try another one:

    $ ./readability
    Text: Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.
    Grade 5

This text has 214 letters, 4 sentences, and 56 words. That comes out to about 382.14 letters per 100 words, and 7.14 sentences per 100 words. Plugged into the Coleman-Liau formula, we get a fifth-grade reading level.

As the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level. If you were to take this paragraph, for instance, which has longer words and sentences than either of the prior two examples, the formula would give the text an twelfth-grade reading level.

    $ ./readability
    Text: As the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level. If you were to take this paragraph, for instance, which has longer words and sentences than either of the prior two examples, the formula would give the text an twelfth-grade reading level.
    Grade 12

<details><summary>Watch a Recording</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script></details>

## Specification

Design and implement a program, `readability`, that computes the Coleman-Liau index of text.

- Implement your program in a file called `readability.c` in a directory called `readability`.
- Your program must prompt the user for a `string` of text using `get_string`.
- Your program should count the number of letters, words, and sentences in the text. You may assume that a letter is any lowercase character from `a` to `z` or any uppercase character from `A` to `Z`, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
- Your program should print as output `"Grade X"` where `X` is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
- If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output `"Grade 16+"` instead of giving the exact index number. If the index number is less than 1, your program should output `"Before Grade 1"`.
