class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                else:
                    l += 1
                    r -= 1
            return True

        new_s = "".join(filter(str.isalnum, s)).lower()
        l, r = 0, len(new_s) - 1

        while l < r:
            if new_s[l] != new_s[r]:
                return isPalindrome(s, l + 1, r) or isPalindrome(s, l, r - 1)

            l += 1
            r -= 1
        return True