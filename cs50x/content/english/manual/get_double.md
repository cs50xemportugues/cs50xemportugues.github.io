[NAME](#name)
=============

get\_double - prompt a user for a `double`

get\_double - prompts user for a line of text from stdin and returns the equivalent double

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <cs50.h>

Prototype
---------

    double get_double(string prompt, ...);
    

**#include <cs50.h>**

**double get\_double(const char \*format, ...);**

[DESCRIPTION](#description)
===========================

This function prompts the user for a `double`. If the user inputs anything other than a `double` (or a value that cannot fit in a `double`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the equivalent double as precisely as possible; if text does not represent a double or would cause underflow or overflow, user is reprompted.

The prompt is formatted like **printf(3)**.

[RETURN VALUE](#return-value)
=============================

This function returns the user’s input as precisely as possible as a `double`.

Returns the double equivalent to the line read from stdin in \[**DBL\_MIN**, **DBL\_MAX**), as precisely as possible. If line can’t be read, returns **DBL\_MAX**.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        double d = get_double("Input:  ");
        printf("Output: %f\n", d);
    }
    

>     /**
>      * Returns the quotient of two doubles, or DBL_MAX on error.
>      */
>     double divide_doubles(void)
>     {
>         // read double from stdin
>         double d = get_double("Enter a double: ");
>     
>         // make sure we read one successfully
>         if (d == DBL_MAX)
>         {
>             return DBL_MAX;
>         }
>     
>         double e = get_double("What do you want to divide %lf by? ", d);
>     
>         // make sure we don't divide by zero
>         if (e == DBL_MAX || e == 0.0)
>         {
>             return DBL_MAX;
>         }
>     
>         return i / j;
>     }

[SEE ALSO](#see-also)
=====================

>     get_char(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)