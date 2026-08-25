class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> index;
        int size = nums.size();
        for(int i = 0; i < size; i++) {
            int diff = target - nums[i];
            if (index.find(diff) != index.end()) {
                return {index[diff], i};
            }
            index[nums[i]] = i;
        }
        return {};
    }
    
};
