class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        whole_prod =1
        whole_prod_no_0 = 1
        count=0
        for n in nums:
            whole_prod*=n
            if n!=0:
                whole_prod_no_0*=n
            else:
                count+=1
        out=[]
        for n in nums:
            if n==0:
                if count==1:
                    out.append(int(whole_prod_no_0))
                else:
                    out.append(int(whole_prod))
            else:
                out.append(int(whole_prod/n))
        return out