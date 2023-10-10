# [NAME](#name)

random - generate a pseudorandom number

# [SYNOPSIS](#synopsis)

## Header File

    #define _DEFAULT_SOURCE#include <stdlib.h>

## Prototype

    long random(void);

Defining `_DEFAULT_SOURCE` in this way enables `random` within `stdlib.h`.

# [DESCRIPTION](#description)

This function generates a pseudorandom number between `0` and `RAND_MAX`, inclusive, where `RAND_MAX` is a constant defined in `stdlib.h`.

To return a pseudorandom floating-point value between `0.0` and `1.0`, exclusive, instead, it’s common to divide the return value of [random](random) by `(double) RAND_MAX + 1`, as in:

    float number = random() / ((double) RAND_MAX + 1);

To return a pseudorandom integer between `0` and `N`, exclusive, where `N` is some integer, it’s common to divide the return value of [random](random) by `(double) RAND_MAX + 1` and then multiply the quotient by `N`, as in:

    int number = (random() / ((double) RAND_MAX + 1)) * N;

# [RETURN VALUE](#return-value)

This function returns the pseudorandomly generated number as a `long`.

# [EXAMPLE](#example)

    #define _DEFAULT_SOURCE
    #include <stdlib.h>

    #include <stdio.h>
    #include <time.h>

    int main(void)
    {
        srandom(time(NULL));
        printf("%lu\n", random());
        printf("%lu\n", random());
        printf("%lu\n", random());
    }

Calling `time` with an input of `NULL`, a constant defined in `stdlib.h`, returns the current time in seconds.
