# [NAME](#name)

get_int - prompt a user for an `int`

# [SYNOPSIS](#synopsis)

## Header File

    #include <cs50.h>

## Prototype

    int get_int(string prompt, ...);

# [DESCRIPTION](#description)

This function prompts the user for an `int`. If the user inputs anything other than an `int` (or a value that cannot fit in an `int`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

# [RETURN VALUE](#return-value)

This function returns the user’s input as a `int`.

# [EXAMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        int i = get_int("Input:  ");
        printf("Output: %i\n", i);
    }

# [SEE ALSO](#see-also)

>     get_char(3), get_double(3), get_float(3), get_long(3),
>     get_string(3), printf(3)
