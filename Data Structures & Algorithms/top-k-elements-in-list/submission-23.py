class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for i, n in enumerate(nums):
            if n not in count:
                count[n] = 1
            else:    
                count[n] += 1
        
        for c, i in count.items():
            freq[i].append(c)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res




