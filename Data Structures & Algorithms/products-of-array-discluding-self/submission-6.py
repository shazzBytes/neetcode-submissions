class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefArr = [1 for _ in range(length)]
        suffArr = [1 for i in range(length)]
        output = [0 for i in range(length)]
        for i in range(1, length):
            prefArr[i] = nums[i-1] * prefArr[i-1]
        for i in range(length-2, -1, -1):
            suffArr[i] = nums[i+1] * suffArr[i+1]
        
        for i in range(length):
            output[i] = prefArr[i] * suffArr[i]
        return output