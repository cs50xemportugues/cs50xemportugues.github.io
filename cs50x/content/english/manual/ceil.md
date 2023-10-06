[NAME](#name)
=============

ceil - calculate the ceiling of a number

ceil, ceilf, ceill - ceiling function: smallest integral value not less than argument

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <math.h>

Prototype
---------

    double ceil(double x);
    

    #include <math.h>
    
    double ceil(double x);
    float ceilf(float x);
    long double ceill(long double x);

Link with `-lm`.

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[ceilf](ceilf)(), [ceill](ceill)():

> \_ISOC99\_SOURCE || \_POSIX\_C\_SOURCE >= 200112L || /\* Since glibc 2.19: \*/ \_DEFAULT\_SOURCE || /\* Glibc versions <= 2.19: \*/ \_BSD\_SOURCE || \_SVID\_SOURCE

[DESCRIPTION](#description)
===========================

This function returns the ceiling of `x`.

These functions return the smallest integral value that is not less than `x`.

For example, `ceil(0.5)` is 1.0, and `ceil(-0.5)` is 0.0.

[RETURN VALUE](#return-value)
=============================

This function returns, as a `double`, the smallest integer that is not less than `x`. You may safely cast that value to a `long` (or an `int` if it fits).

These functions return the ceiling of `x`.

If `x` is integral, +0, -0, NaN, or infinite, `x` itself is returned.

[EXAMPLE](#example)
===================

    #include <math.h>#include <stdio.h>
    int main(void)
    {
        printf("This is CS%i\n", (int) ceil(49.9));
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

[ceil](ceil)(), [ceilf](ceilf)(), [ceill](ceill)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

C99, POSIX.1-2001, POSIX.1-2008.

The variant returning `double` also conforms to SVr4, 4.3BSD, C89.

[NOTES](#notes)
===============

SUSv2 and POSIX.1-2001 contain text about overflow (which might set `errno` to **ERANGE**, or raise an **FE\_OVERFLOW** exception). In practice, the result cannot overflow on any current machine, so this error-handling stuff is just nonsense. (More precisely, overflow can happen only when the maximum value of the exponent is smaller than the number of mantissa bits. For the IEEE-754 standard 32-bit and 64-bit floating-point numbers the maximum value of the exponent is 128 (respectively, 1024), and the number of mantissa bits is 24 (respectively, 53).)

The integral value returned by these functions may be too large to store in an integer type (`int`, `long`, etc.). To avoid an overflow, which will produce undefined results, an application should perform a range check on the returned value before assigning it to an integer type.

[SEE ALSO](#see-also)
=====================

[floor](/3/floor)(3), [lrint](/3/lrint)(3), [nearbyint](/3/nearbyint)(3), [rint](/3/rint)(3), [round](/3/round)(3), [trunc](/3/trunc)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).