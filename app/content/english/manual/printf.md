# [NAME](#name)

printf - print to the screen

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    int printf(string format, ...);

Note that `...` represents zero or more additional arguments.

# [DESCRIPTION](#description)

This function prints a “formatted string” to the screen. It expects as input a “format string” that specifies what to print and zero or more subsequent arguments. The format string can optionally contain “conversion specifications,” placeholders that begin with `%` that specify how to format the function’s subsequent arguments, if any. For instance, if `c` is a `char`, this function can print it as follows using `%c`:

    printf("%c\n", c);

Alternatively, this function could format that same value as an `int` as well using `%i`, as in an ASCII chart:

    printf("%c %i\n", c, c);

And this function can print strings without any conversion specifications as well:

    printf("hello, world\n");

Among this function’s supported conversion specifications are:

| Conversion Specification | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `string` |

To print an actual percent sign, use `%%`.

To specify the “precision” of a `float` or a `double`, `%f` can optionally contain a `.` after the `%` followed by a number of decimal places. For instance, this function could format the value of one third to one decimal place using `%.1f`:

    printf("%.1f\n", 1.0 / 3.0);

# [RETURN VALUE](#return-value)

This function returns the number of characters printed.

# [EXAMPLES](#examples)

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        string s = "This is CS50";
        printf("%s\n", s);

        int i = 50;
        printf("This is CS%i\n", i);

        float f = 50.0;
        printf("This is CS%.0f\n", f);
    }
