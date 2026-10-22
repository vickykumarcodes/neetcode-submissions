class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # pass 1: left to right
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]
        
        # pass 2: right to left
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result