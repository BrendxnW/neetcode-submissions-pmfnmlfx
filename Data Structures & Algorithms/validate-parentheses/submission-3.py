class Solution:
    def isValid(self, s: str) -> bool:
        compliment = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for letter in s:
            if letter not in compliment:
                stack.append(letter)

            else:
                if stack and stack[-1] == compliment[letter]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False

            
                