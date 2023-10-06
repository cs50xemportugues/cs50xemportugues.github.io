[NAME](#name)
=============

atoi - convert a `string` to an `int`

atoi, atol, atoll - convert a string to an integer

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <stdlib.h>

Prototype
---------

    int atoi(string s);
    

    #include <stdlib.h>
    
    int atoi(const char *nptr);
    long atol(const char *nptr);
    long long atoll(const char *nptr);

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[atoll](atoll)():

> \_ISOC99\_SOURCE || || /\* Glibc versions <= 2.19: \*/ \_BSD\_SOURCE || \_SVID\_SOURCE

[DESCRIPTION](#description)
===========================

This function converts a (positive or negative) integer from a `string` (e.g., `"50"`) to an `int` (e.g., `50`).

The [atoi](atoi)() function converts the initial portion of the string pointed to by `nptr` to `int`. The behavior is the same as

    strtol(nptr, NULL, 10);

except that [atoi](atoi)() does not detect errors.

The [atol](atol)() and [atoll](atoll)() functions behave the same as [atoi](atoi)(), except that they convert the initial portion of the string to their return type of `long` or `long long`.

[RETURN VALUE](#return-value)
=============================

This function returns its input, `s`, as an `int`.

The converted value or 0 on error.

[EXAMPLE](#example)
===================

    #include <stdio.h>#include <stdlib.h>
    int main(void)
    {
        printf("This is CS%i\n", atoi("50"));
    }
    

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[atoi](atoi)(), [atol](atol)(), [atoll](atoll)()

Thread safety

MT-Safe locale

[CONFORMING TO](#conforming-to)
===============================

POSIX.1-2001, POSIX.1-2008, C99, SVr4, 4.3BSD. C89 and POSIX.1-1996 include the functions [atoi](atoi)() and [atol](atol)() only.

[NOTES](#notes)
===============

POSIX.1 leaves the return value of [atoi](atoi)() on error unspecified. On glibc, musl libc, and uClibc, 0 is returned on error.

[BUGS](#bugs)
=============

`errno` is not set on error so there is no way to distinguish between 0 as an error and as the converted value. No checks for overflow or underflow are done. Only base-10 input can be converted. It is recommended to instead use the [strtol](strtol)() and [strtoul](strtoul)() family of functions in new programs.

[SEE ALSO](#see-also)
=====================

[atof](/3/atof)(3), [strtod](/3/strtod)(3), [strtol](/3/strtol)(3), [strtoul](/3/strtoul)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).