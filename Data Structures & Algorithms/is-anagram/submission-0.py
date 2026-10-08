from collections import Counter

def manual_counter(s):
    d = dict()
    for k in s:
        d[k] = d.get(k, 0) + 1
    return d

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return (Counter(s) == Counter(t))
        return (manual_counter(s) == manual_counter(t))