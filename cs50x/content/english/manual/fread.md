[NAME](#name)
=============

fread - read bytes from a file

fread, fwrite - binary stream input/output

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <stdio.h>

Prototype
---------

    size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
    

Think of `void *` as representing the address of the first byte of any type of data. Think of `size_t` as a `long`.

    #include <stdio.h>
    
    size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
    
    size_t fwrite(const void *ptr, size_t size, size_t nmemb,
     FILE *stream);

[DESCRIPTION](#description)
===========================

This function reads data from a file that has been opened via [fopen](fopen). It expects as input:

*   `ptr`, which is the address (of the first byte) of memory into which to read the data,
*   `size`, which is the size (in bytes) of the type of data to read,
*   `nmemb`, which is the number of those types to read at once, and
*   `stream`, which is the pointer to a `FILE` returned by [fopen](fopen).

For instance, if reading one `char` at a time, `size` would be `sizeof(char)` (i.e., `1`), and `nmemb` would be `1`.

The function [fread](fread)() reads `nmemb` items of data, each `size` bytes long, from the stream pointed to by `stream`, storing them at the location given by `ptr`.

The function [fwrite](fwrite)() writes `nmemb` items of data, each `size` bytes long, to the stream pointed to by `stream`, obtaining them from the location given by `ptr`.

For nonlocking counterparts, see [unlocked\_stdio](/3/unlocked_stdio)(3).

[RETURN VALUE](#return-value)
=============================

This function returns the number of items read, which equals the number of bytes read when `size` is `1`.

If an error occurs, or the end of the file is reached, this function might return a value smaller than `nmemb` or even `0`.

The opened file “remembers” the number of bytes that were successfully read, such that subsequent calls to this function for `stream` will return bytes after those already read.

On success, [fread](fread)() and [fwrite](fwrite)() return the number of items read or written. This number equals the number of bytes transferred only when `size` is 1. If an error occurs, or the end of the file is reached, the return value is a short item count (or zero).

The file position indicator for the stream is advanced by the number of bytes successfully read or written.

[fread](fread)() does not distinguish between end-of-file and error, and callers must use [feof](/3/feof)(3) and [ferror](/3/ferror)(3) to determine which occurred.

[EXAMPLES](#examples)
=====================

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
    

The program below demonstrates the use of [fread](fread)() by parsing /bin/sh ELF executable in binary mode and printing its magic and class:

    $ ./a.out
    ELF magic: 0x7f454c46
    Class: 0x02

Program source
--------------

    #include <stdio.h>
    #include <stdlib.h>
    
    #define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))
    
    int
    main(void)
    {
        FILE *fp = fopen("/bin/sh", "rb");
        if (!fp) {
            perror("fopen");
            return EXIT_FAILURE;
        }
    
        unsigned char buffer[4];
    
        size_t ret = fread(buffer, ARRAY_SIZE(buffer), sizeof(*buffer), fp);
        if (ret != sizeof(*buffer)) {
            fprintf(stderr, "fread() failed: %zu\n", ret);
            exit(EXIT_FAILURE);
        }
    
        printf("ELF magic: %#04x%02x%02x%02x\n", buffer[0], buffer[1],
               buffer[2], buffer[3]);
    
        ret = fread(buffer, 1, 1, fp);
        if (ret != 1) {
            fprintf(stderr, "fread() failed: %zu\n", ret);
            exit(EXIT_FAILURE);
        }
    
        printf("Class: %#04x\n", buffer[0]);
    
        fclose(fp);
    
        exit(EXIT_SUCCESS);
    }

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[fread](fread)(), [fwrite](fwrite)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

POSIX.1-2001, POSIX.1-2008, C89.

[SEE ALSO](#see-also)
=====================

[read](/2/read)(2), [write](/2/write)(2), [feof](/3/feof)(3), [ferror](/3/ferror)(3), [unlocked\_stdio](/3/unlocked_stdio)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).