# [NAME](#name)

round - round a number to the nearest integer

# [SYNOPSIS](#synopsis)

## Header File

    #include <math.h>

## Prototype

    double round(double x);

# [DESCRIPTION](#description)

This function rounds `x` to the nearest integer.

# [RETURN VALUE](#return-value)

This function returns, as a `double`, `x` rounded to the nearest integer. You may safely cast that value to a `long` (or an `int` if it fits).

# [EXAMPLE](#example)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("This is CS%i\n", (int) round(49.5));
    }
