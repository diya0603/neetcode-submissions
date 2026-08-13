class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for s in strs:
            l=len(s)
            string+=str(l)+'#'+s
        print(string)
        return string
            

    def decode(self, s: str) -> List[str]:
        out=[]
        i=0
        while i<len(s):
            word_len=""
            while s[i]!='#':
                word_len+=s[i]
                i+=1
            word_len = int(word_len)
            word=""
            
            for j in range(i+1,i+word_len+1):
                word+=s[j]
            out.append(word)
            i=i+word_len+1
        return out

