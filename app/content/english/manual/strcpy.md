# [NAME](#name)

strcpy - copy a string

# [SYNOPSIS](#synopsis)

## Header File

    #include <string.h>

## Prototype

    char *strcpy(char *dest, char *src);

# [DESCRIPTION](#description)

This function copies the string at `src`, including its terminating `'\0'`, to the memory at `dest`.

# [RETURN VALUE](#return-value)

This function returns `dest`.

# [EXAMPLE](#example)

    #include <cs50.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(void)
    {
        char *s = get_string("s: ");
        if (s != NULL)
        {
            char *t = malloc(strlen(s) + 1);
            if (t != NULL)
            {
                strcpy(t, s);
                printf("s: %s\n", s);
                printf("t: %s\n", t);
            }
        }
    }
