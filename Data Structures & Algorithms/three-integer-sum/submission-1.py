class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and n == nums[i-1]:
                continue
            

            l,r = i+1, len(nums) - 1

            while l < r:
                numSum = nums[l] + nums[r] + n

                if numSum > 0:
                    r-=1
                elif numSum < 0 :
                    l+=1
                else:
                    res.append([nums[l], nums[r], n])
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        
        return res
