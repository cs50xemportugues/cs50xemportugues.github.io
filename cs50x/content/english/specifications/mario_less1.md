# Mario

## Getting Started

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/psets/1/mario-less.zip

followed by Enter in order to download a ZIP called `mario-less.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip mario-less.zip

to create a folder called `mario-less`. You no longer need the ZIP file, so you can execute

    rm mario-less.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd mario-less

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    mario-less/ $

If all was successful, you should execute

    ls

and see a file named `mario.c`. Executing `code mario.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!

## World 1-1

Toward the end of World 1-1 in Nintendo’s Super Mario Brothers, Mario must ascend right-aligned pyramid of blocks, a la the below.

![screenshot of Mario jumping up a right-aligned pyramid](https://cs50.harvard.edu/x/2023/psets/1/mario/less/pyramid.png)

Let’s recreate that pyramid in C, albeit in text, using hashes (`#`) for bricks, a la the below. Each hash is a bit taller than it is wide, so the pyramid itself will also be taller than it is wide.

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

The program we’ll write will be called `mario`. And let’s allow the user to decide just how tall the pyramid should be by first prompting them for a positive integer between, say, 1 and 8, inclusive.

Here’s how the program might work if the user inputs `8` when prompted:

    $ ./mario
    Height: 8
           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Here’s how the program might work if the user inputs `4` when prompted:

    $ ./mario
    Height: 4
       #
      ##
     ###
    ####

Here’s how the program might work if the user inputs `2` when prompted:

    $ ./mario
    Height: 2
     #
    ##

And here’s how the program might work if the user inputs `1` when prompted:

    $ ./mario
    Height: 1
    #

If the user doesn’t, in fact, input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
       #
      ##
     ###
    ####

How to begin? Let’s approach this problem one step at a time.

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>
