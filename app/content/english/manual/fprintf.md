# [NAME](#name)

fprintf - print to a file

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    int fprintf(FILE *stream, const char *format, ...);

Note that `...` represents zero or more additional arguments.

# [DESCRIPTION](#description)

This function prints a “formatted string” to a file. It expects as input the pointer to a `FILE` that was returned by [fopen](fopen), a “format string” that specifies what to print, and zero or more subsequent arguments. The format string can optionally contain “conversion specifications,” placeholders that begin with `%` that specify how to format the function’s subsequent arguments, if any. For instance, if `file` is a pointer to a `FILE` and `c` is a `char`, this function can print the latter to the former as follows using `%c`:

    fprintf(file, "%c\n", c);

Alternatively, this function could format that same value as an `int` as well using `%i`, as in an ASCII chart:

    fprintf(file, "%c %i\n", c, c);

And this function can print strings without any conversion specifications as well:

    fprintf(file, "hello, world\n");

Among this function’s supported conversion specifications are:

| Conversion Specification | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `char *` |

To print actual percent sign, use `%%`.

To specify the “precision” of a `float` or a `double`, `%f` can optionally contain a `.` after the `%` followed by a number of decimal places. For instance, this function could format the value of one third to one decimal place using `%.1f`:

    fprintf(file, "%.1f\n", 1.0 / 3.0);

# [RETURN VALUE](#return-value)

This function returns the number of characters printed.

# [EXAMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file == NULL)
        {
            return 0;
        }

        char *s = "This is CS50";
        fprintf(file, "%s\n", s);

        int i = 50;
        fprintf(file, "This is CS%i\n", i);

        float f = 50.0;
        fprintf(file, "This is CS%.0f\n", f);

        fclose(file);
        return 0;
    }
