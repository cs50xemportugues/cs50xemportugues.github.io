# [NAME](#name)

time - get time in seconds

# [SYNOPSIS](#synopsis)

## Header File

    #include <time.h>

## Prototype

    long time(NULL);

Think of this function as returning a `long` as output and as taking only `NULL` as input.

# [DESCRIPTION](#description)

This function gets the current date and time as seconds since January 1, 1970, 00:00:00 UTC, otherwise known as the Epoch.

# [RETURN VALUE](#return-value)

This function returns the number of seconds since January 1, 1970, 00:00:00 UTC.

# [EXAMPLE](#example)

    #include <stdio.h>
    #include <time.h>

    int main(void)
    {
        printf("The time is now %li.\n", time(NULL));
    }
