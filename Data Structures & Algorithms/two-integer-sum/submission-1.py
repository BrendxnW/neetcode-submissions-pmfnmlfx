class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            compliment = target - n

            if compliment not in seen:
                seen[n] = i

            else:
                return[seen[compliment], i]