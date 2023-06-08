
Background
----------

Odds are, if you’re a Facebook user, at least one of your friends posted something looking like this, particularly back in early 2022 when it was all the rage:

![Wordle results](https://cs50.harvard.edu/x/2023/psets/2/wordle50/wordle.png)

If so, your friend has played Wordle, and are sharing their results for that day! Each day, a new “secret word” is chosen (the same for everyone) and the object is to guess what the secret word is within six tries. Fortunately, given that there are more than six five-letter words in the English language, you may get some clues along the way, and the image above actually shows your friend’s progression through their guesses, using those clues to try to home in on the correct word. Using a scheme similar to the game [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)), if after you guess that letter turns green, it means not only is that letter in the secret word that day, but it is also in the correct position. If it turns yellow, it means that the letter guessed appears _somewhere_ in the word, but not in that spot. Letters that turn gray aren’t in the word at all and can be omitted from future guesses.

Let’s finish writing a program called `wordle` that enables us to recreate this game and play it in our terminal instead. We’ll make a few slight changes to the game (for example, the way it handles a letter appearing twice in a word isn’t the same as how the real game handles it, but for simplicity’s sake, we’ll err on the side of ease of understanding rather than a perfectly faithful interpretation), and we’ll use red text instead of gray to indicate letters that aren’t in the word at all. At the time the user executes the program, they should decide, by providing a command-line argument, what the length of the word they want to guess is, between 5 and 8 letters.

Here are a few examples of how the program should work. For example, if the user omits a command line argument entirely:

    $ ./wordle
    Usage: ./wordle wordsize
    

If the user instead does provide a command-line argument, but it’s not in the correct range:

    $ ./wordle 4
    Error: wordsize must be either 5, 6, 7, or 8
    

Here’s how the program might work if the user provides a key of `5`:

    $ ./wordle 5
    This is WORDLE50
    You have 6 tries to guess the 5-letter word I'm thinking of
    Input a 5-letter word:
    

At which point, the user should type in a 5-letter word. Of course, the user could well be stubborn, and we should make sure they’re following the rules:

    
<pre><code>$ ./wordle 5
<span class="right">This is WORDLE50</span>
You have 6 tries to guess the 5-letter word I'm thinking of
Input a 5-letter word: wordle
Input a 5-letter word: computer
Input a 5-letter word: okay
Input a 5-letter word: games
Guess 1: <span class="wrong">g</span><span class="close_">a</span><span class="wrong">m</span><span class="close_">e</span><span class="wrong">s</span>
Input a 5-letter word:
</code></pre>
    

Notice that we didn’t even count any of those invalid attempts as guesses. But as soon as they made a legitimate attempt, we counted it as a guess and reported on the status of the word. Looks like the user has a few clues now; they know the word contains an `a` and an `e` somewhere, but not in the exact spots they appear in the word `games`. And they know that `g`, `m`, and `s` don’t appear in the word at all, so future guesses can omit them. Perhaps they might try, say, `heart` next! ❤️
