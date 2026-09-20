class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        sMap = {}

        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))

            if sMap.get(s) is None:
                sMap[s] = [strs[i]]
            else:
                sMap[s].append(strs[i])
            
        for s in sMap:
            ans.append(sMap[s])

        return ans
