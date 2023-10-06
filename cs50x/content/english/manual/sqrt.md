[NAME](#name)
=============

sqrt - calculate the square root of a number

sqrt, sqrtf, sqrtl - square root function

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <math.h>

Prototype
---------

    double sqrt(double x);
    

    #include <math.h>
    
    double sqrt(double x);
    float sqrtf(float x);
    long double sqrtl(long double x);

Link with `-lm`.

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[sqrtf](sqrtf)(), [sqrtl](sqrtl)():

> \_ISOC99\_SOURCE || \_POSIX\_C\_SOURCE >= 200112L || /\* Since glibc 2.19: \*/ \_DEFAULT\_SOURCE || /\* Glibc versions <= 2.19: \*/ \_BSD\_SOURCE || \_SVID\_SOURCE

[DESCRIPTION](#description)
===========================

This function calculates the square root of `x`.

These functions return the nonnegative square root of `x`.

[RETURN VALUE](#return-value)
=============================

This function returns, as a `double`, the square root of `x`.

On success, these functions return the square root of `x`.

If `x` is a NaN, a NaN is returned.

If `x` is +0 (-0), +0 (-0) is returned.

If `x` is positive infinity, positive infinity is returned.

If `x` is less than -0, a domain error occurs, and a NaN is returned.

[EXAMPLE](#example)
===================

    #include <math.h>#include <stdio.h>
    int main(void)
    {
        printf("This is CS%i\n", (int) sqrt(2500));
    }
    

[ERRORS](#errors)
=================

See [math\_error](/7/math_error)(7) for information on how to determine whether an error has occurred when calling these functions.

The following errors can occur:

Domain error: `x` less than -0

`errno` is set to **EDOM**. An invalid floating-point exception (**FE\_INVALID**) is raised.

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[sqrt](sqrt)(), [sqrtf](sqrtf)(), [sqrtl](sqrtl)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

C99, POSIX.1-2001, POSIX.1-2008.

The variant returning `double` also conforms to SVr4, 4.3BSD, C89.

[SEE ALSO](#see-also)
=====================

[cbrt](/3/cbrt)(3), [csqrt](/3/csqrt)(3), [hypot](/3/hypot)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).