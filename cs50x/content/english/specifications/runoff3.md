
Specification
-------------

Complete the implementation of `runoff.c` in such a way that it simulates a runoff election. You should complete the implementations of the `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie`, and `eliminate` functions, and you should not modify anything else in `runoff.c` (and the inclusion of additional header files, if you’d like).

### `vote`

Complete the `vote` function.

*   The function takes arguments `voter`, `rank`, and `name`. If `name` is a match for the name of a valid candidate, then you should update the global preferences array to indicate that the voter `voter` has that candidate as their `rank` preference (where `0` is the first preference, `1` is the second preference, etc.).
*   If the preference is successfully recorded, the function should return `true`; the function should return `false` otherwise (if, for instance, `name` is not the name of one of the candidates).
*   You may assume that no two candidates will have the same name.


<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">candidate_count</code> stores the number of candidates in the election.</li>
  <li data-marker="*">Recall that you can use <a href="https://man.cs50.io/3/strcmp"><code class="language-plaintext highlighter-rouge">strcmp</code></a> to compare two strings.</li>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">preferences[i][j]</code> stores the index of the candidate who is the <code class="language-plaintext highlighter-rouge">j</code>th ranked preference for the <code class="language-plaintext highlighter-rouge">i</code>th voter.</li>
</ul></details>

### `tabulate`

Complete the `tabulate` function.

*   The function should update the number of `votes` each candidate has at this stage in the runoff.
*   Recall that at each stage in the runoff, every voter effectively votes for their top-preferred candidate who has not already been eliminated.

<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">voter_count</code> stores the number of voters in the election and that, for each voter in our election, we want to count one ballot.</li>
  <li data-marker="*">Recall that for a voter <code class="language-plaintext highlighter-rouge">i</code>, their top choice candidate is represented by <code class="language-plaintext highlighter-rouge">preferences[i][0]</code>, their second choice candidate by <code class="language-plaintext highlighter-rouge">preferences[i][1]</code>, etc.</li>
  <li data-marker="*">Recall that the <code class="language-plaintext highlighter-rouge">candidate</code> <code class="language-plaintext highlighter-rouge">struct</code> has a field called <code class="language-plaintext highlighter-rouge">eliminated</code>, which will be <code class="language-plaintext highlighter-rouge">true</code> if the candidate has been eliminated from the election.</li>
  <li data-marker="*">Recall that the <code class="language-plaintext highlighter-rouge">candidate</code> <code class="language-plaintext highlighter-rouge">struct</code> has a field called <code class="language-plaintext highlighter-rouge">votes</code>, which you’ll likely want to update for each voter’s preferred candidate.</li>
  <li data-marker="*">Once you’ve cast a vote for a voter’s first non-eliminated candidate, you’ll want to stop there, not continue down their ballot! Recall that you can break out of a loop early using <code class="language-plaintext highlighter-rouge">break</code> inside of a conditional.</li>
</ul></details>

### `print_winner`

Complete the `print_winner` function.

*   If any candidate has more than half of the vote, their name should be printed and the function should return `true`.
*   If nobody has won the election yet, the function should return `false`.

<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">voter_count</code> stores the number of voters in the election. Given that, how would you express the number of votes needed to win the election?</li>
</ul></details>

### `find_min`

Complete the `find_min` function.

*   The function should return the minimum vote total for any candidate who is still in the election.

<details><summary>Hints</summary><ul>
  <li data-marker="*">You’ll likely want to loop through the candidates to find the one who is both still in the election and has the fewest number of votes. What information should you keep track of as you loop through the candidates?</li>
</ul></details>

### `is_tie`

Complete the `is_tie` function.

*   The function takes an argument `min`, which will be the minimum number of votes that anyone in the election currently has.
*   The function should return `true` if every candidate remaining in the election has the same number of votes, and should return `false` otherwise.

<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that a tie happens if every candidate still in the election has the same number of votes. Note, too, that the <code class="language-plaintext highlighter-rouge">is_tie</code> function takes an argument <code class="language-plaintext highlighter-rouge">min</code>, which is the smallest number of votes any candidate currently has. How might you use that information to determine if the election is a tie (or, conversely, not a tie)?</li>
</ul></details>

### `eliminate`

Complete the `eliminate` function.

*   The function takes an argument `min`, which will be the minimum number of votes that anyone in the election currently has.
*   The function should eliminate the candidate (or candidates) who have `min` number of votes.
