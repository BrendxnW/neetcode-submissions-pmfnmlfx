class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = 0
        while n < len(nums):
            if nums[n] != val:
                n += 1
            else:
                nums.pop(n)

        return len(nums)