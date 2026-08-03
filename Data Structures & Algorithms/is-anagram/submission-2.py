class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}

        for c in s:
            s1[c] = 0
        for c in s:
            s1[c] += 1
        
        for c in t:
            if c not in s1:
                return False

            s1[c] -= 1
        
        for c in s1:
            if s1[c] is not 0:
                return False

        return True
            
        