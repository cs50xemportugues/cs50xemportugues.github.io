# [NAME](#name)

get_string - prompt a user for a `string`

# [SYNOPSIS](#synopsis)

## Header File

    #include <cs50.h>

## Prototype

    string get_string(string prompt, ...);

# [DESCRIPTION](#description)

This function prompts the user for a `string`.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](printf), this function accepts additional arguments as well, one per format code.

# [RETURN VALUE](#return-value)

This function returns the user’s input as a `string`.

# [EXAMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        string s = get_string("Input:  ");
        printf("Output: %s\n", s);
    }

# [SEE ALSO](#see-also)

>     get_char(3), get_double(3), get_float(3), get_int(3),
>     get_long(3), printf(3)
