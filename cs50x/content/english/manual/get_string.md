[NAME](#name)
=============

get\_string - prompt a user for a `string`

get\_string - prompts user for a line of text from stdin and returns it as a string

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <cs50.h>

Prototype
---------

    string get_string(string prompt, ...);
    

**#include <cs50.h>**

**char \*get\_string(const char \*format, ...);**

[DESCRIPTION](#description)
===========================

This function prompts the user for a `string`.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns it as a string (char \*), sans trailing line ending. Supports CR (\\r), LF (\\n), and CRLF (\\r\\n) as line endings. Stores string on heap, but library’s destructor frees memory on program’s exit.

The prompt is formatted like **printf(3)**.

[RETURN VALUE](#return-value)
=============================

This function returns the user’s input as a `string`.

Returns the read line as a string. If user inputs only a line ending, returns "", not NULL. Returns NULL upon error or no input whatsoever (i.e., just EOF).

[EXAMPLE](#example)
===================

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        string s = get_string("Input:  ");
        printf("Output: %s\n", s);
    }
    

>     int main(void)
>     {
>         string s = get_string("Enter string: ");
>     
>         // ensure string was read
>         if (s == NULL)
>         {
>             return 1;
>         }
>     
>         string next = get_string("You just entered %s. Enter a new string: ", s);
>     
>         if (next == NULL)
>         {
>             return 1;
>         }
>     
>         printf("Your last string was %s\n", s);
>     }

[SEE ALSO](#see-also)
=====================

>     get_char(3), get_double(3), get_float(3), get_int(3),
>     get_long(3), printf(3)