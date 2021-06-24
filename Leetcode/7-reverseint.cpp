#include <limits.h>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            if (res > 0 && (INT_MAX/10 < res || (INT_MAX / 10 == res && INT_MAX % 10 < x % 10))) {
                return 0;
            } else if (res < 0 && (INT_MIN/10 > res || (INT_MIN / 10 == res && INT_MIN % 10 > x % 10))) {
                return 0;
            }
            res = res * 10 + (x % 10);
            x = x / 10;
            // how to check if outside 32 bit range? convert to binary
        }
        return res;
    }
};