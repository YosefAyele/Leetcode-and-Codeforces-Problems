class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # two pass solution
        # first find the O's which are unflippable
        # then capture all the O's which are not unflippable
        
        def inbound(r,c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        unflippables = set()
        visited = set()
        
        def dfs(r,c):
            
            # if board[r][c] == "O":
            unflippables.add((r,c))
            visited.add((r,c))
            
            for x, y in directions:
                next_r = r + x
                next_c = c + y
                if inbound(next_r,next_c) and (next_r,next_c) not in visited and board[next_r][next_c] == "O":
                    dfs(next_r,next_c)
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                neighbours = 0
                for x,y in directions:
                    r_next = row + x
                    c_next = col + y
                    if inbound(r_next,c_next):
                        neighbours += 1
                if neighbours < 4 and board[row][col] == "O":
                    dfs(row,col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row,col) not in unflippables:
                    board[row][col] = "X"
            
        
        
                
                    
            
        
        
        
        