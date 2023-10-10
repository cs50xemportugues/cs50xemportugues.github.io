# [NAME](#name)

realloc - reallocate memory dynamically

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdlib.h>

## Prototype

    void *realloc(void *ptr, size_t size);

Think of `void *` as meaning the address of any type of value in memory. Think of `size_t` as a `long`.

# [DESCRIPTION](#description)

This function dynamically resizes a block of memory that was returned by `malloc`, the address of whose first byte is `ptr`, to be `size` contiguous bytes instead, moving (and copying) the original bytes in memory as needed.

# [RETURN VALUE](#return-value)

This function returns the address of the reallocated block’s first byte (which may or may not be the same as `ptr`) or `NULL` in cases of error (as when insufficient memory is available).

# [EXAMPLE](#example)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *s = malloc(3);
        if (s == NULL)
        {
            return 1;
        }

        s[0] = 'h';
        s[1] = 'i';
        s[2] = '\0';
        printf("%s\n", s);

        char *tmp = realloc(s, 4);
        if (tmp == NULL)
        {
            free(s);
            return 1;
        }
        s = tmp;

        s[2] = '!';
        s[3] = '\0';
        printf("%s\n", s);

        free(s);
        return 0;
    }
