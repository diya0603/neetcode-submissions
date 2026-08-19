from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map=defaultdict(int)
        l,r=0,0
        max_char=0
        longest=0
        while r<len(s):
            char_map[s[r]]+=1
            max_char=max(max_char, char_map[s[r]])

            while (r-l+1)-max_char>k:
                char_map[s[l]]-=1
                l+=1
            longest=max(longest,r-l+1)
            r+=1

        return longest    


