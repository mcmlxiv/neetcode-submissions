class Solution:
    def isValid(self, s: str) -> bool:
        mapParans = {')':'(','}':'{',']':'['}
        stack = []

        for char in s:
            if char in mapParans:
                if stack and stack[-1] == mapParans[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
            
                