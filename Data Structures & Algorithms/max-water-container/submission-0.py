class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights)-1
        while left < right:
            l_h = heights[left]
            r_h = heights[right]
            max_area = max(max_area, (right - left)*min(l_h, r_h))
            if l_h < r_h:
                left+=1
            else:
                right-=1
        return max_area 
        