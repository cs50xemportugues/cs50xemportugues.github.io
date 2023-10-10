# [NAME](#name)

fread - read bytes from a file

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);

Think of `void *` as representing the address of the first byte of any type of data. Think of `size_t` as a `long`.

# [DESCRIPTION](#description)

This function reads data from a file that has been opened via [fopen](fopen). It expects as input:

- `ptr`, which is the address (of the first byte) of memory into which to read the data,
- `size`, which is the size (in bytes) of the type of data to read,
- `nmemb`, which is the number of those types to read at once, and
- `stream`, which is the pointer to a `FILE` returned by [fopen](fopen).

For instance, if reading one `char` at a time, `size` would be `sizeof(char)` (i.e., `1`), and `nmemb` would be `1`.

# [RETURN VALUE](#return-value)

This function returns the number of items read, which equals the number of bytes read when `size` is `1`.

If an error occurs, or the end of the file is reached, this function might return a value smaller than `nmemb` or even `0`.

The opened file “remembers” the number of bytes that were successfully read, such that subsequent calls to this function for `stream` will return bytes after those already read.

# [EXAMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "r");
        if (file != NULL)
        {
            char c;
            while (fread(&c, sizeof(char), 1, file))
            {
                printf("%c", c);
            }
            fclose(file);
        }
    }
