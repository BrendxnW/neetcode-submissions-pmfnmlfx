class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        k = 0


        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                r += 1


            else:
                nums.pop(r)
                

        return r