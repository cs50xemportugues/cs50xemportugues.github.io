
Getting Started
---------------

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $
    

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/psets/4/reverse.zip
    

followed by Enter in order to download a ZIP called `reverse.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip reverse.zip
    

to create a folder called `reverse`. You no longer need the ZIP file, so you can execute

    rm reverse.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd reverse
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    reverse/ $
    

If all was successful, you should execute

    ls
    

and see a file named `reverse.c`. Executing `code reverse.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!

### The WAV File Format

Notice that, in the visual below, a WAV file is broken into three chunks. Each chunk has a few blocks of data inside of it.

The first chunk contains information about the file’s type. In particular, see how the “File Format” block in the first chunk spells out ‘W’ ‘A’ ‘V’ ‘E’ in bytes 8–11, to indicate the file is a WAV file.

The second chunk contains information about the upcoming audio data, including how many “channels” of audio are present and how many bits are in each audio “sample”. Audio files have 1 channel when they’re “monophonic”: if you were to wear headphones, you’d hear the same audio in your left and right ear. Audio files have 2 channels when they’re “stereophonic”: wearing headphones, you’d hear slightly different audio in your left and right ear, creating a sense of spaciousness. Samples are the individual chunks of bits which make up the audio you hear. With more bits per sample, an audio file can have greater clarity (at the cost of more memory used!).

Finally, the third chunk contains the audio data itself—those samples we mentioned just above.

Everything before the audio data is considered part of the WAV “header”. Recall that a file header is simply some metadata about the file. In this case, the header is 44 bytes long.

![WAV Header](https://cs50.harvard.edu/x/2023/psets/4/reverse/WAV_header.png)

A more technical explanation of WAV headers can be found [here](http://soundfile.sapp.org/doc/WaveFormat/), which is the resource by which this visual was inspired. Notice that we’ve included a file, `wav.h`, which implements all these details for you in a struct called `WAVHEADER`.
