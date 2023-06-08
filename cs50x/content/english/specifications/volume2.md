
Implementation Details
----------------------

Complete the implementation of `volume.c`, such that it changes the volume of a sound file by a given factor.

*   The program accepts three command-line arguments: `input` represents the name of the original audio file, `output` represents the name of the new audio file that should be generated, and `factor` is the amount by which the volume of the original audio file should be scaled.
    *   For example, if `factor` is `2.0`, then your program should double the volume of the audio file in `input` and save the newly generated audio file in `output`.
*   Your program should first read the header from the input file and write the header to the output file. Recall that this header is always exactly 44 bytes long.
    *   Note that `volume.c` already defines a variable for you called `HEADER_SIZE`, equal to the number of bytes in the header.
*   Your program should then read the rest of the data from the WAV file, one 16-bit (2-byte) sample at a time. Your program should multiply each sample by the `factor` and write the new sample to the output file.
    *   You may assume that the WAV file will use 16-bit signed values as samples. In practice, WAV files can have varying numbers of bits per sample, but we’ll assume 16-bit samples for this lab.
*   Your program, if it uses `malloc`, must not leak any memory.

### Walkthrough


<div class="alert" data-alert="primary" role="alert"><p>This video was recorded when the course was still using CS50 IDE for writing code. Though the interface may look different from your codespace, the behavior of the two environments should be largely similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/LiGhjz9ColQ"></iframe>


### Hints

*   You’ll likely want to create an array of bytes to store the data from the WAV file header that you’ll read from the input file. Using the `uint8_t` type to represent a byte, you can create an array of `n` bytes for your header with syntax like

<pre>
uint8_t header[n];
</pre>    

replacing `n` with the number of bytes. You can then use `header` as an argument to `fread` or `fwrite` to read into or write from the header.

*   You’ll likely want to create a “buffer” in which to store audio samples that you read from the WAV file. Using the `int16_t` type to store an audio sample, you can create a buffer variable with syntax like

<pre>
int16_t buffer;
</pre>   

You can then use `&buffer` as an argument to `fread` or `fwrite` to read into or write from the buffer. (Recall that the `&` operator is used to get the address of the variable.)

*   You may find the documentation for [`fread`](https://man.cs50.io/3/fread) and [`fwrite`](https://man.cs50.io/3/fwrite) helpful here.
    *   In particular, note that both functions accept the following arguments:
        *   `ptr`: a pointer to the location in memory to store data (when reading from a file) or from which to write data (when writing data to a file)
        *   `size`: the number of bytes in an item of data
        *   `nmemb`: the number of items of data (each of `size` bytes) to read or write
        *   `stream`: the file pointer to be read from or written to
    *   Per its documentation, `fread` will return the number of items of data successfully read. You may find this useful to check for when you’ve reached the end of the file!


<details><summary>Not sure how to solve?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-rtZkTAK2gg"></iframe></details>


### How to Test Your Code

Your program should behave per the examples below.

    $ ./volume input.wav output.wav 2.0
    

When you listen to `output.wav` (as by control-clicking on `output.wav` in the file browser, choosing **Download**, and then opening the file in an audio player on your computer), it should be twice as loud as `input.wav`!

    $ ./volume input.wav output.wav 0.5
    

When you listen to `output.wav`, it should be half as loud as `input.wav`!

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/labs/2023/x/volume
    

Execute the below to evaluate the style of your code using `style50`.

    style50 volume.c
    

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/labs/2023/x/volume