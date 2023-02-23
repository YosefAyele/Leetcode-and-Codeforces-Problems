class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        prefixGrid = [[0]*(m+1) for _ in range(n+1)]
        
        for row in range(1,n+1):
            for col in range(1,m+1):
                prefixGrid[row][col] = prefixGrid[row-1][col] + prefixGrid[row][col-1] + mat[row-1][col-1] - prefixGrid[row-1][col-1]
        
        
        res = [[0]*m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                left = max(0,col - k)
                right = min(m,col + k+1)
                
                top = max(0,row - k)
                bottom = min(n,row + k+1) 
                
                res[row][col] = prefixGrid[bottom][right] - prefixGrid[top][right] - prefixGrid[bottom][left] + prefixGrid[top][left]
        return res
            
                
            