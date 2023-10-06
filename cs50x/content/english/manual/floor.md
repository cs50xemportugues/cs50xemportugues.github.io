[NAME](#name)
=============

floor - calculate the floor of a number

floor, floorf, floorl - largest integral value not greater than argument

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <math.h>

Prototype
---------

    double floor(double x);
    

    #include <math.h>
    
    double floor(double x);
    float floorf(float x);
    long double floorl(long double x);

Link with `-lm`.

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[floorf](floorf)(), [floorl](floorl)():

> \_ISOC99\_SOURCE || \_POSIX\_C\_SOURCE >= 200112L || /\* Since glibc 2.19: \*/ \_DEFAULT\_SOURCE || /\* Glibc versions <= 2.19: \*/ \_BSD\_SOURCE || \_SVID\_SOURCE

[DESCRIPTION](#description)
===========================

This function returns the floor of `x`.

These functions return the largest integral value that is not greater than `x`.

For example, `floor(0.5)` is 0.0, and `floor(-0.5)` is -1.0.

[RETURN VALUE](#return-value)
=============================

This function returns, as a `double`, the largest integer that is not greater than `x`. You may safely cast that value to a `long` (or an `int` if it fits).

These functions return the floor of `x`.

If `x` is integral, +0, -0, NaN, or an infinity, `x` itself is returned.

[EXAMPLE](#example)
===================

    #include <math.h>#include <stdio.h>
    int main(void)
    {
        printf("This is CS%i\n", (int) floor(50.1));
    }
    

[ERRORS](#errors)
=================

No errors occur. POSIX.1-2001 documents a range error for overflows, but see NOTES.

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[floor](floor)(), [floorf](floorf)(), [floorl](floorl)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

C99, POSIX.1-2001, POSIX.1-2008.

The variant returning `double` also conforms to SVr4, 4.3BSD, C89.

[NOTES](#notes)
===============

SUSv2 and POSIX.1-2001 contain text about overflow (which might set `errno` to **ERANGE**, or raise an **FE\_OVERFLOW** exception). In practice, the result cannot overflow on any current machine, so this error-handling stuff is just nonsense. (More precisely, overflow can happen only when the maximum value of the exponent is smaller than the number of mantissa bits. For the IEEE-754 standard 32-bit and 64-bit floating-point numbers the maximum value of the exponent is 128 (respectively, 1024), and the number of mantissa bits is 24 (respectively, 53).)

[SEE ALSO](#see-also)
=====================

[ceil](/3/ceil)(3), [lrint](/3/lrint)(3), [nearbyint](/3/nearbyint)(3), [rint](/3/rint)(3), [round](/3/round)(3), [trunc](/3/trunc)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).