# [NAME](#name)

atoi - convert a `string` to an `int`

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdlib.h>

## Prototype

    int atoi(string s);

# [DESCRIPTION](#description)

This function converts a (positive or negative) integer from a `string` (e.g., `"50"`) to an `int` (e.g., `50`).

# [RETURN VALUE](#return-value)

This function returns its input, `s`, as an `int`.

# [EXAMPLE](#example)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("This is CS%i\n", atoi("50"));
    }
