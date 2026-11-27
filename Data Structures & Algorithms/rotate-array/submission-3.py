class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n

        def Reverse(l, r):
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        Reverse(0, n - 1)
        Reverse(0, k - 1)
        Reverse(k, n - 1)