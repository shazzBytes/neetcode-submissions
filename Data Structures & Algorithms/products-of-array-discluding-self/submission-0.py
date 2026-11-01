class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        i want to multiply all the items except self.
        the first one would map[1] = 1; then 
        the second one would be map[2] = 1;
        the third one would be map[4] = 1;
        the fourth one would be map[6] = 1;
        '''
        n = len(nums)
        zeroes = 0;
        prod = 1
        for i in nums:
            if i:
                prod *= i
            else:
                zeroes += 1
            if zeroes > 1:
                return [0]*n
        res = [0]*n;
        for i, c in enumerate(nums):
            if zeroes:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res