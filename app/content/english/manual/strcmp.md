# [NAME](#name)

strcmp - compare two strings

# [SYNOPSIS](#synopsis)

## Header Files

    #include <cs50.h>
    #include <string.h>

## Prototype

    int strcmp(string s1, string s2);

# [DESCRIPTION](#description)

This function compares two strings case-sensitively.

# [RETURN VALUE](#return-value)

This function returns

- an `int` less than `0` if `s1` comes before `s2`,
- `0` if `s1` is the same as `s2`,
- an `int` greater than `0` if `s1` comes after `s2`.

The strings are compared using “ASCIIbetical” order, based on the ASCII values of their characters. For instance, `"AAA"` would come before `"BBB"`, and `"AAA"` would also come before `"aaa"`.

# [EXAMPLES](#examples)

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        string s1 = get_string("s1: ");
        string s2 = get_string("s2: ");
        if (strcmp(s1, s2) == 0)
        {
            printf("Those are the same.\n");
        }
        else
        {
            printf("Those are different.\n");
        }
    }
