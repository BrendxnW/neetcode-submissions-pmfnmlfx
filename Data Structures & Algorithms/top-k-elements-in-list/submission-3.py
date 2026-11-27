class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        while k > 0:
            high_value = max(seen, key=seen.get)
            res.append(high_value)
            seen.pop(high_value)
            k -= 1
        return res