#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    // Get input from the user
    string word = get_string("Word: ");

    // Determine length of our string
    int length = strlen(word);

    // First, assume everything is alphabetical
    bool alphabetical = true;

    // Look at every character
    for (int i = 1; i < length; i++)
    {
        // If a character is not alphabetical from the one previous
        if (word[i] < word[i - 1])
        {
            alphabetical = false;
        }
    }

    if (alphabetical)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }
}