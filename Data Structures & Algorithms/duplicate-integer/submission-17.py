class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        a = []
        s = set()
        for i in nums:
            if i in s:
                a.append(i)
            else:
                s.add(i)
        if (len(a) > 0):
            return True
        else:
            return False