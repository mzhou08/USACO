#include <iostream>
#include <vector>

int main() {
  int K;
  int M;
  int N;
  std::cin >> K >> M >> N;

  std::vector< std::vector<int> > patches;
  std::vector<int> nhoj_cows;

  for (int i = 0; i < K; i++) {
    int patch_i;
    int tastiness_i;

    std::cin >> patch_i >> tastiness_i;

    std::vector<int> patch_info;
    patch_info.push_back(patch_i);
    patch_info.push_back(tastiness_i);

    patches.push_back(patch_info);
    
  }
}
