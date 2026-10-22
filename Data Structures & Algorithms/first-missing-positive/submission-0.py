class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)

        candidate = 1
        while candidate in s:
            candidate += 1

        return candidate