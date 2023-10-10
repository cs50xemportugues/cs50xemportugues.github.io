# [NAME](#name)

strstr, strcasestr - locate a substring

# [SYNOPSIS](#synopsis)

strcasestr - locate a substring

## Header Files

    #include <cs50.h>

    #define _GNU_SOURCE
    #include <string.h>

## Prototype

    string strcasestr(string haystack, string needle);

Defining `_GNU_SOURCE` in this way enables [strcasestr](strcasestr) within `string.h`.

# [DESCRIPTION](#description)

This function searches `haystack` for (the first occurrence of) `needle` case-insensitively. In other words, it determines whether (and where) `needle` is a substring of `haystack`, ignoring case.

# [RETURN VALUE](#return-value)

If `needle` is found in `haystack`, ignoring case, this function returns the substring of `haystack` that begins with `needle`. (For instance, if `haystack` is `"FOO BAR BAR BAZ"` and `needle` is `"bar"`, this function returns `"BAR BAR BAZ"`.) If `needle` is not found in `haystack`, ignoring case, this function returns `NULL`.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <stdio.h>

    #define _GNU_SOURCE
    #include <string.h>

    int main(void)
    {
        string haystack = "FOO BAR BAR BAZ";
        string needle = "bar";

        string match = strstr(haystack, needle);
        if (match)
        {
            printf("%s\n", match);
        }
    }
