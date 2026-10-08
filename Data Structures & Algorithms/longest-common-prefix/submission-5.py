class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_word = min(strs, key=len) # min len string

        for _ in range(len(min_len_word)):
            for word in strs:
                if not word.startswith(min_len_word):
                    min_len_word = min_len_word[:-1]
                    break
        return min_len_word
            

        first_word = strs[0]
        lcp = ''
        check_all = True
        for i, c in enumerate(first_word):
            for word in strs:
                if word[i] != c:
                    check_all = False

            if check_all == False:
                return lcp
            else:
                lcp += c