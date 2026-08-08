class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r : 
            if s[l] != s[r]:
                noLeft = s[l+1:r+1] 
                noRight = s[l:r]

                return noLeft == noLeft[::-1] or noRight == noRight[::-1]

            l += 1
            r -= 1
        
        return True
