class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in prev:
                return [prev[x], i]
            else:
                prev[n] = i