<style>.wrong { background-color: red } .right { background-color: green; } .close_ { background-color: yellow; }</style>

Wordle50
========

For this problem, you’ll implement a program that behaves similarly to the popular [Wordle](https://www.nytimes.com/games/wordle/index.html) daily word game.

<pre><code> $ ./wordle 5
<span class="right">This is WORDLE50</span>
You have 6 tries to guess the 5-letter word I'm thinking of
Input a 5-letter word: crash
Guess 1: <span class="close_">c</span><span class="wrong">ra</span><span class="close_">s</span><span class="wrong">h</span>
Input a 5-letter word: scone
Guess 2: <span class="right">s</span><span class="close_">c</span><span class="wrong">o</span><span class="close_">n</span><span class="right">e</span>
Input a 5-letter word: since
Guess 3: <span class="right">since</span>
You won!
</code></pre>


Getting Started
---------------

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $
    

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/psets/2/wordle.zip
    

followed by Enter in order to download a ZIP called `wordle.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip wordle.zip
    

to create a folder called `wordle`. You no longer need the ZIP file, so you can execute

    rm wordle.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd wordle
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    wordle/ $
    

If all was successful, you should execute

    ls
    

and see a file named `wordle.c`, as well as `5.txt`, `6.txt`, `7.txt` and `8.txt`. Executing `code wordle.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong! If you try to compile the game now, it will do so without errors, but when you try to run it you will see this error:

    Error opening file 0.txt.
    

‘Tis normal, though, since you haven’t yet implemented part of the code we need to make that error message go away!
