
Getting Started
---------------

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $
    

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/labs/6/world-cup.zip
    

followed by Enter in order to download a ZIP called `world-cup.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip world-cup.zip
    

to create a folder called `world-cup`. You no longer need the ZIP file, so you can execute

    rm world-cup.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd world-cup
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    world-cup/ $
    

If all was successful, you should execute

    ls
    

and you should see the following files:

    answers.txt  2018m.csv  2019w.csv  tournament.py
    

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

Understanding
-------------

Start by taking a look at the `2018m.csv` file. This file contains the 16 teams in the knockout round of the 2018 Men’s World Cup and the ratings for each team. Notice that the CSV file has two columns, one called `team` (representing the team’s country name) and one called `rating` (representing the team’s rating).

The order in which the teams are listed determines which teams will play each other in each round (in the first round, for example, Uruguay will play Portugal and France will play Argentina; in the next round, the winner of the Uruguay-Portugal match will play the winner of the France-Argentina match). So be sure not to edit the order in which teams appear in this file!

Ultimately, in Python, we can represent each team as a dictionary that contains two values: the team name and the rating. Uruguay, for example, we would want to represent in Python as `{"team": "Uruguay", "rating": 976}`.

Next, take a look at `2019w.csv`, which contains data formatted the same way for the 2019 Women’s World Cup.

Now, open `tournament.py` and see that we’ve already written some code for you. The variable `N` at the top represents how many World Cup simulations to run: in this case, 1000.

The `simulate_game` function accepts two teams as inputs (recall that each team is a dictionary containing the team name and the team’s rating), and simulates a game between them. If the first team wins, the function returns `True`; otherwise, the function returns `False`.

The `simulate_round` function accepts a list of teams (in a variable called `teams`) as input, and simulates games between each pair of teams. The function then returns a list of all of the teams that won the round.

In the `main` function, notice that we first ensure that `len(sys.argv)` (the number of command-line arguments) is 2. We’ll use command-line arguments to tell Python which team CSV file to use to run the tournament simulation. We’ve then defined a list called `teams` (which will eventually be a list of teams) and a dictionary called `counts` (which will associate team names with the number of times that team won a simulated tournament). Right now they’re both empty, so populating them is left up to you!

Finally, at the end of `main`, we sort the teams in descending order of how many times they won simulations (according to `counts`) and print the estimated probability that each team wins the World Cup.

Populating `teams` and `counts` and writing the `simulate_tournament` function are left up to you!
