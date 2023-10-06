[NAME](#name)
=============

strcasecmp - compare two strings ignoring case

strcasecmp, strncasecmp - compare two strings ignoring case

[SYNOPSIS](#synopsis)
=====================

Header Files
------------

    #include <cs50.h>#include <strings.h>

Prototype
---------

    int strcasecmp(string s1, string s2);
    

    #include <strings.h>
    
    int strcasecmp(const char *s1, const char *s2);
    
    int strncasecmp(const char *s1, const char *s2, size_t n);

[DESCRIPTION](#description)
===========================

This function compares two strings case-insensitively.

The [strcasecmp](strcasecmp)() function performs a byte-by-byte comparison of the strings `s1` and `s2`, ignoring the case of the characters. It returns an integer less than, equal to, or greater than zero if `s1` is found, respectively, to be less than, to match, or be greater than `s2`.

The [strncasecmp](strncasecmp)() function is similar, except that it compares no more than `n` bytes of `s1` and `s2`.

[RETURN VALUE](#return-value)
=============================

This function returns

*   an `int` less than `0` if `s1` comes before `s2`, ignoring case,
*   `0` if `s1` is the same as `s2`, ignoring case, or
*   an `int` greater than `0` if `s1` comes after `s2`, ignoring case.

The strings are compared using “ASCIIbetical” order, based on the ASCII values of their characters. For instance, `"AAA"` would come before `"BBB"`.

The [strcasecmp](strcasecmp)() and [strncasecmp](strncasecmp)() functions return an integer less than, equal to, or greater than zero if `s1` is, after ignoring case, found to be less than, to match, or be greater than `s2`, respectively.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <stdio.h>#include <strings.h>
    int main(void)
    {
        string s1 = get_string("s1: ");
        string s2 = get_string("s2: ");
        if (strcasecmp(s1, s2) == 0)
        {
            printf("Those are the same, ignoring case.\n");
        }
        else
        {
            printf("Those are different, even ignoring case.\n");
        }
    }
    

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[strcasecmp](strcasecmp)(), [strncasecmp](strncasecmp)()

Thread safety

MT-Safe locale

[CONFORMING TO](#conforming-to)
===============================

4.4BSD, POSIX.1-2001, POSIX.1-2008.

[NOTES](#notes)
===============

The [strcasecmp](strcasecmp)() and [strncasecmp](strncasecmp)() functions first appeared in 4.4BSD, where they were declared in `<string.h>`. Thus, for reasons of historical compatibility, the glibc `<string.h>` header file also declares these functions, if the **\_DEFAULT\_SOURCE** (or, in glibc 2.19 and earlier, **\_BSD\_SOURCE**) feature test macro is defined.

The POSIX.1-2008 standard says of these functions:

> When the **LC\_CTYPE** category of the locale being used is from the POSIX locale, these functions shall behave as if the strings had been converted to lowercase and then a byte comparison performed. Otherwise, the results are unspecified.

[SEE ALSO](#see-also)
=====================

[bcmp](/3/bcmp)(3), [memcmp](/3/memcmp)(3), [strcmp](/3/strcmp)(3), [strcoll](/3/strcoll)(3), [string](/3/string)(3), [strncmp](/3/strncmp)(3), [wcscasecmp](/3/wcscasecmp)(3), [wcsncasecmp](/3/wcsncasecmp)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).