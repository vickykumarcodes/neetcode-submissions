class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = 0
        while l < r:
            # compute width and height of the current pair
            width = r - l
            height = min(heights[r], heights[l])

            # compute water and update best if it is larger
            water = width * height
            if water > best:
                best = water
            
            # move the pointer that points at the shorter bar
            #(if two are equal, any side will work)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best
