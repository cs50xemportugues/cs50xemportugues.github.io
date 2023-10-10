# [NAME](#name)

tolower - convert a `char` to lowercase

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int tolower(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function converts `c` to lowercase.

# [RETURN VALUE](#return-value)

If `c` is an uppercase letter (`A` through `Z`), this function returns its lowercase equivalent (`a` through `z`). If `c` is not an uppercase letter, this function returns `c` itself.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input:  ");
        printf("Output: %c\n", tolower(c));
    }
