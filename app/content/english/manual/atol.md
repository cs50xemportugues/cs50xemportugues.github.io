# [NAME](#name)

atol - convert a `string` to a `long`

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdlib.h>

## Prototype

    long atol(string s);

# [DESCRIPTION](#description)

This function converts a (positive or negative) integer from a `string` (e.g., `"50"`) to a `long` (e.g., `50`).

# [RETURN VALUE](#return-value)

This function returns its input, `s`, as a `long`.

# [EXAMPLE](#example)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("This is CS%li\n", atol("50"));
    }
