# [NAME](#name)

isalnum - check whether a character is alphanumeric

# [SYNOPSIS](#synopsis)

## Header File

    #include <ctype.h>

## Prototype

    int isalnum(char c);

Think of this function as taking a `char` as input.

# [DESCRIPTION](#description)

This function checks whether `c` is alphanumeric (i.e., a letter or a number) or not.

# [RETURN VALUE](#return-value)

This function returns a non-zero `int` if `c` is alphanumeric and `0` if `c` is not alphanumeric.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    int main(void)
    {
        char c = get_char("Input: ");
        if (isalnum(c))
        {
            printf("Your input is alphanumeric.\n");
        }
        else
        {
            printf("Your input is not alphanumeric.\n");
        }
    }
