Lab 8: Trivia
=============

<div class="alert" data-alert="warning" role="alert"><p>You are welcome to collaborate with one or two classmates on this lab, though it is expected that every student in any such group contribute equally to the lab.</p></div>


Write a webpage that lets users answer trivia questions.

![screenshot of trivia questions](https://cs50.harvard.edu/x/2023/labs/8/questions.png)

Getting Started
---------------

<div class="alert" data-alert="primary" role="alert"><p>Started CS50x in 2021 or prior and need to migrate your work from CS50 IDE to the new VS Code codespace? Be sure to check out our instructions on how to <a href="../../new/">migrate</a> your files!</p></div>

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $
    

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/labs/8/trivia.zip
    

followed by Enter in order to download a ZIP called `trivia.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip trivia.zip
    

to create a folder called `trivia`. You no longer need the ZIP file, so you can execute

    rm trivia.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd trivia
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    trivia/ $
    

If all was successful, you should execute

    ls
    

and you should see an `index.html` file and a `styles.css` file.

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

Implementation Details
----------------------

Design a webpage using HTML, CSS, and JavaScript to let users answer trivia questions.

*   In `index.html`, add beneath “Part 1” a multiple-choice trivia question of your choosing with HTML.
    *   You should use an `h3` heading for the text of your question.
    *   You should have one `button` for each of the possible answer choices. There should be at least three answer choices, of which exactly one should be correct.
*   Using JavaScript, add logic so that the buttons change colors when a user clicks on them.
    *   If a user clicks on a button with an incorrect answer, the button should turn red and text should appear beneath the question that says “Incorrect”.
    *   If a user clicks on a button with the correct answer, the button should turn green and text should appear beneath the question that says “Correct!”.
*   In `index.html`, add beneath “Part 2” a text-based free response question of your choosing with HTML.
    *   You should use an `h3` heading for the text of your question.
    *   You should use an `input` field to let the user type a response.
    *   You should use a `button` to let the user confirm their answer.
*   Using JavaScript, add logic so that the text field changes color when a user confirms their answer.
    *   If the user types an incorrect answer and presses the confirmation button, the text field should turn red and text should appear beneath the question that says “Incorrect”.
    *   If the user types the correct answer and presses the confirmation button, the input field should turn green and text should appear beneath the question that says “Correct!”.

Optionally, you may also:

*   Edit `styles.css` to change the CSS of your webpage!
*   Add additional trivia questions to your trivia quiz if you would like!

### Walkthrough

<div class="alert" data-alert="primary" role="alert"><p>This video was recorded when the course was still using CS50 IDE for writing code. Though the interface may look different from your codespace, the behavior of the two environments should be largely similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/WGd0Jx7rxUo"></iframe>


### Hints

*   Use [`document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) to query for a single HTML element.
*   Use [`document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) to query for multiple HTML elements that match a query. The function returns an array of all matching elements.


<details><summary>Not sure how to solve?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/FLlI7rSSV_M"></iframe></details>


### Testing

No `check50` for this lab, as implementations will vary based on your questions! But be sure to test both incorrect and correct responses for each of your questions to ensure that your webpage responds appropriately.

Run `http-server` in your terminal while in your `lab8` directory to start a web server that serves your webpage.

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/labs/2023/x/trivia