
Usage
-----

As well as running your queries in `sqlite3`, you can test your queries in the VS Code terminal by running

    $ cat filename.sql | sqlite3 songs.db
    

where `filename.sql` is the file containing your SQL query.

### Hints

*   See [this SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!


<details><summary>Not sure how to solve?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/7hydPL9ZswE"></iframe></details>


### Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) is a feature presenting Spotify users’ 100 most played songs from the past year. In 2021, Spotify Wrapped calculated an [“Audio Aura”](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) for each user, a “reading of \[their\] two most prominent moods as dictated by \[their\] top songs and artists of the year.” Suppose Spotify determines an audio aura by looking at the average energy, valence, and danceability of a person’s top 100 songs from the past year. In `answers.txt`, reflect on the following questions:

*   If `songs.db` contains the top 100 songs of one listener from 2018, how would you characterize their audio aura?
*   Hypothesize about why the way you’ve calculated this aura might _not_ be very representative of the listener. What better ways of calculating this aura would you propose?

Be sure to submit `answers.txt` along with each of your `.sql` files!

### Testing

Execute the below to evaluate the correctness of your code using `check50`.

    check50 cs50/labs/2023/x/songs
    

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/labs/2023/x/songs
    

Acknowledgements
----------------

Dataset from [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).