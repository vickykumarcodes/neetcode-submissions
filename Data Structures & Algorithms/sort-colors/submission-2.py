class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        first we initialize the counts [0, 0, 0] then we loop through nums to count  the nums for ex: nums = [1, 0, 1, 2] -> counts = [1, 2, 1]. then we can run another loop that will give the output [0, 1, 1, 2]
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] +=1 
        i = 0
        for color in range(3):
            for c in range(counts[color]):
                nums[i] = color
                i += 1


        