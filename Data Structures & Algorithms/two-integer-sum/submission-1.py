class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}

        for i in range(len(nums)): 
            n = nums[i]
            req = target - n
            
            if req in sum:
                return [sum.get(req), i]
            sum[n] = i
        
        return [-1,-1]
        