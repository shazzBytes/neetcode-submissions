#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> uniques;
        for (int i: nums)  {
            if (uniques.find(i) == uniques.end()) {
                uniques.insert({i, i});
            }
            else {
                return true;
            }
        }
        return false;
    }
};