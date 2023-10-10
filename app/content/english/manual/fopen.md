# [NAME](#name)

fopen - open a file

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    FILE *fopen(const char *pathname, const char *mode);

# [DESCRIPTION](#description)

This function opens a file, `pathname`. Supported values for `mode` include

- `"r"`, if opening the file in order to read from it,
- `"w"`, if opening the file in order to write to it, and
- `"a"`, if opening the file in order to append to it.

# [RETURN VALUE](#return-value)

This function returns a pointer to a `FILE` representing the opened file or, in cases of error (as when `pathname` doesn’t exist), `NULL`.

# [EXAMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file != NULL)
        {
            fprintf(file, "This is CS50\n");
            fclose(file);
        }
    }
