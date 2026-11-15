class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0:
                break

            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            l, r = i + 1, len(sorted_nums) - 1
            
            while l < r:
                if sorted_nums[l] + sorted_nums[r] + sorted_nums[i] > 0 :
                    r -= 1

                elif sorted_nums[l] + sorted_nums[r] + sorted_nums[i] < 0:
                    l += 1
                
                else:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1

        return res