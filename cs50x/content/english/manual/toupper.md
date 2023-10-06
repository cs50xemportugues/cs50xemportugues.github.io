[NAME](#name)
=============

toupper - convert a `char` to uppercase

toupper, tolower, toupper\_l, tolower\_l - convert uppercase or lowercase

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <ctype.h>

Prototype
---------

    int toupper(char c);
    

Think of this function as taking a `char` as input.

    #include <ctype.h>
    
    int toupper(int c);
    int tolower(int c);
    
    int toupper_l(int c, locale_t locale);
    int tolower_l(int c, locale_t locale);

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[toupper\_l](toupper_l)(), [tolower\_l](tolower_l)():

> Since glibc 2.10:
> 
> \_XOPEN\_SOURCE >= 700
> 
> Before glibc 2.10:
> 
> \_GNU\_SOURCE

[DESCRIPTION](#description)
===========================

This function converts `c` to uppercase.

These functions convert lowercase letters to uppercase, and vice versa.

If `c` is a lowercase letter, [toupper](toupper)() returns its uppercase equivalent, if an uppercase representation exists in the current locale. Otherwise, it returns `c`. The [toupper\_l](toupper_l)() function performs the same task, but uses the locale referred to by the locale handle `locale`.

If `c` is an uppercase letter, [tolower](tolower)() returns its lowercase equivalent, if a lowercase representation exists in the current locale. Otherwise, it returns `c`. The [tolower\_l](tolower_l)() function performs the same task, but uses the locale referred to by the locale handle `locale`.

If `c` is neither an `unsigned char` value nor **EOF**, the behavior of these functions is undefined.

The behavior of [toupper\_l](toupper_l)() and [tolower\_l](tolower_l)() is undefined if `locale` is the special locale object **LC\_GLOBAL\_LOCALE** (see [duplocale](/3/duplocale)(3)) or is not a valid locale object handle.

[RETURN VALUE](#return-value)
=============================

If `c` is a lowercase letter (`a` through `z`), this function returns its uppercase equivalent (`A` through `Z`). If `c` is not a lowercase letter, this function returns `c` itself.

The value returned is that of the converted letter, or `c` if the conversion was not possible.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <ctype.h>#include <stdio.h>
    int main(void)
    {
        char c = get_char("Input:  ");
        printf("Output: %c\n", toupper(c));
    }
    

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[toupper](toupper)(), [tolower](tolower)(),  
[toupper\_l](toupper_l)(), [tolower\_l](tolower_l)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

[toupper](toupper)(), [tolower](tolower)(): C89, C99, 4.3BSD, POSIX.1-2001, POSIX.1-2008.

[toupper\_l](toupper_l)(), [tolower\_l](tolower_l)(): POSIX.1-2008.

[NOTES](#notes)
===============

The standards require that the argument `c` for these functions is either **EOF** or a value that is representable in the type `unsigned char`. If the argument `c` is of type `char`, it must be cast to _unsigned char_, as in the following example:

    char c;
    ...
    res = toupper((unsigned char) c);

This is necessary because `char` may be the equivalent `signed char`, in which case a byte where the top bit is set would be sign extended when converting to `int`, yielding a value that is outside the range of `unsigned char`.

The details of what constitutes an uppercase or lowercase letter depend on the locale. For example, the default **"C"** locale does not know about umlauts, so no conversion is done for them.

In some non-English locales, there are lowercase letters with no corresponding uppercase equivalent; the German sharp s is one example.

[SEE ALSO](#see-also)
=====================

[isalpha](/3/isalpha)(3), [newlocale](/3/newlocale)(3), [setlocale](/3/setlocale)(3), [towlower](/3/towlower)(3), [towupper](/3/towupper)(3), [uselocale](/3/uselocale)(3), [locale](/7/locale)(7)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).