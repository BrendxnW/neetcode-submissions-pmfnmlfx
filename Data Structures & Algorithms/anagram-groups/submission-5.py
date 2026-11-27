class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            code = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                code[index] += 1
            
            res[tuple(code)] = res.get(tuple(code), []) + [word]

        return list(res.values())