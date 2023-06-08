Bulbs
=====

Not-So-Broken Light Bulbs
-------------------------

In lecture, you may have noticed what seemed like a “bug” at the front of the stage, whereby some of the bulbs always seem to be off:

![screenshot of Week 2 lecture with strip of bulbs](https://cs50.harvard.edu/x/2023/psets/2/bulbs/binary_bulbs.jpg)

Each sequence of bulbs, though, encodes a message in _binary_, the language computers “speak.” Let’s write a program to make secret messages of your own, perhaps that we could even put on stage!

Getting Started
---------------

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $
    

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/psets/2/bulbs.zip
    

followed by Enter in order to download a ZIP called `bulbs.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip bulbs.zip
    

to create a folder called `bulbs`. You no longer need the ZIP file, so you can execute

    rm bulbs.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd bulbs
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    bulbs/ $
    

If all was successful, you should execute

    ls
    

and see a file named `bulbs.c`. Executing `code bulbs.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!
