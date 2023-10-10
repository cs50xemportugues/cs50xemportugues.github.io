# [NAME](#name)

strlen - calculate the length of a string

# [SYNOPSIS](#synopsis)

strlen - calculate the length of a string

## Header Files

    #include <cs50.h>
    #include <string.h>

## Prototype

    int strlen(string s);

# [DESCRIPTION](#description)

This function calculates the length of `s`.

# [RETURN VALUE](#return-value)

This function returns the number of characters in `s`, excluding the terminating NUL byte (i.e., `'\0'`).

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        string s = get_string("Input:  ");
        printf("Output: ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            printf("%c", s[i]);
        }
        printf("\n");
    }
