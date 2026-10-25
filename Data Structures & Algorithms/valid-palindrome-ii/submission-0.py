class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l, r) -> bool:
            # Helper to check if a substring is a perfect palindrome
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(l+1, r) or is_pal(l, r-1)
            l += 1
            r -= 1
        return True