[NAME](#name)
=============

get\_float - prompt a user for a `float`

get\_float - prompts user for a line of text from stdin and returns the equivalent float

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <cs50.h>

Prototype
---------

    float get_float(string prompt, ...);
    

**#include <cs50.h>**

**float get\_float(const char \*format, ...);**

[DESCRIPTION](#description)
===========================

This function prompts the user for a `float`. If the user inputs anything other than a `float` (or a value that cannot fit in a `float`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the equivalent float as precisely as possible; if text does not represent a float or would cause underflow or overflow, user is reprompted.

The prompt is formatted like **printf(3)**.

[RETURN VALUE](#return-value)
=============================

This function returns the user’s input as precisely as possible as a `float`.

Returns the float equivalent to the line read from stdin in \[**FLT\_MIN**, **FLT\_MAX**), as precisely as possible. If line can’t be read, returns **FLT\_MAX**.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        float f = get_float("Input:  ");
        printf("Output: %f\n", f);
    }
    

>     /**
>      * Returns the product of two floats, or FLT_MAX on error.
>      */
>     float multiply_floats(void)
>     {
>         // read float from stdin
>         float f = get_float("Enter a float: ");
>     
>         // make sure we read one successfully
>         if (f == FLT_MAX)
>         {
>             return FLT_MAX;
>         }
>     
>         float g = get_float("What do you want to multiply %f by? ", f);
>     
>         if (g == FLT_MAX)
>         {
>             return FLT_MAX;
>         }
>     
>         return i * j;
>     }

[SEE ALSO](#see-also)
=====================

>     get_char(3), get_double(3), get_int(3), get_long(3),
>     get_string(3)