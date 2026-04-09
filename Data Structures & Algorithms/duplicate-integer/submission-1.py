class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for number in nums:
            if number not in seen:
                seen[number] = 1
            else:
                return True

        return False