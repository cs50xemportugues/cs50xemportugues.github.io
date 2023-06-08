
Usage
-----

Here are a few examples of how the program should work. For example, if the user omits one of the command-line arguments:

    $ ./reverse input.wav
    Usage: ./reverse input.wav output.wav
    

Or if the user omits both of the command-line arugments:

    $ ./reverse
    Usage: ./reverse input.wav output.wav
    

Here’s how the program should work if the user provides an input file that is not an actual WAV file:

    $ ./reverse image.jpg output.wav
    Input is not a WAV file.
    

You may assume the user enters a valid output filename, such as `output.wav`.

A successfully executed program should not output any text, and should create a WAV file with the user-specified name that plays the audio of the input WAV file in reverse. For example:

    $ ./reverse input.wav output.wav
    

Testing
-------

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/problems/2023/x/reverse
    

Execute the below to evaluate the style of your code using `style50`.

    style50 reverse.c
    

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/reverse