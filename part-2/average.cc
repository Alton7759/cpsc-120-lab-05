// TODO: Add the required header

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);
  double sum{0};
  int i = 1;
  // TODO: Validate that there is at least one command line argument.
  // If not, print an error message and return a non-zero value.
  if (arguments.size() <= 1) {
    std::cout << "error: must supple at least one number\n";
  }
  // TODO: Write a for-each loop to sum (add up) all of the command line
  // arguments.
  // Use a double or float type so that your program preserves fractional
  // values.
  // The loop needs to skip over the command name, which is the first element
  // of the arguments vector.
  // Each argument is a std::string. You will need to convert each string into
  // a number with the std::stod or std::stof function.
  bool skip{true};
  for (const std::string& num : arguments) {
    if (skip == true) {
      skip = false;

    } else {
      sum = sum + std::stod(arguments.at(i));
      i++;
    }
    int s = arguments.size() - 1;
  }
  std::cout << sum;
  // TODO: After the loop has finished summing the arguments, calculate the
  // average of the values. Recall that the average is the total value divided
  // by the number of values.

  // TODO: Use cout to print out a message of the form
  // average = *AVERAGE*
  // on its own line.

  return 0;
}
