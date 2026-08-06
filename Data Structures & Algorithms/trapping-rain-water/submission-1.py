class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height) - 1
        leftMax, rightMax = height[l], height[r]

        output = 0 


        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                output += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                output += rightMax - height[r]
        
        return output
