class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        window.add(nums[0])
        l = 0 

        for r in range(l+1,len(nums)):
            while abs(l - r) > k and window:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True
            window.add(nums[r])
        
        return False
        