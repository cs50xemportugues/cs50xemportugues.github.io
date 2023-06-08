
Testing
-------

If you want to see how your site looks while you work on it, you can run `http-server`. Command- or control-click on the first link presented by http-server, which should open your webpage in a new tab. You should then be able to refresh the tab containing your webpage to see your latest changes.

Recall also that by opening Developer Tools in Google Chrome, you can _simulate_ visiting your page on a mobile device by clicking the phone-shaped icon to the left of **Elements** in the developer tools window, or, once the Developer Tools tab has already been opened, by typing `Ctrl`+`Shift`+`M` on a PC or `Cmd`+`Shift`+`M` on a Mac, rather than needing to visit your site on a mobile device separately!

Assessment
----------

No `check50` for this assignment! Instead, your site’s correctness will be assessed based on whether you meet the requirements of the specification as outlined above, and whether your HTML is well-formed and valid. To ensure that your pages are, you can use this [Markup Validation Service](https://validator.w3.org/#validate_by_input), copying and pasting your HTML directly into the provided text box. Take care to eliminate any warnings or errors suggested by the validator before submitting!

Consider also:

*   whether the aesthetics of your site are such that it is intuitive and straightforward for a user to navigate;
*   whether your CSS has been factored out into a separate CSS file(s); and
*   whether you have avoided repetition and redundancy by “cascading” style properties from parent tags.

Afraid `style50` does not support HTML files, and so it is incumbent upon you to indent and align your HTML tags cleanly. Know also that you can create an HTML comment with:

    <!-- Comment goes here -->
    

but commenting your HTML code is not as imperative as it is when commenting code in, say, C or Python. You can also comment your CSS, in CSS files, with:

    /* Comment goes here */
    

Hints
-----

For fairly comprehensive guides on the languages introduced in this problem, check out these tutorials:

*   [HTML](https://www.w3schools.com/html/)
*   [CSS](https://www.w3schools.com/css/)
*   [JavaScript](https://www.w3schools.com/js/)

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/homepage