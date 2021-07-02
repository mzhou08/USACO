#include <string.h>
#include <map.h>

class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        map <char, int> vals = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        map <char, int>::iterator here;
        map <char, int>::iterator aft;
        for (int i = 0; i < s.size() - 1; i++) {
            here = vals.find(s[i]);
            aft = vals.find(s[i + 1]);
            if (here->second >= aft->second) {
                sum += here->second;
            } else {
                sum -= here->second;
            }
        }
        here = vals.find(s.back());
        sum += here->second;
        return sum;
    }
};