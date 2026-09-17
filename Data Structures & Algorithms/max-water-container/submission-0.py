class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to find the two highest bars but also with the widest width
        left = 0
        right = len(heights) - 1
        biggest_area = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            if area > biggest_area:
                biggest_area = area
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

        return biggest_area