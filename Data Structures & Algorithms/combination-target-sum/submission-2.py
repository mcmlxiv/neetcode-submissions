class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        setSum = []
        res = []

        def backtrack(i,combination, target):
            if combination == target:
                res.append(setSum.copy())
                return
            
            if combination > target:
                return
            if i >= len(nums):
                return
            
            setSum.append(nums[i])
            backtrack(i, combination + nums[i], target)
            setSum.pop()
            backtrack(i + 1 , combination, target)
        
        backtrack(0,0, target)

        return res
                