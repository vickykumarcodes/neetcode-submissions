class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #count = 0
        #for start in range(len(nums)):
        #    total = 0
        #    for end in range(start, len(nums)):
        #        total += nums[end]
        #        if total == k:
        #            count += 1
        #return count

        seen = {0: 1}
        s = 0
        count = 0
        for num in nums:
            s += num
            count += seen.get(s-k, 0)
            seen[s] = seen.get(s, 0) + 1
        return count