class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {"}":"{","]":"[",")":"("}

        for chr in s:
            if stack and chr in brackets:
                if stack[-1] == brackets[chr]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(chr)

        return len(stack) == 0


