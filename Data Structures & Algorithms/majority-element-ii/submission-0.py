class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        threshold = len(nums) //3
        result = []
        for num, count in counts.items():
            if count > threshold:
                result.append(num)
        return result