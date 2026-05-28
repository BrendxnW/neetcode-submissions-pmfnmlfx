class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for word in strs:
            decode = [0] * 26

            for c in word:
                idx = ord(c) - 97
                decode[idx] += 1
            res[tuple(decode)].append(word)

        return list(res.values())
