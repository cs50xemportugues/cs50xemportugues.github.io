Lab 6: World Cup
================

<div class="alert" data-alert="warning" role="alert"><p>You are welcome to collaborate with one or two classmates on this lab, though it is expected that every student in any such group contribute equally to the lab.</p></div>

Write a program to run simulations of the FIFA World Cup.

    $ python tournament.py 2018m.csv
    Belgium: 20.9% chance of winning
    Brazil: 20.3% chance of winning
    Portugal: 14.5% chance of winning
    Spain: 13.6% chance of winning
    Switzerland: 10.5% chance of winning
    Argentina: 6.5% chance of winning
    England: 3.7% chance of winning
    France: 3.3% chance of winning
    Denmark: 2.2% chance of winning
    Croatia: 2.0% chance of winning
    Colombia: 1.8% chance of winning
    Sweden: 0.5% chance of winning
    Uruguay: 0.1% chance of winning
    Mexico: 0.1% chance of winning
    

Background
----------

In soccer’s World Cup, the knockout round consists of 16 teams. In each round, each team plays another team and the losing teams are eliminated. When only two teams remain, the winner of the final match is the champion.

In soccer, teams are given [FIFA Ratings](https://en.wikipedia.org/wiki/FIFA_World_Rankings#Current_calculation_method), which are numerical values representing each team’s relative skill level. Higher FIFA ratings indicate better previous game results, and given two teams’ FIFA ratings, it’s possible to estimate the probability that either team wins a game based on their current ratings. The FIFA Ratings from two previous World Cups are available as the [May 2018 Men’s FIFA Ratings](https://www.fifa.com/fifa-world-ranking/ranking-table/men/rank/id12189/) and [March 2019 Women’s FIFA Ratings](https://www.fifa.com/fifa-world-ranking/ranking-table/women/rank/ranking_20190329/).

Using this information, we can simulate the entire tournament by repeatedly simulating rounds until we’re left with just one team. And if we want to estimate how likely it is that any given team wins the tournament, we might simulate the tournament many times (e.g. 1000 simulations) and count how many times each team wins a simulated tournament. 1000 simulations might seem like many, but with today’s computing power we can accomplish those simulations in a matter of milliseconds. At the end of this lab, we’ll experiment with how worthwhile it might be to increase the number of simulations we run, given the trade-off of runtime.

Your task in this lab is to do just that using Python!
