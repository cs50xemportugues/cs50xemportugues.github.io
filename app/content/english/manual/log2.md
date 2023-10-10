# [NAME](#name)

log2 - calculate the base-2 logarithm of a number

# [SYNOPSIS](#synopsis)

## Header File

    #include <math.h>

## Prototype

    double log2(double x);

# [DESCRIPTION](#description)

This function calculates the base-2 logarithm of `x`.

# [RETURN VALUE](#return-value)

This function returns, as a `double`, the base-2 logarithm of `x`.

# [EXAMPLE](#example)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("This is CS%i\n", (int) log2(1125899906842624));
    }
