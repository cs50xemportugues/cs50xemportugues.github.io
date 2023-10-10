# [NAME](#name)

islower - check whether a character is lowercase

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int islower(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function checks whether `c` is a lowercase letter (`'a'` through `'z'`) or not. In other words, it checks whether the [ASCII](https://asciichart.com/) value of `c` is between 97 and 122, inclusive.

# [RETURN VALUE](#return-value)

This function returns a non-zero `int` if `c` is a lowercase letter and `0` if `c` is not a lowercase letter.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input: ");
        if (islower(c))
        {
            printf("Your input is a lowercase letter.\n");
        }
        else
        {
            printf("Your input is not a lowercase letter.\n");
        }
    }
