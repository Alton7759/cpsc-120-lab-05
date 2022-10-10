![Formatting](../../../actions/workflows/part-1.yml/badge.svg)

# Blackjack Score

In this exercise, you will write a program that computes the score for a hand of blackjack.

[Blackjack](https://en.wikipedia.org/wiki/Blackjack) is a casino card game. The game involves a dealer, who is usually a casino employee, and one or more players. Players take turns. On a player's turn, they may "**hit**", meaning draw one card; or "**stand**", meaning to end their turn without taking any cards. (There are additional options that we are omitting for now.)

The object of the game is to attain the highest score possible, without going over 21. A total score greater than 21 is called a "**bust**" and is an automatic loss.

Each card contributes to a player's score as follows:

| Card Type | Score |
|-----------|-------|
| Number card (2 through 10) | the value of the number |
| Face card (jack, queen, or king) | 10 |
| Ace | 1, plus possible bonus; see below |

**Ace bonus**: If a player's hand includes an ace, they may count that ace as 11 points instead of 1. To avoid a bust, this bonus only applies when it increases the score to 21 or less.

Only one ace bonus will ever apply. Two aces with the bonus would count for 22 points, surely a bust. So if the ace bonus is used, it is only used once.

When a player's first two cards total 21 exactly, this is called a "**blackjack**".  A blackjack is a combination of one ace, with one 10 or face card. A blackjack is an automatic win (or tie with other blackjacks).

Here are some scoring examples:

| Cards | Score |
|-------|-------|
| 9, 8 | 17 |
| 5, 6, 7 | 18 |
| 10, 5, 8 | 23 (bust)
| 2, 5, ace| 18 (uses ace bonus) |
| ace, king | 21 (blackjack, uses ace bonus) |
| king, queen, ace | 21 (does not use ace bonus) |

The input to your program is a list of cards, given as command line arguments. Your program should recognized the following names for cards:

| Input | Card | Score |
|-------|------|-------|
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | 10 | 10 |
| J | jack | 10 |
| Q | queen | 10 |
| K | king | 10 |
| A | ace | 1 or 11 |

Observe that each card name is either a **whole number** or a **capital letter**.

Your program should compute the score of the given list of cards. If there is no bust (score is less than or equal to 21), print output

"Score is *SCORE*"

If there is a bust (score is greater than 21), print output

"Score is *SCORE*, BUST"

When there are no command line arguments, your program should treat that as a valid list of no cards, and print output

"Score is 0"

## Input Validation

Your program should validate that every command line argument is a valid card name.

If one of the command line arguments is not a valid card name, your program should print

"error: unknown card '*ARGUMENT*'"

and return a non-zero exit code.

For example:
```
$ ./blackjack 5 A wombat 4
error: unknown card 'wombat'
```

Your program must not suffer a runtime error in this situation.

## Example Input and Output

```
$ ./blackjack 10 X
error: unknown card 'X'
```

```
$ ./blackjack
Score is 0
```

```
$ ./blackjack 9 8
Score is 17
```

```
$ ./blackjack 5 6 7
Score is 18
```

```
$ ./blackjack 10 5 8
Score is 23, BUST
```

```
$ ./blackjack 2 5 A
Score is 18
```

```
$ ./blackjack A K
Score is 21
```

```
$ ./blackjack K Q A
Score is 21
```

## Test Cases

As usual, test your program against the test suite below.

| Test Case | Input                              | Expected Output                          |
|-----------|------------------------------------|------------------------------------------|
| 1         | (no arguments)      | `Score is 0` |
| 2         | 7               | `Score is 7` |
| 3         | 10              | `Score is 10` |
| 4         | J               | `Score is 10` |
| 5         | Q               | `Score is 10` |
| 6         | K               | `Score is 10` |
| 7         | A               | `Score is 11` |
| 8         | 5 Q             | `Score is 15` |
| 9         | 2 9 8            | `Score is 19` |
| 10        | K 5 6            | `Score is 21` |
| 11        | 10 10 10            | `Score is 30, BUST` |
| 12        | J K 3            | `Score is 23, BUST` |
| 13        | 5 10 A           | `Score is 16` |
| 14        | Q A           | `Score is 21` |
| 15        | 6 A           | `Score is 17` |
| 16        | A A A A A     | `Score is 15` |

## What to Do

1. With your partner, edit the `blackjack.cc` source file using VS Code. Add the required header. Replace all the TODO comments with working code.
1. Compile your program with the `$ make` shell command. Use the **debug compile error** procedure to debug any compile errors.
1. Run your program with the `$ ./blackjack` shell command.
1. Test that your program passes all of the test cases in the test suite above. If your program suffers a runtime error, use the **debug runtime error** procedure to debug the error. If your program does not produce the expected output, use the **debug logic error** procedure to debug the error.
1. Test your program against automated test with the `$ make test` command. Debug any runtime errors or logic errors using the same procedures.
1. Check your header with the `$ make header` shell command. Correct any errors.
1. Check for format errors with the `$ make format` shell command. Correct any errors.
1. Check for lint errors with the `$ make lint` shell command. Correct any errors.
1. After your program passes all of these tests and checks, push your code to GitHub. Use the usual trio of commands: `git add`, `git commit`, and `git push`.

## Next Steps

After you have pushed your code, you are done with this lab. You may ask your TA for permission to sign out and leave.
