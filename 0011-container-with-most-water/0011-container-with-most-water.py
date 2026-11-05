class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        maximum_area = 0

        while left<right:

            width = right - left
            h = min(height[left], height[right])

            area = width * h

            maximum_area = max(area, maximum_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum_area
        