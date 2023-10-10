# [NAME](#name)

toupper - convert a `char` to uppercase

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int toupper(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function converts `c` to uppercase.

# [RETURN VALUE](#return-value)

If `c` is a lowercase letter (`a` through `z`), this function returns its uppercase equivalent (`A` through `Z`). If `c` is not a lowercase letter, this function returns `c` itself.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input:  ");
        printf("Output: %c\n", toupper(c));
    }
