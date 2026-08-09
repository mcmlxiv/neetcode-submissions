class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'}':'{', ']':'[', ')':'('}

        for chr in s:
            if chr in brackets:
                if stack and brackets[chr] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(chr)

        
        return len(stack) == 0
