class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        for l in range(len(nums)):
            r = l + 1

            while (abs(l-r) <=k) and r<len(nums):
                if nums[l] == nums[r]:
                    return True
                
                r+=1
        
        return False
        
        
        
        
        l = 0
        r = 1

        while l<r and r<len(nums):
            
            numSet= set()
            numSet.add(nums[l])

            while (abs(l-r)) <= k and r<len(nums):
                if nums[r] in numSet:
                    return True
                
                numSet.add(nums[r])
                r+= 1
            
            l+=1
            r= l+1
        
        return False



