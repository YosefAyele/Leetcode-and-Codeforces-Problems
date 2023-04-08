class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        directions = [[-1,0], [1,0],[0,-1],[0,1]]
        
        def isInbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col]:
                    for rowChange, colChange in directions:
                        newRow = row + rowChange
                        newCol = col + colChange
                        
                        if not isInbound(newRow,newCol) or not grid[newRow][newCol]:
                            res += 1
        return res
                        
                        
                        