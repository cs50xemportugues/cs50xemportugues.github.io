#include <cs50.h>
#include <stdio.h>

// Define a new struct called "candidate"
typedef struct
{
    string name;
    int votes;
}
candidate;

candidate get_candidate(string prompt);

int main(void)
{
    // Prompt user for a candidate
    candidate president = get_candidate("Enter a president: ");
}

candidate get_candidate(string prompt)
{
    // Print prompt
    printf("%s\n", prompt);

    // Declare a new candidate
    candidate c;

    // Initialize the candidate's attributes
    c.name = get_string("Enter a name: ");
    c.votes = get_int("Enter a number of votes: ");

    // Return the new candidate
    return c;
}