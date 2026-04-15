class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        l, r = 0, len(height) - 1
        lh = height[l]
        rh = height[r]
        while l < r - 1:
            if lh < rh:
                l+=1
                while height[l] < lh:
                    total_area += lh - height[l]
                    l += 1
                lh = height[l]
            else:
                r -= 1
                while height[r] < rh:
                    total_area += rh - height[r]
                    r -=1
                rh = height[r]
        return total_area
                

        