class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()
        l = 0

        for r in range(len(nums)):
            # pop smaller values from the back so q stays monotonically decreasing.        
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove the left most index if it falls outside the current window
            if l > q[0]:
                q.popleft()

            # once the window reaches size k, record the max and slide left pointer
            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
        return result