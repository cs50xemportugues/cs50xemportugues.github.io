# [NAME](#name)

pow - raise a number to a power

# [SYNOPSIS](#synopsis)

## Header File

    #include <math.h>

## Prototype

    double pow(double x, double y);

# [DESCRIPTION](#description)

This function raises `x` to the power of `y`.

# [RETURN VALUE](#return-value)

This function returns, as a `double`, `x` raised to the power of `y`.

# [EXAMPLE](#example)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("A 32-bit integer can store %li possible values.\n", (long) pow(2, 32));
    }
