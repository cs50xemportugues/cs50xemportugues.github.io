# [NAME](#name)

strstr - locate a substring

# [SYNOPSIS](#synopsis)

## Header Files

    #include <cs50.h>
    #include <string.h>

## Prototype

    string strstr(string haystack, string needle);

# [DESCRIPTION](#description)

This function searches `haystack` for (the first occurrence of) `needle`. In other words, it determines whether (and where) `needle` is a substring of `haystack`.

# [RETURN VALUE](#return-value)

If `needle` is found in `haystack`, this function returns the substring of `haystack` that begins with `needle`. (For instance, if `haystack` is `"foo bar bar baz"` and `needle` is `"bar"`, this function returns `"bar bar baz"`.) If `needle` is not found in `haystack`, this function returns `NULL`.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <string.h>
    #include <stdio.h>

    int main(void)
    {
        string haystack = "foo bar bar baz";
        string needle = "bar";

        string match = strstr(haystack, needle);
        if (match)
        {
            printf("%s\n", match);
        }
    }
