class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = {}

        for i, n in enumerate(nums):
            if n in window and abs(window[n] - i ) <= k :
                return True
            
            window[n] = i
        
        return False
        