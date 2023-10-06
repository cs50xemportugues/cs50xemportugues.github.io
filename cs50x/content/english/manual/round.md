[NAME](#name)
=============

round - round a number to the nearest integer

round, roundf, roundl - round to nearest integer, away from zero

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <math.h>

Prototype
---------

    double round(double x);
    

    #include <math.h>
    
    double round(double x);
    float roundf(float x);
    long double roundl(long double x);

Link with `-lm`.

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[round](round)(), [roundf](roundf)(), [roundl](roundl)():

> \_ISOC99\_SOURCE || \_POSIX\_C\_SOURCE >= 200112L

[DESCRIPTION](#description)
===========================

This function rounds `x` to the nearest integer.

These functions round `x` to the nearest integer, but round halfway cases away from zero (regardless of the current rounding direction, see [fenv](/3/fenv)(3)), instead of to the nearest even integer like [rint](/3/rint)(3).

For example, `round(0.5)` is 1.0, and `round(-0.5)` is -1.0.

[RETURN VALUE](#return-value)
=============================

This function returns, as a `double`, `x` rounded to the nearest integer. You may safely cast that value to a `long` (or an `int` if it fits).

These functions return the rounded integer value.

If `x` is integral, +0, -0, NaN, or infinite, `x` itself is returned.

[EXAMPLE](#example)
===================

    #include <math.h>#include <stdio.h>
    int main(void)
    {
        printf("This is CS%i\n", (int) round(49.5));
    }
    

[ERRORS](#errors)
=================

No errors occur. POSIX.1-2001 documents a range error for overflows, but see NOTES.

[VERSIONS](#versions)
=====================

These functions first appeared in glibc in version 2.1.

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[round](round)(), [roundf](roundf)(), [roundl](roundl)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

C99, POSIX.1-2001, POSIX.1-2008.

[NOTES](#notes)
===============

POSIX.1-2001 contains text about overflow (which might set `errno` to **ERANGE**, or raise an **FE\_OVERFLOW** exception). In practice, the result cannot overflow on any current machine, so this error-handling stuff is just nonsense. (More precisely, overflow can happen only when the maximum value of the exponent is smaller than the number of mantissa bits. For the IEEE-754 standard 32-bit and 64-bit floating-point numbers the maximum value of the exponent is 128 (respectively, 1024), and the number of mantissa bits is 24 (respectively, 53).)

If you want to store the rounded value in an integer type, you probably want to use one of the functions described in [lround](/3/lround)(3) instead.

[SEE ALSO](#see-also)
=====================

[ceil](/3/ceil)(3), [floor](/3/floor)(3), [lround](/3/lround)(3), [nearbyint](/3/nearbyint)(3), [rint](/3/rint)(3), [trunc](/3/trunc)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).