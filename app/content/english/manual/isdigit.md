# [NAME](#name)

isdigit - check whether a character is a digit

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int isdigit(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function checks whether `c` is a decimal digit (`'0'` through `'9'`) or not. In other words, it checks whether the [ASCII](https://asciichart.com/) value of `c` is between 48 and 57, inclusive.

# [RETURN VALUE](#return-value)

This function returns a non-zero `int` if `c` is a decimal digit and `0` if `c` is not a decimal digit.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input: ");
        if (isdigit(c))
        {
            printf("Your input is a digit.\n");
        }
        else
        {
            printf("Your input is not a digit.\n");
        }
    }
