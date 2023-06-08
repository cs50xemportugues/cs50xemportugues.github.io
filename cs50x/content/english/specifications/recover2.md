
Walkthrough
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ooL0r_8N9ms?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Usage
-----

Your program should behave per the examples below.

    $ ./recover
    Usage: ./recover IMAGE
    

where `IMAGE` is the name of the forensic image. For example:

    $ ./recover card.raw
    

Hints
-----

Keep in mind that you can open `card.raw` programmatically with `fopen`, as with the below, provided `argv[1]` exists.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">FILE</span> <span class="o">*</span><span class="n">file</span> <span class="o">=</span> <span class="n">fopen</span><span class="p">(</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="s">"r"</span><span class="p">);</span>
</code></pre></div></div>
    

When executed, your program should recover every one of the JPEGs from `card.raw`, storing each as a separate file in your current working directory. Your program should number the files it outputs by naming each `###.jpg`, where `###` is three-digit decimal number from `000` on up. Befriend [`sprintf`](https://man.cs50.io/3/sprintf) and note that `sprintf` stores a formatted string at a location in memory. Given the prescribed `###.jpg` format for a JPEG’s filename, how many bytes should you allocate for that string? (Don’t forget the NUL character!)

You need not try to recover the JPEGs’ original names. To check whether the JPEGs your program spit out are correct, simply double-click and take a look! If each photo appears intact, your operation was likely a success!

Odds are, though, the JPEGs that the first draft of your code spits out won’t be correct. (If you open them up and don’t see anything, they’re probably not correct!) Execute the command below to delete all JPEGs in your current working directory.

    $ rm *.jpg
    

If you’d rather not be prompted to confirm each deletion, execute the command below instead.

    $ rm -f *.jpg
    

Just be careful with that `-f` switch, as it “forces” deletion without prompting you.

If you’d like to create a new type to store a byte of data, you can do so via the below, which defines a new type called `BYTE` to be a `uint8_t` (a type defined in `stdint.h`, representing an 8-bit unsigned integer).

    typedef uint8_t BYTE;
    

Keep in mind, too, that you can read data from a file using [`fread`](https://man.cs50.io/3/fread), which will read data from a file into a location in memory. Per its [manual page](https://man.cs50.io/3/fread), `fread` returns the number of bytes that it has read, in which case it should either return `512` or `0`, given that `card.raw` contains some number of 512-byte blocks. In order to read every block from `card.raw`, after opening it with `fopen`, it should suffice to use a loop like:

   
<pre class="highlight">
<span class="k">while</span> (fread(buffer, <span class="mi">1</span>, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
{


}
</pre>
That way, as soon as `fread` returns `0` (which is effectively `false`), your loop will end.

Testing
-------

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/problems/2023/x/recover
    

Execute the below to evaluate the style of your code using `style50`.

    style50 recover.c
    

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/recover