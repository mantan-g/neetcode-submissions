class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}

        for ss in s:
            c = sMap.get(ss)
            if c is None:
                sMap[ss] = 1
            else:
                sMap[ss] = sMap[ss] + 1
        
        for tt in t: 
            if tt in sMap:
                c = sMap.get(tt)
                if c == 0: 
                    return False
                else: 
                    c = sMap[tt] - 1
                    sMap[tt] = c
            else:
                return False

    
        for ss in sMap:
            if sMap.get(ss) > 0:
                return False

        return True
