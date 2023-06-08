
### `helpers.h`

Next, take a look at `helpers.h`. This file is quite short, and just provides the function prototypes for the functions you saw earlier.

Here, take note of the fact that each function takes a 2D array called `image` as an argument, where `image` is an array of `height` many rows, and each row is itself another array of `width` many `RGBTRIPLE`s. So if `image` represents the whole picture, then `image[0]` represents the first row, and `image[0][0]` represents the pixel in the upper-left corner of the image.

### `helpers.c`

Now, open up `helpers.c`. Here’s where the implementation of the functions declared in `helpers.h` belong. But note that, right now, the implementations are missing! This part is up to you.

### `Makefile`

Finally, let’s look at `Makefile`. This file specifies what should happen when we run a terminal command like `make filter`. Whereas programs you may have written before were confined to just one file, `filter` seems to use multiple files: `filter.c` and `helpers.c`. So we’ll need to tell `make` how to compile this file.

Try compiling `filter` for yourself by going to your terminal and running

    $ make filter
    

Then, you can run the program by running:

    $ ./filter -g images/yard.bmp out.bmp
    

which takes the image at `images/yard.bmp`, and generates a new image called `out.bmp` after running the pixels through the `grayscale` function. `grayscale` doesn’t do anything just yet, though, so the output image should look the same as the original yard.

Specification
-------------

Implement the functions in `helpers.c` such that a user can apply grayscale, reflection, blur, or edge detection filters to their images.

*   The function `grayscale` should take an image and turn it into a black-and-white version of the same image.
*   The `reflect` function should take an image and reflect it horizontally.
*   The `blur` function should take an image and turn it into a box-blurred version of the same image.
*   The `edges` function should take an image and highlight the edges between objects, according to the Sobel operator.

You should not modify any of the function signatures, nor should you modify any other files other than `helpers.c`.

Walkthrough
-----------

**Please note that there are 5 videos in this playlist.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/vsOsctDernw?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382OwvMbZuaMGtD9wZkhnhYj"></iframe></div>
