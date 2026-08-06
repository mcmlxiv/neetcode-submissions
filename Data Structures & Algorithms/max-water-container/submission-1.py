class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tallest = 0


        l,r = 0, len(heights)  - 1


        while l<r:
            height = min(heights[l], heights[r])
            area = r-l
            tall = height * area

            tallest= max(tallest, tall)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
            
        
        return tallest
