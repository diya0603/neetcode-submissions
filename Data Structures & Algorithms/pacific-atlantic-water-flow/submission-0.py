
class Solution:
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific=[[False]*cols for _ in range(rows)]
        atlantic=[[False]*cols for _ in range(rows)]
        out =[]
        def dfs(reach,h,r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if reach[r][c]:
                return
            
            if heights[r][c]>=h:
                reach[r][c] = True
                dfs(reach,heights[r][c],r-1,c)
                dfs(reach,heights[r][c],r+1,c)
                dfs(reach,heights[r][c],r,c+1)
                dfs(reach,heights[r][c],r,c-1)
            return
        
        
        r=0
        for c in range(cols):
            dfs(pacific,heights[r][c],r,c)
        c=0
        for r in range(rows):
            dfs(pacific,heights[r][c],r,c)
        r=rows-1
        for c in range(cols):
            dfs(atlantic,heights[r][c],r,c)
        c=cols-1
        for r in range(rows):
            dfs(atlantic,heights[r][c],r,c)

        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    out.append([r,c])
        return out 
            