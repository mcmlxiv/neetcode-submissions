class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charMap = {}
        l = 0 

        for r in range(len(s)):
            if s[r] in charMap:
                l = max(charMap[s[r]] + 1, l)

            charMap[s[r]] = r
            res = max(res, r - l + 1)

        
        return res
