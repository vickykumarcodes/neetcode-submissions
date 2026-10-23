class Solution:
    def isPalindrome(self, s: str) -> bool:
        #cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        #return cleaned_str == cleaned_str[::-1]

        left, right = 0, len(s) - 1

        while left < right:
            # skip non alphanumeric chars form the left
            while left < right and not s[left].isalnum():
                left += 1
            # do same for right
            while left < right and not s[right].isalnum():
                right -= 1
            # compare characters
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True