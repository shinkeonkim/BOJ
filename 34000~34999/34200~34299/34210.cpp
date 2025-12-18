#include "aplusb.h"

std::vector<int> AA;
std::vector<int> BB;

void initialize(std::vector<int> A, std::vector<int> B) {
    AA = A;
    BB = B;
}

int answer_question(int i, int j) {
  return AA[i] + BB[j];
}
