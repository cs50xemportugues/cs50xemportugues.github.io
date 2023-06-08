
Specification
-------------

Implement the functions in `helpers.c` such that a user can apply grayscale, sepia, reflection, or blur filters to their images.

*   The function `grayscale` should take an image and turn it into a black-and-white version of the same image.
*   The function `sepia` should take an image and turn it into a sepia version of the same image.
*   The `reflect` function should take an image and reflect it horizontally.
*   Finally, the `blur` function should take an image and turn it into a box-blurred version of the same image.

You should not modify any of the function signatures, nor should you modify any other files other than `helpers.c`.

Walkthrough
-----------

**Please note that there are 5 videos in this playlist.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/K0v9byp9jd0?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut"></iframe></div>


Usage
-----

Your program should behave per the examples below. `INFILE.bmp` is the name of the input image and `OUTFILE.bmp` is the name of the resulting image after a filter has been applied.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -s INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```

Hints
-----

*   The values of a pixel’s `rgbtRed`, `rgbtGreen`, and `rgbtBlue` components are all integers, so be sure to round any floating-point numbers to the nearest integer when assigning them to a pixel value!
*   When implementing the `grayscale` function, you’ll need to average the values of 3 integers. Why might you want to divide the sum of these integers by 3.0 and not 3?
*   In the `reflect` function, you’ll need to swap the values of pixels on opposite sides of a row. Recall from lecture how we implemented swapping two values with a temporary variable. No need to use a separate function for swapping unless you would like to!
*   How might a function that returns the lesser of two integers come in handy while implementing `sepia`, particularly when you need to make sure a color’s value is no higher than 255?
*   When implementing the `blur` function, you might find that blurring one pixel ends up affecting the blur of another pixel. Perhaps create a copy of `image` (the function’s third argument) by declaring a new (two-dimensional) array with code like `RGBTRIPLE copy[height][width];` and copying `image` into `copy`, pixel by pixel, with nested `for` loops? And then read pixels’ colors from `copy` but write (i.e., change) pixels’ colors in `image`?

Testing
-------

Be sure to test all of your filters on the sample bitmap files provided!

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/problems/2023/x/filter/less
    

Execute the below to evaluate the style of your code using `style50`.

    style50 helpers.c
    

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/filter/less