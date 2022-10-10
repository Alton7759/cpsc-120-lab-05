![Formatting](../../../actions/workflows/part-1.yml/badge.svg)

# Average

In this exercise, you will write a program that calculate the **average** of numbers given as command-line arguments.

In mathematics, there are several kinds of average. Your program will compute the [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean), which is the most widely known kind of average. If $x_1, x_2, \ldots, x_n$ are $n$ values, then the *arithmetic mean* $a$ is

$$ a = \frac{1}{n} \sum_{i=1}^{n} x_i .$$

In words, this equation means that the average is equal to the sum of all the values, divided by the number of values. 

Your program will require at least one value to be given as a command line argument. It will compute the average of the values, and print output according to the pattern:

"average = *ARITHMETIC-MEAN*"

Your program must:
- Store values in a `double` or `float` variable.
- Use floating point arithmetic to compute the average, so that averages with decimal parts are calculated accurately.
- Properly handle values that are negative or zero.

## Input Validation

Your program should validate that there is at least one command line argument.

If there are no command line arguments, your program should print
```
error: you must supply at least one number
```
and return a non-zero exit code.

For example:
```
$ ./average
error: you must supply at least one number
```

Your program must not suffer a runtime error in this situation.

## Example Input and Output

```
$ ./average
error: you must supply at least one number
```

```
$ ./average 7
average = 7
```

```
$ ./average 2 4
average = 3
```

```
$ ./average 1 1 2 9
average = 3.25
```

```
$ ./average 3 -5
average = -1
```

## Test Cases

As usual, test your program against the test suite below.

| Test Case | Input                              | Expected Output                          |
|-----------|------------------------------------|------------------------------------------|
| 1         | 1 2               | `average = 2` |
| 2         | 10 20             | `average = 15` |
| 3         | 1.2 1.8              | `average = 1.5` |
| 4         | -3 5                 | `average = 1` |
| 5         | -2 -4                | `average = -3` |
| 6         | 7 1 2                | `average = 3.33333` |

## What to Do

1. With your partner, edit the `average.cc` source file using VS Code. Add the required header. Replace all the TODO comments with working code.
1. Compile your program with the `$ make` shell command. Use the **debug compile error** procedure to debug any compile errors.
1. Run your program with the `$ ./average` shell command.
1. Test that your program passes all of the test cases in the test suite above. If your program suffers a runtime error, use the **debug runtime error** procedure to debug the error. If your program does not produce the expected output, use the **debug logic error** procedure to debug the error.
1. Test your program against automated test with the `$ make test` command. Debug any runtime errors or logic errors using the same procedures.
1. Check your header with the `$ make header` shell command. Correct any errors.
1. Check for format errors with the `$ make format` shell command. Correct any errors.
1. Check for lint errors with the `$ make lint` shell command. Correct any errors.
1. After your program passes all of these tests and checks, push your code to GitHub. Use the usual trio of commands: `git add`, `git commit`, and `git push`.

## Next Steps

After you have pushed your code, move on to part 3.
