
Usage
-----

Your program should behave per the examples below. `INFILE.bmp` is the name of the input image and `OUTFILE.bmp` is the name of the resulting image after a filter has been applied.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -e INFILE.bmp OUTFILE.bmp
``` 

Hints
-----

*   The values of a pixel’s `rgbtRed`, `rgbtGreen`, and `rgbtBlue` components are all integers, so be sure to round any floating-point numbers to the nearest integer when assigning them to a pixel value!

Testing
-------

Be sure to test all of your filters on the sample bitmap files provided!

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/problems/2023/x/filter/more
    

Execute the below to evaluate the style of your code using `style50`.

    style50 helpers.c
    

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/filter/more