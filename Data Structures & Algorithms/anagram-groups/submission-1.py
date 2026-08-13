from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for word in strs:
            m["".join(sorted(word))].append(word)

        return list(m.values())
            
