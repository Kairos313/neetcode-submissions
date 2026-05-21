class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        res = [1]*len(nums)
        prodp = 1
        for i in range(len(nums) - 1):
            prodp *= nums[i]
            prefix[i + 1] = prodp
        
        prods = 1
        for i in range(len(nums) - 1, 0, -1):
            prods *= nums[i]
            suffix[i - 1] = prods
        
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res