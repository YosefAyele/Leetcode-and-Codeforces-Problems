class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def inbound(x,y):
            return 0 <= x < len(image)  and 0 <= y < len(image[0])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        def dfs(r,c):
            prev = image[r][c]
            image[r][c] = color
            visited.add((r,c))
            
            for x,y in directions:
                new_row = r + x
                new_col = c + y
                
                if inbound(new_row,new_col) and image[new_row][new_col] == prev and (new_row,new_col) not in visited:
                    dfs(new_row,new_col)
                    
        dfs(sr,sc)
        
        return image
            