#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            vector<int> ls;
            for (int i = 0; i <= nums.size(); i++) {
                for (int j = 0; j < i; j++) {
                    if (nums[j] == target - nums[i]) {
                        ls = {i, j};
                        return ls;
                    }
                }
            }
            return ls;
        }
};