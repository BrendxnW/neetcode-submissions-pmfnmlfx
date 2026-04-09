class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = {0 : 1}
        cur_sum = 0
    
        for num in nums:
            cur_sum += num
            diff = cur_sum - k

            if diff in prefix:
                res += prefix[diff]

            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1

        return res