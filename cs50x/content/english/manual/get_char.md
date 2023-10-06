[NAME](#name)
=============

get\_char - prompt a user for a `char`

get\_char - prompts user for a line of text from stdin and returns the equivalent char

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <cs50.h>

Prototype
---------

    char get_char(string prompt, ...);
    

**#include <cs50.h>**

**char get\_char(const char \*format, ...);**

[DESCRIPTION](#description)
===========================

This function prompts the user for a `char`. If the user inputs more or less than one `char`, the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the equivalent char; if text is not a single char, user is reprompted.

The prompt is formatted like **printf(3)**.

[RETURN VALUE](#return-value)
=============================

This function returns the user’s input as a `char`.

Returns char equivalent to the line read from stdin. If line can’t be read, returns **CHAR\_MAX**.

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        char c = get_char("Input:  ");
        printf("Output: %c.\n", c);
    }
    

>     int main(void)
>     {
>         // attempt to read character from stdin
>         char c = get_char("Enter char: ");
>     
>         // ensure character was read successfully
>         if (c == CHAR_MAX)
>         {
>             return 1;
>         }
>     
>         char next = get_char("You just entered %c. Enter another char: ", c);
>     
>         if (next == CHAR_MAX)
>         {
>             return 1;
>         }
>     
>         printf("The last char you entered was %c\n", next);
>     }

[SEE ALSO](#see-also)
=====================

>     get_double(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)