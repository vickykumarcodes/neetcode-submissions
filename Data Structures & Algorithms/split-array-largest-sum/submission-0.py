class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            
            # Count the pieces needed with capacity cap = mid
            pieces = 1
            current = 0
            for x in nums:
                if current + x > mid:
                    pieces += 1
                    current = 0
                current += x
                
            # If it's possible to split into <= k pieces, try a 
            #smaller  maximum sum
            if pieces <= k:
                answer = mid
                high = mid - 1
            # Otherwise, the capacity 'mid' is too small, 
            # increase the lower bound
            else:
                low = mid + 1
            
        # Return the minimized largest sum
        return answer