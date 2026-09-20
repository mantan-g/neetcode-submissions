class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for k in s:
            freq[k] = freq.get(k, 0) + 1
        
        for k in t:
            if k not in freq:
                return False
            
            freq[k] -= 1
            if(freq[k] < 0):
                return False

        return True
