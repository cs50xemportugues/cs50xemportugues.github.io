Speller
=======

<div class="alert" data-alert="danger" role="alert"><p><strong>Be sure to read this specification in its entirety before starting so you know what to do and how to do it!</strong></p></div>


For this problem, you’ll implement a program that spell-checks a file, a la the below, using a hash table.

    $ ./speller texts/lalaland.txt
    MISSPELLED WORDS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    WORDS MISSPELLED:
    WORDS IN DICTIONARY:
    WORDS IN TEXT:
    TIME IN load:
    TIME IN check:
    TIME IN size:
    TIME IN unload:
    TIME IN TOTAL:
    

Getting Started
---------------

Log into [code.cs50.io](https://code.cs50.io/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $
    

Next execute

    wget https://cdn.cs50.net/2022/fall/psets/5/speller.zip
    

in order to download a ZIP called `speller.zip` into your codespace.

Then execute

    unzip speller.zip
    

to create a folder called `speller`. You no longer need the ZIP file, so you can execute

    rm speller.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd speller
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    speller/ $
    

Execute `ls` by itself, and you should see a few files and folders:

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
    

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!
