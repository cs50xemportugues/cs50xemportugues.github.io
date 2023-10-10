# [NAME](#name)

ceil - calculate the ceiling of a number

# [SYNOPSIS](#synopsis)

## Header File

    #include <math.h>

## Prototype

    double ceil(double x);

# [DESCRIPTION](#description)

This function returns the ceiling of `x`.

# [RETURN VALUE](#return-value)

This function returns, as a `double`, the smallest integer that is not less than `x`. You may safely cast that value to a `long` (or an `int` if it fits).

# [EXAMPLE](#example)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("This is CS%i\n", (int) ceil(49.9));
    }
