class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = list(s)
        k = list(t)
        print(l, k)
        l.sort()
        k.sort()
        print(l, k)
        if l == k:
            return True
        else:
            return False