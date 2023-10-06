[NAME](#name)
=============

strstr - locate a substring

strstr, strcasestr - locate a substring

[SYNOPSIS](#synopsis)
=====================

Header Files
------------

    #include <cs50.h>#include <string.h>

Prototype
---------

    string strstr(string haystack, string needle);
    

    #include <string.h>
    
    char *strstr(const char *haystack, const char *needle);
    
    #define _GNU_SOURCE /* See feature_test_macros(7) */
    
    #include <string.h>
    
    char *strcasestr(const char *haystack, const char *needle);

[DESCRIPTION](#description)
===========================

This function searches `haystack` for (the first occurrence of) `needle`. In other words, it determines whether (and where) `needle` is a substring of `haystack`.

The [strstr](strstr)() function finds the first occurrence of the substring `needle` in the string `haystack`. The terminating null bytes ('\\0') are not compared.

The [strcasestr](strcasestr)() function is like [strstr](strstr)(), but ignores the case of both arguments.

[RETURN VALUE](#return-value)
=============================

If `needle` is found in `haystack`, this function returns the substring of `haystack` that begins with `needle`. (For instance, if `haystack` is `"foo bar bar baz"` and `needle` is `"bar"`, this function returns `"bar bar baz"`.) If `needle` is not found in `haystack`, this function returns `NULL`.

These functions return a pointer to the beginning of the located substring, or NULL if the substring is not found.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <string.h>#include <stdio.h>
    int main(void)
    {
        string haystack = "foo bar bar baz";
        string needle = "bar";
    
        string match = strstr(haystack, needle);
        if (match)
        {
            printf("%s\n", match);
        }
    }
    

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[strstr](strstr)()

Thread safety

MT-Safe

[strcasestr](strcasestr)()

Thread safety

MT-Safe locale

[CONFORMING TO](#conforming-to)
===============================

[strstr](strstr)(): POSIX.1-2001, POSIX.1-2008, C89, C99.

The [strcasestr](strcasestr)() function is a nonstandard extension.

[SEE ALSO](#see-also)
=====================

[index](/3/index)(3), [memchr](/3/memchr)(3), [memmem](/3/memmem)(3), [rindex](/3/rindex)(3), [strcasecmp](/3/strcasecmp)(3), [strchr](/3/strchr)(3), [string](/3/string)(3), [strpbrk](/3/strpbrk)(3), [strsep](/3/strsep)(3), [strspn](/3/strspn)(3), [strtok](/3/strtok)(3), [wcsstr](/3/wcsstr)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).