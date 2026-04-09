class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) != len(t):
            return False

        for c in s:
            seen[c] = seen.get(c, 0) + 1

        for l in t:
            if l not in seen:
                return False
            else:
                seen[l] -= 1

        return all(count == 0 for count in seen.values())