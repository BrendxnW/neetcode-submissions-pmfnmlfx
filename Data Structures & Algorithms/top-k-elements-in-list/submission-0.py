class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        answer = []

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1


        while k > 0:
            high_value = max(freq, key=freq.get)
            answer.append(high_value)
            freq.pop(high_value)
            k -= 1

        return answer