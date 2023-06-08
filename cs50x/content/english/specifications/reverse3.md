
Specification
-------------

Let’s write a program called called `reverse` that enables us to reverse a WAV file given by the user and create a new WAV file that contains the resulting reversed audio. For simplicity’s sake, we’ll limit the files we deal with to the WAV format. At the time the user executes the program, they should provide, using two command-line arguments, the name of the input file to be read and reversed, and the name of the output file they would like to save the resulting audio in. A successfully executed program should not output any text, and should create a WAV file with the user-specified name that plays the audio of the input WAV file in reverse. For example:

    $ ./reverse input.wav output.wav
    

In `reverse.c`, you’ll notice that a few helpful libraries have been included, as well as a header file, `wav.h`. You’ll likely find these to be useful when implementing your program. We’ve left eight `TODO`s and two helper functions for you to fill in, and we recommend you tackle them in order from 1 to 8.

*   In the first `TODO`, you should ensure the program accepts two command-line arguments: the name of the input WAV file and the name of the output WAV file. If the program does not meet these conditions, you should print an appropriate error message and return `1`, ending the program.
    <ul>
      <li data-marker="+">Hint
        <ul>
          <li data-marker="*">Keep in mind, the number of command-line arguments can be found in the <code class="language-plaintext highlighter-rouge">argc</code> variables passed to the <code class="language-plaintext highlighter-rouge">main</code> function when the program is executed.</li>
          <li data-marker="*">Remember that <code class="language-plaintext highlighter-rouge">argv[0]</code> holds the name of the program as the first command-line argument.</li>
        </ul>
      </li>
    </ul>
*   In the second `TODO`, you should open your input file. We’ll need to open the input file in “read-only” mode, since we’ll only read data from the input file. It may be wise to check that the file has been opened successfully. Otherwise, you should print an appropriate error message and return `1`, exiting the program. We should hold off on opening the output file, though, lest we create a new WAV file before knowing the input file is valid!
    <ul>
      <li data-marker="+">Hint
        <ul>
          <li data-marker="*">If the first <code class="language-plaintext highlighter-rouge">TODO</code> has been implemented properly, it is safe to assume we can reference the name of the input file using <code class="language-plaintext highlighter-rouge">argv[1]</code>.</li>
          <li data-marker="*">Keep in mind, any file that we open, we must also close when we are finished using it. This may mean adding code elsewhere in the program.</li>
        </ul>
      </li>
    </ul>
*   In the third `TODO`, you should read the header from the input file. Recall that, in `wav.h`, we’ve already implemented a struct that can store a WAV file’s header. Since we’ve written `#include "wav.h"` at the top of `reverse.c`, you, too, can use the `WAVHEADER` struct.
    
*   In the fourth `TODO`, you should complete the `check_format` function. `check_format` takes a single argument, a `WAVHEADER` called `header`, representing a struct containing the input file’s header. If `header` indicates the file is indeed a WAV file, the `check_format` function should return `true`. If not, `check_format` should return `false`. To check if a file is of the WAV format, we can compare the elements from the input file header to those we would expect from a WAV file. It suffices to show the “WAVE” marker characters are found in the `format` member of the `WAVHEADER` struct (see [Background](#background) for more detail on WAV file headers).
    
*   In the fifth `TODO`, you can now safely open the output file for writing. It would still be wise to check that the file has been opened successfully.
    <ul>
      <li data-marker="+">Hints
        <ul>
          <li data-marker="*">If the first <code class="language-plaintext highlighter-rouge">TODO</code> has been implemented properly, it is safe to assume we can reference the name of the output file using <code class="language-plaintext highlighter-rouge">argv[2]</code>.</li>
          <li data-marker="*">Keep in mind, any file that we open, we must also close when we are finished using it. This may mean adding code elsewhere in the program.</li>
        </ul>
      </li>
    </ul>

This may be a good place to stop and test that your program behaves as expected. If implemented properly, your program should open a new file when executed with the proper command-line arguments.

If at any point you find it necessary to delete a file, execute the following command in your current working directory.

    $ rm file_name.wav
    

If you’d rather not be prompted to confirm each deletion, execute the command below instead.

    $ rm -f file_name.wav
    

Just be careful with that `-f` switch, as it “forces” deletion without prompting you.

*   Next, now that the file type has been verified, the sixth `TODO` tells us to write the header to the output file. The reversed WAV file will still have the same underlying file structure as the input file (same size, number of channels, bits per sample, etc.), so it suffices to copy the header we read in from the input file in the third `TODO` to the output file.

