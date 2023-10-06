[NAME](#name)
=============

log2 - calculate the base-2 logarithm of a number

log2, log2f, log2l - base-2 logarithmic function

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <math.h>

Prototype
---------

    double log2(double x);
    

    #include <math.h>
    
    double log2(double x);
    float log2f(float x);
    long double log2l(long double x);

Link with `-lm`.

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[log2](log2)(), [log2f](log2f)(), [log2l](log2l)():

> \_ISOC99\_SOURCE || \_POSIX\_C\_SOURCE >= 200112L

[DESCRIPTION](#description)
===========================

This function calculates the base-2 logarithm of `x`.

These functions return the base 2 logarithm of `x`.

[RETURN VALUE](#return-value)
=============================

This function returns, as a `double`, the base-2 logarithm of `x`.

On success, these functions return the base 2 logarithm of `x`.

For special cases, including where `x` is 0, 1, negative, infinity, or NaN, see [log](/3/log)(3).

[EXAMPLE](#example)
===================

    #include <math.h>#include <stdio.h>
    int main(void)
    {
        printf("This is CS%i\n", (int) log2(1125899906842624));
    }
    

[ERRORS](#errors)
=================

See [math\_error](/7/math_error)(7) for information on how to determine whether an error has occurred when calling these functions.

For a discussion of the errors that can occur for these functions, see [log](/3/log)(3).

[VERSIONS](#versions)
=====================

These functions first appeared in glibc in version 2.1.

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[log2](log2)(), [log2f](log2f)(), [log2l](log2l)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

C99, POSIX.1-2001, POSIX.1-2008.

The variant returning `double` also conforms to SVr4, 4.3BSD.

[SEE ALSO](#see-also)
=====================

[cbrt](/3/cbrt)(3), [clog2](/3/clog2)(3), [log](/3/log)(3), [log10](/3/log10)(3), [sqrt](/3/sqrt)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).