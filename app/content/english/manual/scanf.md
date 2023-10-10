# [NAME](#name)

scanf - get input from a user

# [SYNOPSIS](#synopsis)

## Header File

    #include <stdio.h>

## Prototype

    int scanf(const char *format, ...);

Note that `...` represents zero or more additional arguments.

# [DESCRIPTION](#description)

This function “scans” input from a user’s keyboard for values of specified types. It expects as input a “format string” that specifies what to expect and zero or more subsequent arguments, each of which should be a location in memory. The format string should typically contain “conversion specifications,” placeholders that begin with `%` that specify what types of values to expect. Subsequent arguments will be assigned those values. For instance, if `n` is a `int`, this function can get an `int` from a user using `%i`:

    scanf("%i", &n);

Among this function’s supported conversion specifications are:

| Conversion Specification | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |

It is not safe to use this function to get a string from a user using `%s`, as the user’s input might exceed the capacity of the argument that would be assigned that value.

# [RETURN VALUE](#return-value)

This function returns the number of arguments that were assigned values or `EOF`, a constant defined in `stdio.h`, in cases of error.

# [EXAMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        int i;
        printf("Input: ");
        scanf("%i", &i);
        printf("Output: %i\n", i);
    }
