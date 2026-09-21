class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(total, i, combination):
            if total == target:
                res.append(combination.copy())
            
            if i >= len(nums) or total >= target:
                return
            
            combination.append(nums[i])
            dfs(total + nums[i], i, combination)
            combination.pop()
            dfs(total, i+1, combination)
        
        dfs(0,0,[])
        return res