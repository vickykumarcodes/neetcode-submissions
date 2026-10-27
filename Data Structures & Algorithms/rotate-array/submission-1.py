class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Initialize with a new list, then for each index i put (i-k)%n, copy the new list to nums.
        """
        n = len(nums)
        k = k % n
        #new_list = []
        #for i in range(n):
        #    index = (i - k) % n
        #    new_list.append(nums[index])
        #nums[:] = new_list
        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        helper(0, n-1)
        helper(0, k-1)
        helper(k, n-1)

