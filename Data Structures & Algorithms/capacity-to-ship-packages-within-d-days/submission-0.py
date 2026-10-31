class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        answer = high
        while low <= high:
            mid = (low + high) // 2

            days_needed = 1
            current = 0

            for w in weights:
                if current + w > mid:
                    days_needed += 1
                    current = 0
                current += w
            
            if days_needed <= days:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
                