[NAME](#name)
=============

get\_int - prompt a user for an `int`

get\_int - prompts user for a line of text from stdin and returns the equivalent int

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <cs50.h>

Prototype
---------

    int get_int(string prompt, ...);
    

**#include <cs50.h>**

**int get\_int(const char \*format, ...);**

[DESCRIPTION](#description)
===========================

This function prompts the user for an `int`. If the user inputs anything other than an `int` (or a value that cannot fit in an `int`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the equivalent int; if text does not represent an int or would cause overflow, user is reprompted.

The prompt is formatted like **printf(3)**.

[RETURN VALUE](#return-value)
=============================

This function returns the user’s input as a `int`.

Returns the int equivalent to the line read from stdin in \[**INT\_MIN**, **INT\_MAX**). If line can’t be read, returns **INT\_MAX**.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        int i = get_int("Input:  ");
        printf("Output: %i\n", i);
    }
    

>     /**
>      * Returns the sum of two ints read from stdin, or INT_MAX if there was an error.
>      */
>     int add_ints(void)
>     {
>         // read int from stdin
>         int i = get_int("Enter an int: ");
>     
>         // make sure we read one successfully
>         if (i == INT_MAX)
>         {
>             return INT_MAX;
>         }
>     
>         int j = get_int("What do you want to add %d to? ", i);
>     
>         if (j == INT_MAX)
>         {
>             return INT_MAX;
>         }
>     
>         return i + j;
>     }

[SEE ALSO](#see-also)
=====================

>     get_char(3), get_double(3), get_float(3), get_long(3),
>     get_string(3), printf(3)