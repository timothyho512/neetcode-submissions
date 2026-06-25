class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # There could be an easy answer with a time complexity of O(n^2)
        # where we use two pointers and just loop through every single possible combination

        ans = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            ans = max(ans, (right - left)* min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
        return ans