# [NAME](#name)

malloc - allocate memory dynamically

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdlib.h>

## Prototype

    void *malloc(size_t size);

Think of `void *` as meaning the address of any type of value in memory. Think of `size_t` as a `long`.

# [DESCRIPTION](#description)

This function dynamically allocates `size` contiguous bytes of memory (on the heap) that can be used to store any type of values.

# [RETURN VALUE](#return-value)

This function returns the address of the first byte of memory allocated or `NULL` in cases of error (as when insufficient memory is available).

# [EXAMPLE](#example)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *s = malloc(4);
        if (s == NULL)
        {
            return 1;
        }

        s[0] = 'h';
        s[1] = 'i';
        s[2] = '!';
        s[3] = '\0';
        printf("%s\n", s);

        free(s);
        return 0;
    }
