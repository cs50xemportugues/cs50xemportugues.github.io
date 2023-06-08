# Readability

For this problem, you’ll implement a program that calculates the approximate grade level needed to comprehend some text, per the below.

    $ ./readability
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3

## Getting Started

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/psets/2/readability.zip

followed by Enter in order to download a ZIP called `readability.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip readability.zip

to create a folder called `readability`. You no longer need the ZIP file, so you can execute

    rm readability.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd readability

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    readability/ $

If all was successful, you should execute

    ls

and see a file named `readability.c`. Executing `code readability.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!
