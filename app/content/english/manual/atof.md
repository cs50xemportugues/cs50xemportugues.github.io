# [NAME](#name)

atof - convert a `string` to a `float`

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdlib.h>

## Prototype

    float atof(string s);

# [DESCRIPTION](#description)

This function converts a (positive or negative) floating-point value from a `string` (e.g., `"50.0"`) to a `float` (e.g., `50.0`).

# [RETURN VALUE](#return-value)

This function returns its input, `s`, as a `float`.

# [EXAMPLE](#example)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("This is CS%.0f\n", atof("50.0"));
    }
