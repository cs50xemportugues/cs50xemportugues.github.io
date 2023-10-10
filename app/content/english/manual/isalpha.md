# [NAME](#name)

isalpha - check whether a character is alphabetical

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int isalpha(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function checks whether `c` is alphabetical (i.e., a letter) or not.

# [RETURN VALUE](#return-value)

This function returns a non-zero `int` if `c` is alphabetical and `0` if `c` is not alphabetical.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Input: ");
        if (isalpha(c))
        {
            printf("Your input is alphabetical.\n");
        }
        else
        {
            printf("Your input is not alphabetical.\n");
        }
    }
