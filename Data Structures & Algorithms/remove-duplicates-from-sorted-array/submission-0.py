class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        l, r = 0, 1

        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                r += 1
                continue

            else:
                nums.pop(r)
                k -= 1
        return k