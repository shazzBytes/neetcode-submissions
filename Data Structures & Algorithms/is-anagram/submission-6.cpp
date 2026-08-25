#include <map>
#include <vector>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != s.length()) {
            return false;
        }
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s==t;
    }
};
