class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        suffix=[0]*len(nums)
        prod_p=1
        for n in nums:
            prefix.append(prod_p)
            prod_p*=n
        prod_s=1
        for i in range(len(nums)-1,-1,-1):
            suffix[i]=prod_s
            prod_s*=nums[i]
        

        out=[]
        for i in range(len(nums)):
            out.append(prefix[i]*suffix[i])
        return out

