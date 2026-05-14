class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i
        
        for i, n in enumerate(nums):
            x = target - n
            if x in indices and indices[x] != i:
                return [i, indices[x]]
        return []