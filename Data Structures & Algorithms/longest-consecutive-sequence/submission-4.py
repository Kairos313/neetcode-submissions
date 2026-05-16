class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) not in setnums:
                length = 0
                while (i + length) in setnums:
                    length += 1
                longest = max(longest, length)
        return longest