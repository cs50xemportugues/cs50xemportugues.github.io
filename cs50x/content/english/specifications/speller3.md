
#### `dictionary.c`

Now open up `dictionary.c`. Notice how, atop the file, we’ve defined a `struct` called `node` that represents a node in a hash table. And we’ve declared a global pointer array, `table`, which will (soon) represent the hash table you will use to keep track of words in the dictionary. The array contains `N` node pointers, and we’ve set `N` equal to `26` for now, to match with the default `hash` function as described below. You will likely want to increase this depending on your own implementation of `hash`.

Next, notice that we’ve implemented `load`, `check`, `size`, and `unload`, but only barely, just enough for the code to compile. Notice too that we’ve implemented `hash` with a sample algorithm based on the first letter of the word. Your job, ultimately, is to re-implement those functions as cleverly as possible so that this spell checker works as advertised. And fast!

#### `speller.c`

Okay, next open up `speller.c` and spend some time looking over the code and comments therein. You won’t need to change anything in this file, and you don’t need to understand its entirety, but do try to get a sense of its functionality nonetheless. Notice how, by way of a function called `getrusage`, we’ll be “benchmarking” (i.e., timing the execution of) your implementations of `check`, `load`, `size`, and `unload`. Also notice how we go about passing `check`, word by word, the contents of some file to be spell-checked. Ultimately, we report each misspelling in that file along with a bunch of statistics.

Notice, incidentally, that we have defined the usage of `speller` to be

    Usage: speller [dictionary] text
    

where `dictionary` is assumed to be a file containing a list of lowercase words, one per line, and `text` is a file to be spell-checked. As the brackets suggest, provision of `dictionary` is optional; if this argument is omitted, `speller` will use `dictionaries/large` by default. In other words, running

    ./speller text
    

will be equivalent to running

    ./speller dictionaries/large text
    

where `text` is the file you wish to spell-check. Suffice it to say, the former is easier to type! (Of course, `speller` will not be able to load any dictionaries until you implement `load` in `dictionary.c`! Until then, you’ll see `Could not load`.)

Within the default dictionary, mind you, are 143,091 words, all of which must be loaded into memory! In fact, take a peek at that file to get a sense of its structure and size. Notice that every word in that file appears in lowercase (even, for simplicity, proper nouns and acronyms). From top to bottom, the file is sorted lexicographically, with only one word per line (each of which ends with `\n`). No word is longer than 45 characters, and no word appears more than once. During development, you may find it helpful to provide `speller` with a `dictionary` of your own that contains far fewer words, lest you struggle to debug an otherwise enormous structure in memory. In `dictionaries/small` is one such dictionary. To use it, execute

    ./speller dictionaries/small text
    

where `text` is the file you wish to spell-check. Don’t move on until you’re sure you understand how `speller` itself works!

Odds are, you didn’t spend enough time looking over `speller.c`. Go back one square and walk yourself through it again!

#### `texts/`

So that you can test your implementation of `speller`, we’ve also provided you with a whole bunch of texts, among them the script from _La La Land_, the text of the Affordable Care Act, three million bytes from Tolstoy, some excerpts from _The Federalist Papers_ and Shakespeare, and more. So that you know what to expect, open and skim each of those files, all of which are in a directory called `texts` within your `pset5` directory.

Now, as you should know from having read over `speller.c` carefully, the output of `speller`, if executed with, say,

    ./speller texts/lalaland.txt
    

will eventually resemble the below.

Below’s some of the output you’ll see. For information’s sake, we’ve excerpted some examples of “misspellings.” And lest we spoil the fun, we’ve omitted our own statistics for now.

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
    

`TIME IN load` represents the number of seconds that `speller` spends executing your implementation of `load`. `TIME IN check` represents the number of seconds that `speller` spends, in total, executing your implementation of `check`. `TIME IN size` represents the number of seconds that `speller` spends executing your implementation of `size`. `TIME IN unload` represents the number of seconds that `speller` spends executing your implementation of `unload`. `TIME IN TOTAL` is the sum of those four measurements.

**Note that these times may vary somewhat across executions of `speller`, depending on what else your codespace is doing, even if you don’t change your code.**

Incidentally, to be clear, by “misspelled” we simply mean that some word is not in the `dictionary` provided.

#### `Makefile`

And, lastly, recall that `make` automates compilation of your code so that you don’t have to execute `clang` manually along with a whole bunch of switches. However, as your programs grow in size, `make` won’t be able to infer from context anymore how to compile your code; you’ll need to start telling `make` how to compile your program, particularly when they involve multiple source (i.e., `.c`) files, as in the case of this problem. And so we’ll utilize a `Makefile`, a configuration file that tells `make` exactly what to do. Open up `Makefile`, and you should see four lines:

1.  The first line tells `make` to execute the subsequent lines whenever you yourself execute `make speller` (or just `make`).
2.  The second line tells `make` how to compile `speller.c` into machine code (i.e., `speller.o`).
3.  The third line tells `make` how to compile `dictionary.c` into machine code (i.e., `dictionary.o`).
4.  The fourth line tells `make` to link `speller.o` and `dictionary.o` in a file called `speller`.

**Be sure to compile `speller` by executing `make speller` (or just `make`). Executing `make dictionary` won’t work!**
