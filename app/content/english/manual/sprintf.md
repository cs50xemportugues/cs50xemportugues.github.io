# [NAME](#name)

sprintf - print to a string

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    int sprintf(char *str, const char *format, ...);

Note that `...` represents zero or more additional arguments.

# [DESCRIPTION](#description)

This function prints a “formatted string” to a location in memory. It expects as input the address of a buffer (which must be large enough to fit the string, including its `\0`), a “format string” that specifies what to print, and zero or more subsequent arguments. The format string can optionally contain “conversion specifications,” placeholders that begin with `%` that specify how to format the function’s subsequent arguments, if any. For instance, if `buffer` is an array of (at least) 13 bytes and `i` is `50`, this function could format a string as follows:

    sprintf(buffer, "hello, %s\n", i);

Among this function’s supported conversion specifications are:

| Conversion Specification | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `char *` |

To print an actual percent sign, use `%%`.

To specify the “precision” of a `float` or a `double`, `%f` can optionally contain a `.` after the `%` followed by a number of decimal places. For instance, this function could format the value of one third to one decimal place using `%.1f`, assuming `buffer` is an array of size 4 (at least):

    sprintf(buffer, "%.1f\n", 1.0 / 3.0);

# [RETURN VALUE](#return-value)

This function returns the number of characters printed.

# [EXAMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        char buffer[13];

        int i = 50;
        sprintf(buffer, "This is CS%i", i);
        printf("%s\n", buffer);

        float f = 50.0;
        sprintf(buffer, "This is CS%.0f", f);
        printf("%s\n", buffer);
    }
