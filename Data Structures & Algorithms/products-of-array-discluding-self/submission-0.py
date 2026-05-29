class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            pointer = 0
            product = 1
            temp = []   
            while pointer < len(nums):
                if pointer != i:
                    temp.append(nums[pointer])

                pointer += 1

            for num in temp:
                product *= num
            res.append(product)

        return res