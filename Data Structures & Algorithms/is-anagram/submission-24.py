class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        schar = {}
        tchar = {}
        for i, n in enumerate(s):
            if n not in schar:
                schar[n] = 0
            schar[n] += 1

        for i, n in enumerate(t):
            if n not in tchar:
                tchar[n] = 0
            tchar[n] += 1

        return schar == tchar