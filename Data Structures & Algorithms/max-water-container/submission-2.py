class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_height = 0

        while l < r:
            width = r - l

            if heights[r] <= heights[l]:
                temp_height = heights[r] * width
                max_height = max(max_height, temp_height)  
                r -= 1

            else:
                temp_height = heights[l] * width
                max_height = max(max_height, temp_height)  

                l += 1
        return max_height