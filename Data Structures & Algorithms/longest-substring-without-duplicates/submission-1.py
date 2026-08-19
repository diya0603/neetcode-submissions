from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        longest =0
        index_map=defaultdict(int)
        while r<len(s):
            if s[r] in index_map:
                l=max(l,index_map[s[r]]+1)
            index_map[s[r]]=r
            longest=max(longest,r-l+1)
            r+=1
        return longest    
            