# [NAME](#name)

floor - calculate the floor of a number

# [SYNOPSIS](#synopsis)

## Header File

    #include <math.h>

## Prototype

    double floor(double x);

# [DESCRIPTION](#description)

This function returns the floor of `x`.

# [RETURN VALUE](#return-value)

This function returns, as a `double`, the largest integer that is not greater than `x`. You may safely cast that value to a `long` (or an `int` if it fits).

# [EXAMPLE](#example)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("This is CS%i\n", (int) floor(50.1));
    }
