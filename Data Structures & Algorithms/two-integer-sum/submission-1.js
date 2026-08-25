class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let index = new Map()
        for(let i = 0; i < nums.length; i = i+1) {
            let diff = target-nums[i]
            if (index.has(diff)) {
                return [index.get(diff), i];
            }
            index.set(nums[i], i)
        }
        return []
    }
}
