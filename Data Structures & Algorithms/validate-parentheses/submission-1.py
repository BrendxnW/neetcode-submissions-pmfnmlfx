class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = []

        for c in s:
            if c not in close:
                stack.append(c)

            else:
                if stack and stack[-1] == close[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False