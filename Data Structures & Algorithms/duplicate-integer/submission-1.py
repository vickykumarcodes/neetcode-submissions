class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dictionary
        d = dict()
        for k in nums:
            if k in d.keys():
                d[k] += 1
                if d[k] > 1:
                    return True
            else:
                d[k] = 1
        return False
        
