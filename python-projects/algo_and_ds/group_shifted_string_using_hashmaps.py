"""

249. Group Shifted Strings

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

this looks like similar to the connected components problem

"""

from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strings:
            if len(string) < 2:
                groups[len(string)].append(string)
            else:
                if string[1] > string[0]:
                    groups[len(string)].append(string)
                else:
                    groups[-len(string)].append(string)
        return list(groups.values())


