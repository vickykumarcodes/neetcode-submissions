class Solution:
    def trap(self, height: List[int]) -> int:
        """
        set l, r, left_best, right_best, total
        while l < r:
            if height[l] < height[r]: update left_best with height[l], 
                add left_best - height[l] to total, then l += 1
            else: do the mirror on the right side
        return total
        """
        l = 0
        r = len(height) - 1
        left_best = 0
        right_best = 0
        total = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_best:
                    left_best = height[l]
                else:
                    total += left_best - height[l]
                l += 1
            else:
                if height[r] >= right_best:
                    right_best = height[r]
                else:
                    total += right_best - height[r]
                r -= 1
        return total

        
    def trap_arrays(self, height: List[int]) -> int:
        # Another method
        n = len(height)
        # make left_max as a list of n zeros, and the same for right_max
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] = height[n - 1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        total = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            total += water_level - height[i]
        
        return total

        