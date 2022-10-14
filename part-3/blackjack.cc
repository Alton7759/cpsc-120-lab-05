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

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);
  std::vector<std::string> numbers{
      "2", "3", "4", "5", "6", "7", "8", "9", "10",
  };
  std::vector<std::string> faces{
      "J",
      "Q",
      "K",
  };
  int score = 0;
  int num_card_value = 0;
  bool rcard{false};
  for (int i = 1; i < arguments.size(); i++) {
    if (arguments[i] == "A") {
      if (score + 11 > 21) {
        score += 1;
        rcard = true;
      } else {
        score += 11;
        rcard = true;
      }
    }
    for (const std::string& bruh2 : faces) {
      if (arguments[i] == bruh2) {
        score += 10;
        rcard = true;
      }
    }
    for (const std::string& bruh : numbers) {
      if (arguments[i] == bruh) {
        num_card_value = stoi(bruh);
        score += num_card_value;
        rcard = true;
      }
    }
    if (score > 21) {
      std::cout << "Score is " << score << ", BUST \n";
    }
    if (!rcard) {
      std::cout << "error: unknown card '" << arguments[i] << "'\n";
      return 1;
    }
  }
  std::cout << "Score is " << score << "\n";
  return 0;
}
