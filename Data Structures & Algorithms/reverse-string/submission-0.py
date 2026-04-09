class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        point_1, point_2 = 0, len(s) - 1

        while point_1 < point_2:
            s[point_1], s[point_2] = s[point_2], s[point_1]
            point_1, point_2 = point_1 + 1, point_2 -1