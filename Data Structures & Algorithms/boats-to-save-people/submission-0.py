class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        l, r = 0, len(people) - 1

        people.sort()

        while l <= r:
            remain = limit - people[r]
            r -= 1
            boats += 1

            if l <= r and people[l] <= remain:
                l += 1

        return boats