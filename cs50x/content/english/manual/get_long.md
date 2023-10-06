[NAME](#name)
=============

get\_long - prompt a user for an `long`

get\_long - prompts user for a line of text from stdin and returns the equivalent long

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <cs50.h>

Prototype
---------

    long get_long(string prompt, ...);
    

**#include <cs50.h>**

**long get\_long(const char \*format, ...);**

[DESCRIPTION](#description)
===========================

This function prompts the user for a `long`. If the user inputs anything other than an `long` (or a value that cannot fit in an `long`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the equivalent long; if the text does not represent a long or would cause overflow, user is reprompted.

The prompt is formatted like **printf(3)**.

[RETURN VALUE](#return-value)
=============================

This function returns the user’s input as a `long`.

Returns the long equivalent to the line read from stdin in \[**LONG\_MIN**, **LONG\_MAX**). If line can’t be read, returns **LONG\_MAX**.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        long l = get_long("Input:  ");
        printf("Output: %li\n", l);
    }
    

>     /**
>      * Returns the difference of two longs read from stdin, or LONG_MAX if there was an error.
>      */
>     long subtract_longs(void)
>     {
>         // read long from stdin
>         long i = get_long("Enter a long: ");
>     
>         // make sure we read one successfully
>         if (i == LONG_MAX)
>         {
>             return LONG_MAX;
>         }
>     
>         long j = get_long("What do you want to subtract from %ld? ", i);
>     
>         if (j == LONG_MAX)
>         {
>             return LONG_MAX;
>         }
>     
>         return i - j;
>     }

[SEE ALSO](#see-also)
=====================

>     get_char(3), get_double(3), get_float(3), get_int(3), get_string(3),
>     printf(3)