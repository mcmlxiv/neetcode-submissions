class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        length = 1

        for n in numSet:
            
            if (n + 1) in numSet:
                length = 1

                while (n+1) in numSet:
                    length+= 1
                    n += 1
            
            longest = max(longest, length)
        return longest


    