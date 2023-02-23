class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        n, m = len(self.mat), len(self.mat[0])
        self.prefixGrid = [[0]*(m+1) for _ in range(n+1)]
        
        
        for row in range(1,n+1):
            for col in range(1,m+1):
                self.prefixGrid[row][col] = self.prefixGrid[row-1][col] + self.prefixGrid[row][col-1] + self.mat[row-1][col-1] - self.prefixGrid[row-1][col-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.prefixGrid[row2+1][col2+1] - self.prefixGrid[row1][col2+1] - self.prefixGrid[row2+1][col1] + self.prefixGrid[row1][col1]

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)