[NAME](#name)
=============

atof - convert a `string` to a `float`

atof - convert a string to a double

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <stdlib.h>

Prototype
---------

    float atof(string s);
    

    #include <stdlib.h>
    
    double atof(const char *nptr);

[DESCRIPTION](#description)
===========================

This function converts a (positive or negative) floating-point value from a `string` (e.g., `"50.0"`) to a `float` (e.g., `50.0`).

The [atof](atof)() function converts the initial portion of the string pointed to by `nptr` to `double`. The behavior is the same as

    strtod(nptr, NULL);

except that [atof](atof)() does not detect errors.

[RETURN VALUE](#return-value)
=============================

This function returns its input, `s`, as a `float`.

The converted value.

[EXAMPLE](#example)
===================

    #include <stdio.h>#include <stdlib.h>
    int main(void)
    {
        printf("This is CS%.0f\n", atof("50.0"));
    }
    

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[atof](atof)()

Thread safety

MT-Safe locale

[CONFORMING TO](#conforming-to)
===============================

POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.

[SEE ALSO](#see-also)
=====================

[atoi](/3/atoi)(3), [atol](/3/atol)(3), [strfromd](/3/strfromd)(3), [strtod](/3/strtod)(3), [strtol](/3/strtol)(3), [strtoul](/3/strtoul)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).