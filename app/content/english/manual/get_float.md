# [NAME](#name)

get_float - prompt a user for a `float`

# [SYNOPSIS](#synopsis)

## Header File

    #include <cs50.h>

## Prototype

    float get_float(string prompt, ...);

# [DESCRIPTION](#description)

This function prompts the user for a `float`. If the user inputs anything other than a `float` (or a value that cannot fit in a `float`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

# [RETURN VALUE](#return-value)

This function returns the user’s input as precisely as possible as a `float`.

# [EXAMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        float f = get_float("Input:  ");
        printf("Output: %f\n", f);
    }

# [SEE ALSO](#see-also)

>     get_char(3), get_double(3), get_int(3), get_long(3),
>     get_string(3)
