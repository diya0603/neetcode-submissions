class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l=0
        r=len(heights)-1
        while l<r:
            h=min(heights[l],heights[r])
            max_area = max((r-l)*h, max_area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return max_area