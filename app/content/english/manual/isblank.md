# [NAME](#name)

isblank - check whether a character is blank (i.e., a space or tab)

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int isblank(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function checks whether `c` is blank (i.e., `' '` or `'\t'`) or not.

# [RETURN VALUE](#return-value)

This function returns a non-zero `int` if `c` is blank and `0` if `c` is not blank.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input: ");
        if (isblank(c))
        {
            printf("Your input is blank.\n");
        }
        else
        {
            printf("Your input is not blank.\n");
        }
    }
