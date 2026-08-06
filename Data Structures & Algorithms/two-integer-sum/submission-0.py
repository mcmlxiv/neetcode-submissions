class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        obj = {}

        for i,n in enumerate(nums):
            comp = target - n
            
            if comp in obj:
                return [obj[comp],i]
            
            obj[n] = i
