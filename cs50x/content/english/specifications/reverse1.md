Reverse
=======

Implement a program that reverses a WAV file, per the below.

    ./reverse input.wav output.wav
    

Background
----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/J9iyqMwYtG4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


In Electric Light Orchestra’s “Fire on High”, there’s something a little off about the first minute or so of the music. If you take a listen, it sounds almost like the audio is playing backwards. As it turns out, if you play the beginning section of the song in reverse, you’ll hear the following:

_“The music is reversible. Time is not. Turn back, turn back!”_

Creepy, right? This is a technique called “backmasking,” or hiding messages in music that can only be heard when the song is played backwards. Many artists have used (or been suspected of using) this technique in their songs. To be able to do our own investigation into backmasking, we’ve asked you to write a program that can reverse WAV files for us!

Unlike MP3 audio files, WAV files are not compressed. This makes the files much easier to edit and manipulate, which is useful for the task at hand. To learn a little more about WAV files, we need to take a closer look at the WAV file format.

