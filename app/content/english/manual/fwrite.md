# [NAME](#name)

fwrite - write bytes to a file

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    size_t fwrite(void *ptr, size_t size, size_t nmemb, FILE *stream);

Think of `void *` as representing the address of the first byte of any type of data. Think of `size_t` as a `long`.

# [DESCRIPTION](#description)

This function writes data to a file that has been opened via [fopen](fopen). It expects as input:

- `ptr`, which is the address (of the first byte) of memory from which to read the data,
- `size`, which is the size (in bytes) of the type of data to write,
- `nmemb`, which is the number of those types to write at once, and
- `stream`, which is the pointer to a `FILE` returned by [fopen](fopen).

For instance, if writing one `char` at a time, `size` would be `sizeof(char)` (i.e., `1`), and `nmemb` would be `1`.

# [RETURN VALUE](#return-value)

This function returns the number of items written, which equals the number of bytes written when `size` is `1`.

If an error occurs, or the end of the file is reached, this function might return a value smaller than `nmemb` or even `0`.

# [EXAMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        FILE *input = fopen("input.txt", "r");
        if (input == NULL)
        {
            return 1;
        }

        FILE *output = fopen("output.txt", "w");
        if (output == NULL)
        {
            fclose(input);
            return 1;
        }

        char c;
        while (fread(&c, sizeof(char), 1, input))
        {
            fwrite(&c, sizeof(char), 1, output);
        }

        fclose(input);
        fclose(output);
    }
