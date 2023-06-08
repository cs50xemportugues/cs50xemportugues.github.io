
Getting Started
---------------

Log into [code.cs50.io](https://code.cs50.io/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $
    

Next execute

    wget https://cdn.cs50.net/2022/fall/psets/3/tideman.zip
    

in order to download a ZIP called `tideman.zip` into your codespace.

Then execute

    unzip tideman.zip
    

to create a folder called `tideman`. You no longer need the ZIP file, so you can execute

    rm tideman.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd tideman
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    tideman/ $
    

If all was successful, you should execute

    ls
    

and see a file named `tideman.c`. Executing `code tideman.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!

Understanding
-------------

Let’s take a look at `tideman.c`.

First, notice the two-dimensional array `preferences`. The integer `preferences[i][j]` will represent the number of voters who prefer candidate `i` over candidate `j`.

The file also defines another two-dimensional array, called `locked`, which will represent the candidate graph. `locked` is a boolean array, so `locked[i][j]` being `true` represents the existence of an edge pointing from candidate `i` to candidate `j`; `false` means there is no edge. (If curious, this representation of a graph is known as an “adjacency matrix”).

Next up is a `struct` called `pair`, used to represent a pair of candidates: each pair includes the `winner`’s candidate index and the `loser`’s candidate index.

The candidates themselves are stored in the array `candidates`, which is an array of `string`s representing the names of each of the candidates. There’s also an array of `pairs`, which will represent all of the pairs of candidates (for which one is preferred over the other) in the election.

The program also has two global variables: `pair_count` and `candidate_count`, representing the number of pairs and number of candidates in the arrays `pairs` and `candidates`, respectively.

Now onto `main`. Notice that after determining the number of candidates, the program loops through the `locked` graph and initially sets all of the values to `false`, which means our initial graph will have no edges in it.

Next, the program loops over all of the voters and collects their preferences in an array called `ranks` (via a call to `vote`), where `ranks[i]` is the index of the candidate who is the `i`th preference for the voter. These ranks are passed into the `record_preference` function, whose job it is to take those ranks and update the global `preferences` variable.

Once all of the votes are in, the pairs of candidates are added to the `pairs` array via a called to `add_pairs`, sorted via a call to `sort_pairs`, and locked into the graph via a call to `lock_pairs`. Finally, `print_winner` is called to print out the name of the election’s winner!

Further down in the file, you’ll see that the functions `vote`, `record_preference`, `add_pairs`,`sort_pairs`, `lock_pairs`, and `print_winner` are left blank. That’s up to you!
