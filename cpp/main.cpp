#include <iostream>

using namespace std;
int main() {
  int width, length, blocks, winwall, windows, trees;
  cin >> width;
  cin >> length;
  blocks = width * length * 2 + width * 4 + length * 4 - 8; //solid
  blocks -= 2; //door
  winwall = max(width, length);
  windows = ((winwall - 4) / 3 + (winwall % 3 == 0 ? 0 : 1)) * 2;
  blocks -= windows;
  trees = blocks / 2 + (blocks % 2);
  cout << trees;
  return 0;
}
