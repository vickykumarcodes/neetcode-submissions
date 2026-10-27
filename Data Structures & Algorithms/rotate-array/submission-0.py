class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        new_list = []
        for i in range(n):
            index = (i - k) % n
            new_list.append(nums[index])
        nums[:] = new_list
