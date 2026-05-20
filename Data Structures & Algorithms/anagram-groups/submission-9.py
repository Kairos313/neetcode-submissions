class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            res[s].append(i)
        return(list(res.values()))



# Create a dictionary of lists
# Sort all lists
# Add them to res where they all have the same key