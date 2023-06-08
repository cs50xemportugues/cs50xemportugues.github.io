Lab 4: Volume
=============


<div class="alert" data-alert="warning" role="alert"><p>You are welcome to collaborate with one or two classmates on this lab, though it is expected that every student in any such group contribute equally to the lab.</p></div>

Write a program to modify the volume of an audio file.

    $ ./volume INPUT.wav OUTPUT.wav 2.0
    

Where `INPUT.wav` is the name of an original audio file and `OUTPUT.wav` is the name of an audio file with a volume that has been scaled by the given factor (e.g., 2.0).

WAV Files
---------

[WAV files](https://docs.fileformat.com/audio/wav/) are a common file format for representing audio. WAV files store audio as a sequence of “samples”: numbers that represent the value of some audio signal at a particular point in time. WAV files begin with a 44-byte “header” that contains information about the file itself, including the size of the file, the number of samples per second, and the size of each sample. After the header, the WAV file contains a sequence of samples, each a single 2-byte (16-bit) integer representing the audio signal at a particular point in time.

Scaling each sample value by a given factor has the effect of changing the volume of the audio. Multiplying each sample value by 2.0, for example, will have the effect of doubling the volume of the origin audio. Multiplying each sample by 0.5, meanwhile, will have the effect of cutting the volume in half.

Types
-----

So far, we’ve seen a number of different types in C, including `int`, `bool`, `char`, `double`, `float`, and `long`. Inside a header file called `stdint.h` are the declarations of a number of other types that allow us to very precisely define the size (in bits) and sign (signed or unsigned) of an integer. Two types in particular will be useful to us in this lab.

*   `uint8_t` is a type that stores an 8-bit unsigned (i.e., not negative) integer. We can treat each byte of a WAV file’s header as a `uint8_t` value.
*   `int16_t` is a type that stores a 16-bit signed (i.e., positive or negative) integer. We can treat each sample of audio in a WAV file as an `int16_t` value.

Getting Started
---------------

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $
    

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/labs/4/volume.zip
    

followed by Enter in order to download a ZIP called `volume.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip volume.zip
    

to create a folder called `volume`. You no longer need the ZIP file, so you can execute

    rm volume.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd volume
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    volume/ $
    

If all was successful, you should execute

    ls
    

and you should see a `volume.c` file alongside an `input.wav` file.

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!
