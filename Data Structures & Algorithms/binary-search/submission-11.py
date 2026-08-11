class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binaryS(0, len(nums) - 1, nums, target)

    def binaryS(self, l, r, nums, target):
        if l > r:
            return - 1

        m = (l + r) // 2

        if nums[m] == target:
            return m
        
        if nums[m] < target:
            return self.binaryS(m + 1, r, nums, target)
        
        if nums[m] > target:
            return self.binaryS(l, m - 1, nums, target)