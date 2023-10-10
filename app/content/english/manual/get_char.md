# [NAME](#name)

get_char - prompt a user for a `char`

# [SYNOPSIS](#synopsis)

## Header File

    #include <cs50.h>

## Prototype

    char get_char(string prompt, ...);

# [DESCRIPTION](#description)

This function prompts the user for a `char`. If the user inputs more or less than one `char`, the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

# [RETURN VALUE](#return-value)

This function returns the user’s input as a `char`.

# [EXAMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        char c = get_char("Input:  ");
        printf("Output: %c.\n", c);
    }

# [SEE ALSO](#see-also)

>     get_double(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)
