[NAME](#name)
=============

strlen - calculate the length of a string

[SYNOPSIS](#synopsis)
=====================

strlen - calculate the length of a string

Header Files
------------

    #include <cs50.h>#include <string.h>

Prototype
---------

    int strlen(string s);
    

    #include <string.h>
    
    size_t strlen(const char *s);

[DESCRIPTION](#description)
===========================

This function calculates the length of `s`.

The [strlen](strlen)() function calculates the length of the string pointed to by `s`, excluding the terminating null byte ('\\0').

[RETURN VALUE](#return-value)
=============================

This function returns the number of characters in `s`, excluding the terminating NUL byte (i.e., `'\0'`).

The [strlen](strlen)() function returns the number of bytes in the string pointed to by `s`.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <stdio.h>#include <string.h>
    int main(void)
    {
        string s = get_string("Input:  ");
        printf("Output: ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            printf("%c", s[i]);
        }
        printf("\n");
    }
    

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[strlen](strlen)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

POSIX.1-2001, POSIX.1-2008, C89, C99, C11, SVr4, 4.3BSD.

[SEE ALSO](#see-also)
=====================

[string](/3/string)(3), [strnlen](/3/strnlen)(3), [wcslen](/3/wcslen)(3), [wcsnlen](/3/wcsnlen)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).