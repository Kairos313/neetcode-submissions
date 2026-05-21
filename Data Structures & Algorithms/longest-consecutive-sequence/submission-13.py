class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 1
        if len(nums) == 0:
            return 0
            
        for i in range(len(nums)):
            if (nums[i] - 1) not in s:
                j = 1
                while (nums[i] + j) in s:
                    j += 1
                longest = max(longest, j)
        return longest
