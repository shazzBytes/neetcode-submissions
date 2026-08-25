class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let index:Map<number,number> = new Map<number,number>();
        for(let i: number = 0; i < nums.length; i++) {
            let diff: number =  target - nums[i];
            if (index.has(diff)) {
                return [index.get(diff), i]
            }
            index.set(nums[i], i)
        }
        return []
    }
}
