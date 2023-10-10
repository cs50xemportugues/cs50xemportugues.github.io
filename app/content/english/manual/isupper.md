# [NAME](#name)

isupper - check whether a character is uppercase

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int isupper(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function checks whether `c` is a uppercase letter (`'A'` through `'Z'`) or not. In other words, it checks whether the [ASCII](https://asciichart.com/) value of `c` is between 65 and 90, inclusive.

# [RETURN VALUE](#return-value)

This function returns a non-zero `int` if `c` is an uppercase letter and `0` if `c` is not an uppercase letter.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input: ");
        if (isupper(c))
        {
            printf("Your input is an uppercase letter.\n");
        }
        else
        {
            printf("Your input is not an uppercase letter.\n");
        }
    }
