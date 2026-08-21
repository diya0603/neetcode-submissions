class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ele=float('inf')
        def bin_search(nums,l,r):
            if l==r:
                return nums[l]
            mid =  l + (r - l) // 2
            
            if nums[mid]>nums[r]:
                return bin_search(nums,mid+1,r)
            else:
                return bin_search(nums,l,mid)
            
        return bin_search(nums,0,len(nums)-1)