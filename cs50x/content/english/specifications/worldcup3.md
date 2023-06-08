
Implementation Details
----------------------

Complete the implementation of `tournament.py`, such that it simulates a number of tournaments and outputs each team’s probability of winning.

First, in `main`, read the team data from the CSV file into your program’s memory, and add each team to the list `teams`.

*   The file to use will be provided as a command-line argument. You can access the name of the file, then, with `sys.argv[1]`.
*   Recall that you can open a file with `open(filename)`, where `filename` is a variable storing the name of the file.
*   Once you have a file `f`, you can use `csv.DictReader(f)` to give you a “reader”: an object in Python that you can loop over to read the file one row at a time, treating each row as a dictionary.
*   By default, all values read from the file will be strings. So be sure to first convert the team’s `rating` to an `int` (you can use the `int` function in Python to do this).
*   Ultimately, append each team’s dictionary to `teams`. The function call `teams.append(x)` will append `x` to the list `teams`.
*   Recall that each team should be a dictionary with a `team` name and a `rating`.

Next, implement the `simulate_tournament` function. This function should accept as input a list of teams and should repeatedly simulate rounds until you’re left with one team. The function should the return the name of that team.

*   You can call the `simulate_round` function, which simulates a single round, accepting a list of teams as input and returning a list of all of the winners.
*   Recall that if `x` is a list, you can use `len(x)` to determine the length of the list.
*   You should not assume the number of teams in the tournament, but you may assume it will be a power of 2.

Finally, back in the `main` function, run `N` tournament simulations, and keep track of how many times each team wins in the `counts` dictionary.

*   For example, if Uruguay won 2 tournaments and Portugal won 3 tournaments, then your `counts` dictionary should be `{"Uruguay": 2, "Portugal": 3}`.
*   You should use your `simulate_tournament` to simulate each tournament and determine the winner.
*   Recall that if `counts` is a dictionary, then syntax like `counts[team_name] = x` will associate the key stored in `team_name` with the value stored in `x`.
*   You can use the `in` keyword in Python to check if a dictionary has a particular key already. For example, `if "Portugal" in counts:` will check to see if `"Portugal"` already has an existing value in the `counts` dictionary.