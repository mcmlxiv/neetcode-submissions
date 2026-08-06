class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        numSet = set(nums)

        for n in numSet:
            length = 0

            if not (n - 1) in numSet:
                length = 1

                while n + length in numSet:
                    length += 1
                
                longest = max(longest, length)
            
        
        return longest