[NAME](#name)
=============

isdigit - check whether a character is a digit

isalnum, isalpha, isascii, isblank, iscntrl, isdigit, isgraph, islower, isprint, ispunct, isspace, isupper, isxdigit, isalnum\_l, isalpha\_l, isascii\_l, isblank\_l, iscntrl\_l, isdigit\_l, isgraph\_l, islower\_l, isprint\_l, ispunct\_l, isspace\_l, isupper\_l, isxdigit\_l - character classification functions

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <ctype.h>

Prototype
---------

    int isdigit(char c);
    

Think of this function as taking a `char` as input.

    #include <ctype.h>
    
    int isalnum(int c);
    int isalpha(int c);
    int iscntrl(int c);
    int isdigit(int c);
    int isgraph(int c);
    int islower(int c);
    int isprint(int c);
    int ispunct(int c);
    int isspace(int c);
    int isupper(int c);
    int isxdigit(int c);
    
    int isascii(int c);
    int isblank(int c);
    
    int isalnum_l(int c, locale_t locale);
    int isalpha_l(int c, locale_t locale);
    int isblank_l(int c, locale_t locale);
    int iscntrl_l(int c, locale_t locale);
    int isdigit_l(int c, locale_t locale);
    int isgraph_l(int c, locale_t locale);
    int islower_l(int c, locale_t locale);
    int isprint_l(int c, locale_t locale);
    int ispunct_l(int c, locale_t locale);
    int isspace_l(int c, locale_t locale);
    int isupper_l(int c, locale_t locale);
    int isxdigit_l(int c, locale_t locale);
    
    int isascii_l(int c, locale_t locale);

> Feature Test Macro Requirements for glibc (see [feature\_test\_macros](/7/feature_test_macros)(7)):

[isascii](isascii)():

> \_XOPEN\_SOURCE || /\* Glibc since 2.19: \*/ \_DEFAULT\_SOURCE || /\* Glibc versions <= 2.19: \*/ \_SVID\_SOURCE

[isblank](isblank)():

> \_ISOC99\_SOURCE || \_POSIX\_C\_SOURCE >= 200112L

[isalnum\_l](isalnum_l)(), [isalpha\_l](isalpha_l)(), [isblank\_l](isblank_l)(), [iscntrl\_l](iscntrl_l)(), [isdigit\_l](isdigit_l)(), [isgraph\_l](isgraph_l)(), [islower\_l](islower_l)(), [isprint\_l](isprint_l)(), [ispunct\_l](ispunct_l)(), [isspace\_l](isspace_l)(), [isupper\_l](isupper_l)(), [isxdigit\_l](isxdigit_l)():

> Since glibc 2.10:
> 
> \_XOPEN\_SOURCE >= 700
> 
> Before glibc 2.10:
> 
> \_GNU\_SOURCE

[isascii\_l](isascii_l)():

> Since glibc 2.10:
> 
> \_XOPEN\_SOURCE >= 700 && (\_SVID\_SOURCE || \_BSD\_SOURCE)
> 
> Before glibc 2.10:
> 
> \_GNU\_SOURCE

[DESCRIPTION](#description)
===========================

This function checks whether `c` is a decimal digit (`'0'` through `'9'`) or not. In other words, it checks whether the [ASCII](https://asciichart.com/) value of `c` is between 48 and 57, inclusive.

These functions check whether `c`, which must have the value of an `unsigned char` or **EOF**, falls into a certain character class according to the specified locale. The functions without the "\_l" suffix perform the check based on the current locale.

The functions with the "\_l" suffix perform the check based on the locale specified by the locale object `locale`. The behavior of these functions is undefined if `locale` is the special locale object **LC\_GLOBAL\_LOCALE** (see [duplocale](/3/duplocale)(3)) or is not a valid locale object handle.

The list below explains the operation of the functions without the "\_l" suffix; the functions with the "\_l" suffix differ only in using the locale object `locale` instead of the current locale.

[isalnum](isalnum)()

checks for an alphanumeric character; it is equivalent to **([isalpha](isalpha)(**`c`**) || [isdigit](isdigit)(**`c`**))**`.`

[isalpha](isalpha)()

checks for an alphabetic character; in the standard **"C"** locale, it is equivalent to **([isupper](isupper)(**`c`**) || [islower](islower)(**`c`**))**`.` In some locales, there may be additional characters for which [isalpha](isalpha)() is true—letters which are neither uppercase nor lowercase.

[isascii](isascii)()

checks whether `c` is a 7-bit `unsigned char` value that fits into the ASCII character set.

[isblank](isblank)()

checks for a blank character; that is, a space or a tab.

[iscntrl](iscntrl)()

checks for a control character.

[isdigit](isdigit)()

checks for a digit (0 through 9).

[isgraph](isgraph)()

checks for any printable character except space.

[islower](islower)()

checks for a lowercase character.

[isprint](isprint)()

checks for any printable character including space.

[ispunct](ispunct)()

checks for any printable character which is not a space or an alphanumeric character.

[isspace](isspace)()

checks for white-space characters. In the **"C"** and **"POSIX"** locales, these are: space, form-feed (**'\\f'**), newline (**'\\n'**), carriage return (**'\\r'**), horizontal tab (**'\\t'**), and vertical tab (**'\\v'**).

[isupper](isupper)()

checks for an uppercase letter.

[isxdigit](isxdigit)()

checks for hexadecimal digits, that is, one of  
**0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F**.

[RETURN VALUE](#return-value)
=============================

This function returns a non-zero `int` if `c` is a decimal digit and `0` if `c` is not a decimal digit.

The values returned are nonzero if the character `c` falls into the tested class, and zero if not.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <ctype.h>#include <stdio.h>
    int main(void)
    {
        char c = get_char("Input: ");
        if (isdigit(c))
        {
            printf("Your input is a digit.\n");
        }
        else
        {
            printf("Your input is not a digit.\n");
        }
    }
    

[VERSIONS](#versions)
=====================

[isalnum\_l](isalnum_l)(), [isalpha\_l](isalpha_l)(), [isblank\_l](isblank_l)(), [iscntrl\_l](iscntrl_l)(), [isdigit\_l](isdigit_l)(), [isgraph\_l](isgraph_l)(), [islower\_l](islower_l)(), [isprint\_l](isprint_l)(), [ispunct\_l](ispunct_l)(), [isspace\_l](isspace_l)(), [isupper\_l](isupper_l)(), [isxdigit\_l](isxdigit_l)(), and [isascii\_l](isascii_l)() are available since glibc 2.3.

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[isalnum](isalnum)(), [isalpha](isalpha)(), [isascii](isascii)(), [isblank](isblank)(), [iscntrl](iscntrl)(), [isdigit](isdigit)(), [isgraph](isgraph)(), [islower](islower)(), [isprint](isprint)(), [ispunct](ispunct)(), [isspace](isspace)(), [isupper](isupper)(), [isxdigit](isxdigit)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

C89 specifies [isalnum](isalnum)(), [isalpha](isalpha)(), [iscntrl](iscntrl)(), [isdigit](isdigit)(), [isgraph](isgraph)(), [islower](islower)(), [isprint](isprint)(), [ispunct](ispunct)(), [isspace](isspace)(), [isupper](isupper)(), and [isxdigit](isxdigit)(), but not [isascii](isascii)() and [isblank](isblank)(). POSIX.1-2001 also specifies those functions, and also [isascii](isascii)() (as an XSI extension) and [isblank](isblank)(). C99 specifies all of the preceding functions, except [isascii](isascii)().

POSIX.1-2008 marks [isascii](isascii)() as obsolete, noting that it cannot be used portably in a localized application.

POSIX.1-2008 specifies [isalnum\_l](isalnum_l)(), [isalpha\_l](isalpha_l)(), [isblank\_l](isblank_l)(), [iscntrl\_l](iscntrl_l)(), [isdigit\_l](isdigit_l)(), [isgraph\_l](isgraph_l)(), [islower\_l](islower_l)(), [isprint\_l](isprint_l)(), [ispunct\_l](ispunct_l)(), [isspace\_l](isspace_l)(), [isupper\_l](isupper_l)(), and [isxdigit\_l](isxdigit_l)().

[isascii\_l](isascii_l)() is a GNU extension.

[NOTES](#notes)
===============

The standards require that the argument `c` for these functions is either **EOF** or a value that is representable in the type `unsigned char`. If the argument `c` is of type `char`, it must be cast to _unsigned char_, as in the following example:

    char c;
    ...
    res = toupper((unsigned char) c);

This is necessary because `char` may be the equivalent of `signed char`, in which case a byte where the top bit is set would be sign extended when converting to `int`, yielding a value that is outside the range of `unsigned char`.

The details of what characters belong to which class depend on the locale. For example, [isupper](isupper)() will not recognize an A-umlaut (Ä) as an uppercase letter in the default **C** locale.

[SEE ALSO](#see-also)
=====================

[iswalnum](/3/iswalnum)(3), [iswalpha](/3/iswalpha)(3), [iswblank](/3/iswblank)(3), [iswcntrl](/3/iswcntrl)(3), [iswdigit](/3/iswdigit)(3), [iswgraph](/3/iswgraph)(3), [iswlower](/3/iswlower)(3), [iswprint](/3/iswprint)(3), [iswpunct](/3/iswpunct)(3), [iswspace](/3/iswspace)(3), [iswupper](/3/iswupper)(3), [iswxdigit](/3/iswxdigit)(3), [newlocale](/3/newlocale)(3), [setlocale](/3/setlocale)(3), [toascii](/3/toascii)(3), [tolower](/3/tolower)(3), [toupper](/3/toupper)(3), [uselocale](/3/uselocale)(3), [ascii](/7/ascii)(7), [locale](/7/locale)(7)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).