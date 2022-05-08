"""
we can group the anagrams using hashing. just hash the letters and then make them the keys.
since these are lettes we can use bit array with 26 bits as the .

easier would be the sorting. sorting can be done in O(n) using count sort.

"""

import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort(word):
            chars = string.ascii_lowercase
            mapping = {ch: i for i, ch in enumerate(chars)}
            counts = [0] * len(chars)
            for ch in word:
                counts[mapping[ch]] += 1
            build = []
            for i, c in enumerate(counts):
                if c > 0:
                    ch = chars[i]
                    build.append(ch * c)
            build = build[::-1]
            return "".join(build)
        
        groups = {}
        for word in strs:
            sw = sort(word)
            # sw = "".join(sorted(word))
            if sw not in groups:
                groups[sw] = [word]
            else:
                groups[sw].append(word)
        return list(groups.values())