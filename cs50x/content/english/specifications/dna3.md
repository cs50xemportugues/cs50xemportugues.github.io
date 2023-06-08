
Specification
-------------

In a file called `dna.py`, implement a program that identifies to whom a sequence of DNA belongs.

*   The program should require as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.
    *   If your program is executed with the incorrect number of command-line arguments, your program should print an error message of your choice (with `print`). If the correct number of arguments are provided, you may assume that the first argument is indeed the filename of a valid CSV file and that the second argument is the filename of a valid text file.
*   Your program should open the CSV file and read its contents into memory.
    *   You may assume that the first row of the CSV file will be the column names. The first column will be the word `name` and the remaining columns will be the STR sequences themselves.
*   Your program should open the DNA sequence and read its contents into memory.
*   For each of the STRs (from the first line of the CSV file), your program should compute the longest run of consecutive repeats of the STR in the DNA sequence to identify. Notice that we’ve defined a helper function for you, `longest_match`, which will do just that!
*   If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual.
    *   You may assume that the STR counts will not match more than one individual.
    *   If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print `No match`.

Walkthrough
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/j84b_EgntcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Usage
-----

Your program should behave per the example below:

<pre>
$ python dna.py databases/large.csv sequences/5.txt
Lavender
</pre>

<pre>
$ python dna.py
Usage: python dna.py data.csv sequence.txt
</pre>

<pre>
$ python dna.py data.csv
Usage: python dna.py data.csv sequence.txt
</pre>
