# [NAME](#name)

ispunct - check whether a character is punctuation

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int ispunct(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function checks whether `c` is a punctuation mark (e.g., `'.'`, or `','`, or `'!'` etc.) or not.

# [RETURN VALUE](#return-value)

This function returns a non-zero `int` if `c` is punctuation and `0` if `c` is not punctuation.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input: ");
        if (ispunct(c))
        {
            printf("Your input is punctuation.\n");
        }
        else
        {
            printf("Your input is not punctuation.\n");
        }
    }
