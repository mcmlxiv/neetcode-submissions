class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
       
        res = []

        def backtrack(i,combination, total):
            if total == target:
                res.append(combination.copy())
                return
            
            if total > target:
                return
            if i >= len(nums):
                return
            
            combination.append(nums[i])
            backtrack(i, combination, total + nums[i])
            combination.pop()
            backtrack(i + 1 , combination, total)
        
        backtrack(0,[], 0)

        return res
                