class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        method - The three reversal
        1. reverse the nums
        2. reverse the first k elements
        3. reverse the rest
        """
        n = len(nums)
        k = k % n
        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        helper(0, n-1)
        helper(0, k-1)
        helper(k, n-1)
        """
        Initialize with a new list, then for each index i put (i - k) % n, 
        copy the new  list to nums.
        """
    def rotate_extra_list(self, nums: List[int], k: int) -> None:
        n = len(nums)
        new_list = []
        for i in range(n):
            index = (i - k) % n
            new_list.append(nums[index])
        nums[:] = new_list
