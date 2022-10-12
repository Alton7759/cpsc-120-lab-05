// Christian Alton Bonilla
// CPSC 120-01
// 2022-10-12
// Alton77@csu.fullerton.edu
// @alton7759
//
// Lab 05-03
// Partners: @Jaylinmai
//
// we get to play blackjack
//

#include <array>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);
  std::array<std::string, 9> numbers = {"2", "3", "4", "5", "6",
                                        "7", "8", "9", "10"};
  std::array<std::string, 9> faces = {"K", "k",    "q",     "Q",   "J",
                                      "j", "jack", "queen", "king"};
  int allnums{0};
  bool facespass{false};
  bool numberspass{false};
  bool apass{false};
  bool skip{true};
  for (const std::string& check : arguments) {
    if (check == "A") {
      apass = true;
      if (allnums + 11 > 21) {
        allnums += 1;
      } else {
        allnums += 11;
      }
    } else {
      apass = false;
    }
    for (const std::string& numberc : numbers) {
      if (check == numberc) {
        allnums += std::stoi(numberc);
        numberspass = true;

      } else {
        numberspass = false;
      }
    }
    for (const std::string& facec : faces) {
      if (check == facec) {
        allnums += 10;
        facespass = true;

      } else {
        facespass = false;
      }
    }
    if (skip) {
      skip = false;
    } else if (facespass || numberspass || apass) {
    } else {
      std::cout << "error: unknown card '" << check << "'\n";
      return 0;
    }
  }
  if (allnums > 21) {
    std::cout << "Score is " << allnums << ", BUST\n";
    return 0;
  }
  std::cout << "Score is " << allnums << "\n";

  return 0;
}
