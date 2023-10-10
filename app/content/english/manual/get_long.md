# [NAME](#name)

get_long - prompt a user for an `long`

# [SYNOPSIS](#synopsis)

## Header File

    #include <cs50.h>

## Prototype

    long get_long(string prompt, ...);

# [DESCRIPTION](#description)

This function prompts the user for a `long`. If the user inputs anything other than an `long` (or a value that cannot fit in an `long`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

# [RETURN VALUE](#return-value)

This function returns the user’s input as a `long`.

# [EXAMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        long l = get_long("Input:  ");
        printf("Output: %li\n", l);
    }

# [SEE ALSO](#see-also)

>     get_char(3), get_double(3), get_float(3), get_int(3), get_string(3),
>     printf(3)
