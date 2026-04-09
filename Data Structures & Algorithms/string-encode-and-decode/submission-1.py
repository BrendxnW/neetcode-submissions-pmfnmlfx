class Solution:

    def encode(self, strs: List[str]) -> str:

        new_string = ""
        for word in strs:
            new_string += str(len(word)) + "!" + word
        return new_string

    def decode(self, s: str) -> List[str]:

        og_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "!":
                j += 1
            length = int(s[i:j])
            og_list.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return og_list