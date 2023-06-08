
Implementation Details
----------------------

To write our program, we’ll first need to think about **bases**.

### The Basics

The simplest _base_ is base-1, or _unary_; to write a number, _N_, in base-1, we would simply write _N_ consecutive `1`s. So the number `4` in base-1 would be written as `1111`, and the number `12` as `111111111111`. Think of it like counting on your fingers or tallying up a score with marks on a board.

You might see why base-1 isn’t used much nowadays. (The numbers get rather long!) Instead, a common convention is base-10, or _decimal_. In base-10, each _digit_ is multiplied by some power of 10, in order to represent larger numbers. For instance, `123` is short for <code>123 = 1 • 10<sup>2</sup> + 2 • 10<sup>1</sup> + 3 • 10<sup>0</sup></code>.

Changing base is as simple as changing the `10` above to a different number. For instance, if you wrote `123` in base-4, the number you’d really be writing is <code>123 = 1 • 4<sup>2</sup> + 2 • 4<sup>1</sup> + 3 • 4<sup>0</sup></code>, which is equal to the decimal number `27`.

Computers, though, use base-2, or _binary_. In binary, writing `123` would be a mistake, since binary numbers can only have `0`s and `1`s. But the process of figuring out exactly what decimal number a binary number stands for is exactly the same. For instance, the number `10101` in base-2 represents <code>1 • 2<sup>4</sup> + 0 • 2<sup>3</sup> + 1 • 2<sup>2</sup> + 0 • 2<sup>1</sup> + 1 • 2<sup>0</sup></code>, which is equal to the decimal number `21`.

### Encoding a Message

Light bulbs can only be on or off. In other words, light bulbs represent two possible states; either the bulb is on, or the bulb is off, just as binary numbers are either 1 or 0. We’ll have to find a way to encode text as a sequence of binary numbers.

Let’s write a program called `bulbs` that takes a message and converts it to a set of bulbs that we could show to an unsuspecting audience. We’ll do it in two steps:

*   The first step consists of turning the text into decimal numbers. Let’s say we want to encode the message `HI!`. Luckily, we already have a convention in place for how to do this, [ASCII](https://asciichart.com/). Notice that `H` is represented by the decimal number `72`, `I` is represented by `73`, and `!` is represented by `33`.
*   The next step involves taking our decimal numbers (like `72`, `73`, and `33`) and converting them into equivalent binary numbers, which only use 0s and 1s. For the sake of having a consistent number of bits in each of our binary numbers, assume that each decimal is represented with 8 bits. `72` is `01001000`, `73` is `01001001`, and `33` is `00100001`.

Lastly, we’ll interpret these binary numbers as instructions for the light bulbs on stage; 0 is off, 1 is on. (You’ll find that `bulbs.c` includes a `print_bulb` function that’s been implemented for you, which takes in a `0` or `1` and outputs emoji representing light bulbs.)

Here’s an example of how the completed program might work. Unlike the Sanders stage, we’ll print one byte per line for clarity.

    # ./bulbs
    Message: HI!
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫🟡
    

To check our work, we can read a bulb that’s on (🟡) as a `1` and bulb that’s off (⚫) as a `0`. Then `HI!` became

    01001000
    01001001
    00100001
    

which is precisely what we’d expect.

Another example:

    # ./bulbs
    Message: HI MOM
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫⚫
    ⚫🟡⚫⚫🟡🟡⚫🟡
    ⚫🟡⚫⚫🟡🟡🟡🟡
    ⚫🟡⚫⚫🟡🟡⚫🟡
    

Notice that all characters are included in the lightbulb instructions, including nonalphabetical characters like spaces (`00100000`).
