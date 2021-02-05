//
// Created by khalidzhang on 2020/12/22.
//
#include "temp.h"
#include "word.h"
int main(int argc, char *argv[]) {
  word w("aha cpp");
  printf("%s", w.getWord().c_str());
  return 0;
}
