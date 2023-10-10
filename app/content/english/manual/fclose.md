# [NAME](#name)

fclose - close a file

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    int fclose(FILE *stream);

# [DESCRIPTION](#description)

This function closes a file that has been opened via [fopen](fopen). It expects as input the pointer to a `FILE` that was returned by [fopen](fopen).

# [RETURN VALUE](#return-value)

This function returns `0` if successful and `EOF`, a constant, in cases of error.

# [EXAMPLE](#example)

    #inclue <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file != NULL)
        {
            fprintf(file, "This is CS50\n");
            fclose(file);
        }
    }
