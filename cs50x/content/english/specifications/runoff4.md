
Walkthrough
-----------


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Usage
-----

Your program should behave per the example below:

    ./runoff Alice Bob Charlie
    Number of voters: 5
    Rank 1: Alice
    Rank 2: Charlie
    Rank 3: Bob
    
    Rank 1: Alice
    Rank 2: Charlie
    Rank 3: Bob
    
    Rank 1: Bob
    Rank 2: Charlie
    Rank 3: Alice
    
    Rank 1: Bob
    Rank 2: Charlie
    Rank 3: Alice
    
    Rank 1: Charlie
    Rank 2: Alice
    Rank 3: Bob
    
    Alice
    

Testing
-------

Be sure to test your code to make sure it handles…

*   An election with any number of candidate (up to the `MAX` of `9`)
*   Voting for a candidate by name
*   Invalid votes for candidates who are not on the ballot
*   Printing the winner of the election if there is only one
*   Not eliminating anyone in the case of a tie between all remaining candidates

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/problems/2023/x/runoff
    

Execute the below to evaluate the style of your code using `style50`.

    style50 runoff.c
    

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/runoff