[NAME](#name)
=============

fclose - close a file

fclose - close a stream

[SYNOPSIS](#synopsis)
=====================

Header File
-----------

    #include <stdio.h>

Prototype
---------

    int fclose(FILE *stream);
    

**#include <stdio.h>**

**int fclose(FILE \***`stream`**);**

[DESCRIPTION](#description)
===========================

This function closes a file that has been opened via [fopen](fopen). It expects as input the pointer to a `FILE` that was returned by [fopen](fopen).

The [fclose](fclose)() function flushes the stream pointed to by `stream` (writing any buffered output data using [fflush](/3/fflush)(3)) and closes the underlying file descriptor.

The behaviour of [fclose](fclose)() is undefined if the `stream` parameter is an illegal pointer, or is a descriptor already passed to a previous invocation of [fclose](fclose)().

[RETURN VALUE](#return-value)
=============================

This function returns `0` if successful and `EOF`, a constant, in cases of error.

Upon successful completion, 0 is returned. Otherwise, **EOF** is returned and `errno` is set to indicate the error. In either case, any further access (including another call to [fclose](fclose)()) to the stream results in undefined behavior.

[EXAMPLE](#example)
===================

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
    

[ERRORS](#errors)
=================

**EBADF**

The file descriptor underlying `stream` is not valid.

The [fclose](fclose)() function may also fail and set `errno` for any of the errors specified for the routines [close](/2/close)(2), [write](/2/write)(2), or [fflush](/3/fflush)(3).

[ATTRIBUTES](#attributes)
=========================

For an explanation of the terms used in this section, see [attributes](/7/attributes)(7).

Interface

Attribute

Value

[fclose](fclose)()

Thread safety

MT-Safe

[CONFORMING TO](#conforming-to)
===============================

POSIX.1-2001, POSIX.1-2008, C89, C99.

[NOTES](#notes)
===============

Note that [fclose](fclose)() flushes only the user-space buffers provided by the C library. To ensure that the data is physically stored on disk the kernel buffers must be flushed too, for example, with [sync](/2/sync)(2) or [fsync](/2/fsync)(2).

[SEE ALSO](#see-also)
=====================

[close](/2/close)(2), [fcloseall](/3/fcloseall)(3), [fflush](/3/fflush)(3), [fileno](/3/fileno)(3), [fopen](/3/fopen)(3), [setbuf](/3/setbuf)(3)

[COLOPHON](#colophon)
=====================

This page is part of release 5.10 of the Linux `man-pages` project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/).