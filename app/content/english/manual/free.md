# [NAME](#name)

free - free dynamically allocated memory

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdlib.h>

## Prototype

    void free(void *ptr);

Think of `void *` as meaning the address of any type of value in memory.

# [DESCRIPTION](#description)

This function frees memory that has been dynamically allocated with `malloc`. It expects as input the pointer that was returned by [malloc](malloc).

# [RETURN VALUE](#return-value)

This function does not return a value.

# [EXAMPLE](#example)

    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(void)
    {
        char *s = "hello, world\n";
        char *t = malloc(strlen(s) + 1);
        if (t != NULL)
        {
            strcpy(t, s);
            printf("%s\n", t);
            free(t);
        }
    }
