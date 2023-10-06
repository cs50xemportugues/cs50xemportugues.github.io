[NAME](#name)
=============

random - generate a pseudorandom number

random, srandom, initstate, setstate - random number generator

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #define _DEFAULT_SOURCE#include <stdlib.h>

Prototype
---------

    long random(void);
    

Defining `_DEFAULT_SOURCE` in this way enables `random` within `stdlib.h`.

    #include <stdlib.h>
    
    long random(void);
    
    void srandom(unsigned seed);
    
    char *initstate(unsigned seed, char *state, size_t n);
    
    char *setstate(char *state);

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[random](random)(), [srandom](srandom)(), [initstate](initstate)(), [setstate](setstate)():

> \_XOPEN\_SOURCE >= 500 || /\* Glibc since 2.19: \*/ \_DEFAULT\_SOURCE || /\* Glibc versions <= 2.19: \*/ \_SVID\_SOURCE || \_BSD\_SOURCE

[DESCRIPTION](#description)
===========================

This function generates a pseudorandom number between `0` and `RAND_MAX`, inclusive, where `RAND_MAX` is a constant defined in `stdlib.h`.

To return a pseudorandom floating-point value between `0.0` and `1.0`, exclusive, instead, it’s common to divide the return value of [random](random) by `(double) RAND_MAX + 1`, as in:

    float number = random() / ((double) RAND_MAX + 1);
    

To return a pseudorandom integer between `0` and `N`, exclusive, where `N` is some integer, it’s common to divide the return value of [random](random) by `(double) RAND_MAX + 1` and then multiply the quotient by `N`, as in:

    int number = (random() / ((double) RAND_MAX + 1)) * N;
    

The [random](random)() function uses a nonlinear additive feedback random number generator employing a default table of size 31 long integers to return successive pseudo-random numbers in the range from 0 to 2^31 - 1. The period of this random number generator is very large, approximately `16 * ((2^31) - 1)`.

The [srandom](srandom)() function sets its argument as the seed for a new sequence of pseudo-random integers to be returned by [random](random)(). These sequences are repeatable by calling [srandom](srandom)() with the same seed value. If no seed value is provided, the [random](random)() function is automatically seeded with a value of 1.

The [initstate](initstate)() function allows a state array `state` to be initialized for use by [random](random)(). The size of the state array `n` is used by [initstate](initstate)() to decide how sophisticated a random number generator it should use—the larger the state array, the better the random numbers will be. Current "optimal" values for the size of the state array `n` are 8, 32, 64, 128, and 256 bytes; other amounts will be rounded down to the nearest known amount. Using less than 8 bytes results in an error. `seed` is the seed for the initialization, which specifies a starting point for the random number sequence, and provides for restarting at the same point.

The [setstate](setstate)() function changes the state array used by the [random](random)() function. The state array `state` is used for random number generation until the next call to [initstate](initstate)() or [setstate](setstate)(). `state` must first have been initialized using [initstate](initstate)() or be the result of a previous call of [setstate](setstate)().

[RETURN VALUE](#return-value)
=============================

This function returns the pseudorandomly generated number as a `long`.

The [random](random)() function returns a value between 0 and `(2^31) - 1`. The [srandom](srandom)() function returns no value.

The [initstate](initstate)() function returns a pointer to the previous state array. On error, `errno` is set to indicate the cause.

On success, [setstate](setstate)() returns a pointer to the previous state array. On error, it returns NULL, with `errno` set to indicate the cause of the error.

[EXAMPLE](#example)
===================

    #define _DEFAULT_SOURCE#include <stdlib.h>
    #include <stdio.h>#include <time.h>
    int main(void)
    {
        srandom(time(NULL));
        printf("%lu\n", random());
        printf("%lu\n", random());
        printf("%lu\n", random());
    }
    

Calling `time` with an input of `NULL`, a constant defined in `stdlib.h`, returns the current time in seconds.

[ERRORS](#errors)
=================

**EINVAL**

The `state` argument given to [setstate](setstate)() was NULL.

**EINVAL**

A state array of less than 8 bytes was specified to [initstate](initstate)().

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[random](random)(), [srandom](srandom)(),  
[initstate](initstate)(), [setstate](setstate)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

POSIX.1-2001, POSIX.1-2008, 4.3BSD.

[NOTES](#notes)
===============

The [random](random)() function should not be used in multithreaded programs where reproducible behavior is required. Use [random\_r](/3/random_r)(3) for that purpose.

Random-number generation is a complex topic. _Numerical Recipes in C: The Art of Scientific Computing_ (William H. Press, Brian P. Flannery, Saul A. Teukolsky, William T. Vetterling; New York: Cambridge University Press, 2007, 3rd ed.) provides an excellent discussion of practical random-number generation issues in Chapter 7 (Random Numbers).

For a more theoretical discussion which also covers many practical issues in depth, see Chapter 3 (Random Numbers) in Donald E. Knuth's `The Art of Computer Programming`, volume 2 (Seminumerical Algorithms), 2nd ed.; Reading, Massachusetts: Addison-Wesley Publishing Company, 1981.

[BUGS](#bugs)
=============

According to POSIX, [initstate](initstate)() should return NULL on error. In the glibc implementation, `errno` is (as specified) set on error, but the function does not return NULL.

[SEE ALSO](#see-also)
=====================

[getrandom](/2/getrandom)(2), [drand48](/3/drand48)(3), [rand](/3/rand)(3), [random\_r](/3/random_r)(3), [srand](/3/srand)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).