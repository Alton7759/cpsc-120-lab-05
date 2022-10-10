// TODO: Add the required header

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);

  // TODO: Declare variables necessary to make your loop work.

  // TODO: Write a for-each loop that iterates through the command line
  // arguments.
  // The loop needs to skip over the command name, which is the first element
  // of the arguments vector.
  // For each card:
  //   - A number card (2 through 10) counts as its value. So a 5 adds 5 to
  //     the score.
  //   - A face card (J, Q, K) counts as 10.
  //   - An ace (A) counts as 1.
  //   - If an argument is invalid (none of "2" through "10", "J", "Q", "K",
  //     or "A": print the error message
  //        error: unknown card '*ARGUMENT*'
  //     and stop the program with a non-zero error code.
  // Further, an ace may count as 11 if it increases the score, without making
  // the score go over 21.

  // TODO: If the score is 21 or less, print output of the form
  // Score is *SCORE*
  // Otherwise (score is greater than 21), print output of the form
  // Score is *SCORE*, BUST

  return 0;
}
