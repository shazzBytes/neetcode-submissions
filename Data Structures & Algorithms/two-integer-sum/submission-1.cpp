class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> index;
        int s = nums.size();
        for(int i = 0; i < s; i++) {
            // [3, 4, 5, 6], target 7
            // diff = 4, not in map, 
            // index[3] = 0
            // diff = 3, index.find(3) = true
            // 
            int diff = target - nums[i];
            if (index.find(diff) != index.end()) {
                return {index[diff], i};
            }
            index[nums[i]] = i;
        }
        return {};
    }
};
