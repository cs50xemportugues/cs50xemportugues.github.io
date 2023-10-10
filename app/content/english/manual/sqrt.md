# [NAME](#name)

sqrt - calculate the square root of a number

# [SYNOPSIS](#synopsis)

## Header File

    #include <math.h>

## Prototype

    double sqrt(double x);

# [DESCRIPTION](#description)

This function calculates the square root of `x`.

# [RETURN VALUE](#return-value)

This function returns, as a `double`, the square root of `x`.

# [EXAMPLE](#example)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("This is CS%i\n", (int) sqrt(2500));
    }
