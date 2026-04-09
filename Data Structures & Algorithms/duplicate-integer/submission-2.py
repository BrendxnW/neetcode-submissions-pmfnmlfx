class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in nums:
            if i not in seen:
                seen[i] = 1 + seen.get(i, 0)

            else:
                return True

        return False