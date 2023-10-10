# [NAME](#name)

fscanf - get input from a file

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    int fscanf(FILE *stream, const char *format, ...);

Note that `...` represents zero or more additional arguments.

# [DESCRIPTION](#description)

This function “scans” a file for values of specified types. It expects as input the pointer to a `FILE` that was returned by [fopen](fopen), a “format string” that specifies what to expect, and zero or more subsequent arguments, each of which should be a location in memory. The format string should typically contain “conversion specifications,” placeholders that begin with `%` that specify what types of values to expect. Subsequent arguments will be assigned those values. For instance, if `n` is a `int`, this function can get an `int` from a user using `%i`:

    scanf("%i", &n);

Among this function’s supported conversion specifications are:

| Conversion Specification | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |

To get a single word (i.e., a sequence of non-whitespace characters), use `%s`. But it is only safe to use this function to get a word from a file using `%s` if that word is of some maximal length. For instance, if `file` is a pointer to a `FILE` that was returned by [fopen](fopen) and `buffer` is an array of 3 bytes, this function could be user to get `"hi"`, including its `'\0'`, but not `"hi!"`, as follows:

    fscanf(file, "%s", buffer);

# [RETURN VALUE](#return-value)

This function returns the number of arguments that were assigned values or `EOF`, a constant defined in `stdio.h`, if the end of the file has been reached.

# [EXAMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("hi.txt", "r");
        if (file != NULL)
        {
            char buffer[3];
            fscanf(file, "%s", buffer);
            fclose(file);
            printf("%s\n", buffer);
        }
    }
