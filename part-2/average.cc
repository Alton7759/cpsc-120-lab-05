// Christian Alton bonilla
// CPSC 120-01
// 2022-09-21
// Alton77@csu.fullerton.edu
// @alton7759
//
// Lab 01-01
// Partners: @annavera38
//
// prints the change from fahrenheit to celsius
//

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);
  double sum{0};
  int i{1};
  if (arguments.size() <= 1) {
    std::cout << "error: must supple at least one number\n";
    return 0;
  }
  bool skip{true};
  for (const std::string& num : arguments) {
    if (skip) {
      skip = false;

    } else {
      sum = sum + std::stod(num);
      i++;
    }
  }
  double s = arguments.size() - 1.0;
  double average = sum / s;
  std::cout << "average = " << average << "\n";
  return 0;
}
