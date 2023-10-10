# [NAME](#name)

get_double - prompt a user for a `double`

# [SYNOPSIS](#synopsis)

## Header File

    #include <cs50.h>

## Prototype

    double get_double(string prompt, ...);

# [DESCRIPTION](#description)

This function prompts the user for a `double`. If the user inputs anything other than a `double` (or a value that cannot fit in a `double`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

# [RETURN VALUE](#return-value)

This function returns the user’s input as precisely as possible as a `double`.

# [EXAMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        double d = get_double("Input:  ");
        printf("Output: %f\n", d);
    }

# [SEE ALSO](#see-also)

>     get_char(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)
