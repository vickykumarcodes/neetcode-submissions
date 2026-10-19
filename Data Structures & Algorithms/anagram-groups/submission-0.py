class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make an empty dict: key -> list of words
        anagram_map = {}
        # for each word:
        for word in strs:
        #   build the key(sorted letters, joined into a string)
            key = ''.join(sorted(word))
        #   add the word to the list for that key
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)
        # return all the lists
        return list(anagram_map.values())
