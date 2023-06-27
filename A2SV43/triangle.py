class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
             # recursive
        
        m = len(triangle)
        
        @cache
        def dp(row,col):
            
            
            if row == m-1:
                
                if col <= m-1:
                    return triangle[row][col]
                return inf
            
            if row >= m:
                return inf

            down = dp(row+1,col)
            down_right = dp(row+1,col+1)
            
            return  triangle[row][col] + min(down_right,down)
        
        return dp(0,0)
        