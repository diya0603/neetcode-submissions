class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        res=0
        for n in nums:
            if n-1 not in nums:
                count=0
                curr=n
                while curr in nums:
                    count+=1
                    curr+=1
                res=max(res, count)
        return res


        