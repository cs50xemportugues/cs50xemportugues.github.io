# [NAME](#name)

isspace - check whether a character is whitespace (e.g., a newline, space, or tab)

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int isspace(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function checks whether `c` is whitespace (e.g., `\n`, `' '`, or `'\t'`) or not.

# [RETURN VALUE](#return-value)

This function returns a non-zero `int` if `c` is whitespace and `0` if `c` is not whitespace.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input: ");
        if (isspace(c))
        {
            printf("Your input is whitespace.\n");
        }
        else
        {
            printf("Your input is not whitespace.\n");
        }
    }
