class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # 1. Get length of the mountain array
        n = mountainArr.length()
        
        # 2. Find the peak index
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
                # The peak must be to the right of mid
            else:
                high = mid
                # mid could be the peak, or the peak is to the left
        peak = low
        
        # 3. Search the rising (increasing) side
        low = 0
        high = peak
        while low <= high:
            mid = (low + high) // 2
            value = mountainArr.get(mid)
            if value == target:
                return mid
            elif value < target:
                low = mid + 1
            else:
                high = mid - 1
                
        # 4. Search the falling (decreasing) side
        low = peak + 1
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            value = mountainArr.get(mid)
            if value == target:
                return mid
            elif value < target:
                high = mid - 1  
                # Since it's decreasing, larger values are to the left
            else:
                low = mid + 1   # Smaller values are to the right
                
        # 5. If nothing was found, return -1
        return -1