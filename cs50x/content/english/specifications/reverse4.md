
*   In the seventh `TODO`, you should implement the `get_block_size` function. `get_block_size`, like `check_format`, takes a single argument: this is a `WAVHEADER` called `header`, representing the struct containing the input file’s header. `get_block_size` should return an integer representing the **block size** of the given WAV file, in bytes. We can think of a _block_ as a unit of auditory data. For audio, we calculate the size of each block with the following calculation: **number of channels** multiplied by **bytes per sample**. Luckily, the header contains all the information we need to compute these values. Be sure to reference the [Background](#background) section for a more in-depth explanation as to what these values mean and how they are stored. See too `wav.h`, to determine which members of `WAVHEADER` might be useful.
<ul>
<li data-marker="+">Hints
  <ul>
    <li data-marker="*">Notice that one of the members of <code class="language-plaintext highlighter-rouge">WAVHEADER</code> is <code class="language-plaintext highlighter-rouge">bitsPerSample</code>. But to calculate block size, you’ll need <strong>bytes</strong> per sample!</li>
  </ul>
</li>
</ul>

*   The eighth and final `TODO` is where the actual reversing of the audio takes place. To do this, we need to read in each block of auditory data starting from the very end of the input file and moving backwards, simultaneously writing each block to the output file so they are written in reverse order. First, we should declare an array to store each block we read in. Then, it’s up to you to iterate through the input file audio data. You’ll want to be sure you read through all of the audio, but don’t erroneously copy any of the data from the header! Additionally, for testing purposes, we would like to maintain the order of the channels for each audio block. For example, in a WAV file with two channels (stereophonic sound), we want to make sure that the first channel of the last audio block in the input becomes the first channel of the first audio block in the output.
<ul>
<li data-marker="+">Hints
    <ul>
      <li data-marker="*">A few functions (and a thorough understanding of their usage) may be especially helpful when completing this section - the CS50 manual pages may prove especially useful here:
        <ul>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fread"><code class="language-plaintext highlighter-rouge">fread</code></a>: reads from a file to a buffer. The output of the <code class="language-plaintext highlighter-rouge">get_block_size</code> helper function may be useful here when deciding which values to use for the size and number of data to be read at a time.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fwrite"><code class="language-plaintext highlighter-rouge">fwrite</code></a>: writes from a buffer to a file.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fseek"><code class="language-plaintext highlighter-rouge">fseek</code></a>: sets a file pointer to a given offset. It may be useful to experiment with negative offset values to move a file pointer backwards.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/ftell"><code class="language-plaintext highlighter-rouge">ftell</code></a>: returns the current position of a file pointer. It may be useful to inspect what value <code class="language-plaintext highlighter-rouge">ftell</code> returns after the input header is read in the third <code class="language-plaintext highlighter-rouge">TODO</code> in addition to what it returns while the audio data is being read.</li>
        </ul>
      </li>
      <li data-marker="*">Keep in mind that after you use <code class="language-plaintext highlighter-rouge">fread</code> to load in a block of data, the <code class="language-plaintext highlighter-rouge">input</code> pointer will be pointing at the location where the read concluded. In other words, the <code class="language-plaintext highlighter-rouge">input</code> pointer may need to be moved back <em>two</em> block sizes after each <code class="language-plaintext highlighter-rouge">fread</code>, one to move back to where the <code class="language-plaintext highlighter-rouge">fread</code> began, and the second to move to the previous, unread block.</li>
    </ul>
</li>
</ul>

*   Finally, be sure to close any files you’ve opened!
