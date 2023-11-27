#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get user input, make sure it's positive
    int length;
    do
    {
        length = get_int("Size of array: ");
    }
    while (length < 1);

    // Declare our array
    int array[length];

    // Initialize the first value of the array
    array[0] = 1;

    // Print the first value
    printf("%i\n", array[0]);

    // Fill in the rest of the array
    for (int i = 1; i < length; i++)
    {
        // Current value is twice the previous value
        array[i] = array[i - 1] * 2;

        // Print the current value
        printf("%i\n", array[i]);
    }
}