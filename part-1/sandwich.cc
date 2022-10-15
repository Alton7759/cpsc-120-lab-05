// Christian Alton bonilla
// CPSC 120-01
// 2022-10-10
// Alton77@csu.fullerton.edu
// @alton7759
//
// Lab 05-01
// Partners: @jaylinmai
//
// Program to calculate the number of days between two Gregorian dates.
//

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);
  if (arguments.size() != 4) {
    std::cout << "error: you must supply three arguments\n";
    return 1;
  }
  std::string protein = arguments.at(1);

  std::string bread = arguments.at(2);

  std::string condiment = arguments.at(3);

  std::cout << "Your order:\n"
            << "A " << protein << " sandwich on " << bread << " with "
            << condiment << "."
            << "\n";
  return 0;
}
