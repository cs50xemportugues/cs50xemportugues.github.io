
## Implementation Details

In `cash.c`, we’ve implemented most (but not all!) of a program that prompts the user for the number of cents that a customer is owed and then prints the smallest number of coins with which that change can be made. Indeed, `main` is already implemented for you. But notice how `main` calls several functions that aren’t yet implemented! One of those functions, `get_cents`, takes no arguments (as indicated by `void`) and returns an `int`. The rest of the functions all take one argument, an `int`, and also return an `int`. All of them currently return `0` so that the code will compile. But you’ll want to replace every `TODO` and `return 0;` with your own code. Specifically, complete the implementation of those functions as follows:

- Implement `get_cents` in such a way that the function prompts the user for a number of cents using `get_int` and then returns that number as an `int`. If the user inputs a negative `int`, your code should prompt the user again. (But you don’t need to worry about the user inputting, e.g., a `string`, as `get_int` will take care of that for you.) Odds are you’ll find a `do while` loop of help, as in [`mario.c`](https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight)!
- Implement `calculate_quarters` in such a way that the function calculates (and returns as an `int`) how many quarters a customer should be given if they’re owed some number of cents. For instance, if `cents` is `25`, then `calculate_quarters` should return `1`. If `cents` is `26` or `49` (or anything in between, then `calculate_quarters` should also return `1`. If `cents` is `50` or `74` (or anything in between), then `calculate_quarters` should return `2`. And so forth.
- Implement `calculate_dimes` in such a way that the function calculates the same for dimes.
- Implement `calculate_nickels` in such a way that the function calculates the same for nickels.
- Implement `calculate_pennies` in such a way that the function calculates the same for pennies.

Note that, unlike functions that only have side effects, functions that return a value should do so explicitly with `return`! Take care not to modify the distribution code itself, only replace the given `TODO`s and the subsequent `return` value! Note too that, recalling the idea of abstraction, each of your calculate functions should accept any value of `cents` , not just those values that the greedy algorithm might suggest. If `cents` is 85, for example, `calculate_dimes` should return 8.

<details><summary>Hint</summary><ul>
  <li data-marker="*">Recall that there are several sample programs in Week 1’s <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/">Source Code</a> that illustrate how functions can return a value.</li>
</ul></details>

Your program should behave per the examples below.

```
$ ./cash
Change owed: 41
4
```
```
$ ./cash
Change owed: -41
Change owed: foo
Change owed: 41
4
```

### How to Test Your Code

For this program, try testing your code manually–it’s good practice:

- If you input `-1`, does your program prompts you again?
- If you input `0`, does your program output `0`?
- If you input `1`, does your program output `1` (i.e., one penny)?
- If you input `4`, does your program output `4` (i.e., four pennies)?
- If you input `5`, does your program output `1` (i.e., one nickel)?
- If you input `24`, does your program output `6` (i.e., two dimes and four pennies)?
- If you input `25`, does your program output `1` (i.e., one quarter)?
- If you input `26`, does your program output `2` (i.e., one quarter and one penny)?
- If you input `99`, does your program output `9` (i.e., three quarters, two dimes, and four pennies)?

You can also execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

```
check50 cs50/problems/2023/x/cash
```

<details><summary>Is <code>check50</code> failing to compile your code?</summary><p>Be sure you have only modified those parts of the program marked as <code class="language-plaintext highlighter-rouge">TODO</code>.  If you modify the <code class="language-plaintext highlighter-rouge">main</code> function or add any global variables, for example, your code may <strong>fail to compile</strong>.  <code class="language-plaintext highlighter-rouge">check50</code> will test your five functions independently, beyond just checking for the final answer.</p></details>

And execute the below to evaluate the style of your code using `style50`.

```
style50 cash.c
```

## How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2023/x/cash
```