class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1
        
        i = 0
        for color in range(3):
            for c in range(counts[color]):
                nums[i] = color
                i += 1

        