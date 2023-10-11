# [NAME](#name)

srandom - seed pseudorandom number generation

# [SYNOPSIS](#synopsis)

## Header File

    #define _DEFAULT_SOURCE
    #include <stdlib.h>

## Prototype

    void srandom(unsigned int seed);

An `unsigned int` must be non-negative.

Defining `_DEFAULT_SOURCE` in this way enables [srandom](srandom) within `stdlib.h`.

# [DESCRIPTION](#description)

This function alters the sequence of pseudorandom numbers generated by [random](random). It should be called (once) before making any calls to [random](random). In other words, if you first call [srandom](srandom) with a `seed` of `1`, subsequent calls to [random](random) will return different values than if you first call [srandom](srandom) with a `seed` of `2`.

Rather than hardcode a value for `seed`, it is common to pass the return value of [time](/2/time) (which changes every second) to [srandom](srandom).

# [RETURN VALUE](#return-value)

This function does not return a value.

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