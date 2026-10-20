class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: an array of size 0 or 1 is already sorted
        if len(nums) <= 1:
            return nums
        
        # Helper function to merge two sorted lists
        def merge(A: List[int], B: List[int]) -> List[int]:
            m, n = len(A), len(B)
            C, i, j = [], 0, 0
            
            # Case 1: Compare elements from both lists
            while i < m and j < n:
                if A[i] <= B[j]:
                    C.append(A[i])
                    i += 1
                else:
                    C.append(B[j])
                    j += 1
                    
            # Case 2: Append remaining elements of A
            while i < m:
                C.append(A[i])
                i += 1
                
            # Case 3: Append remaining elements of B
            while j < n:
                C.append(B[j])
                j += 1
                
            return C 

        # Split the array into two halves recursively
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # Merge the sorted halves and return
        return merge(left_half, right_half)