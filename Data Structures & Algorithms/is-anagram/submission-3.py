class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seenS, seenT = {}, {}

        for letters in range(len(s)):
            seenS[s[letters]] = 1 + seenS.get(s[letters], 0)
            seenT[t[letters]] = 1 + seenT.get(t[letters], 0)

        for characters in seenS:
            if seenS[characters] != seenT.get(characters, 0):
                return False
        return True