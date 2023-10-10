# [NAME](#name)

strcasecmp - compare two strings ignoring case

# [SYNOPSIS](#synopsis)

## Header Files

    #include <cs50.h>#include <strings.h>

## Prototype

    int strcasecmp(string s1, string s2);

# [DESCRIPTION](#description)

This function compares two strings case-insensitively.

# [RETURN VALUE](#return-value)

This function returns

- an `int` less than `0` if `s1` comes before `s2`, ignoring case,
- `0` if `s1` is the same as `s2`, ignoring case, or
- an `int` greater than `0` if `s1` comes after `s2`, ignoring case.

The strings are compared using “ASCIIbetical” order, based on the ASCII values of their characters. For instance, `"AAA"` would come before `"BBB"`.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <stdio.h>
    #include <strings.h>

    int main(void)
    {
        string s1 = get_string("s1: ");
        string s2 = get_string("s2: ");
        if (strcasecmp(s1, s2) == 0)
        {
            printf("Those are the same, ignoring case.\n");
        }
        else
        {
            printf("Those are different, even ignoring case.\n");
        }
    }
