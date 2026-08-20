class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return t
        t_map={}
        for c in t:
            t_map[c]=1+t_map.get(c,0)
        need=len(t_map)
        s_map={}
        best_l,best_r=0,len(s)-1
        min_len =float('inf')
        l=0
        have =0
        for r in range(len(s)):
            if s[r] in t_map:
                s_map[s[r]]=1+s_map.get(s[r],0)
                if s_map[s[r]]==t_map[s[r]]:
                    have+=1
                if need==have:
                    
                    while need==have:
                        if r-l+1 < min_len:
                            best_l=l
                            best_r=r
                            min_len = r-l+1
                        if s[l] in s_map:
                            s_map[s[l]]-=1
                            if s_map[s[l]]<t_map[s[l]]:
                                have-=1
                        l+=1
            
        if min_len==float('inf'):
            return ""
        else:
            return s[best_l:best_r+1]


            


