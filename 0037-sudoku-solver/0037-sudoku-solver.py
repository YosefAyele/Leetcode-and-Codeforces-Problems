class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        
        empty = deque([])
        
        for row in range(9):
            for col in range(9):
                
                curr = board[row][col]
                
                if curr == ".":
                    empty.append([row,col])
                else:
                    rows[row].add(curr)
                    cols[col].add(curr)
                    box[(row//3,col//3)].add(curr)
        
        def backtrack():
            
            if not empty:
                return True
            
            r, c = empty[0]
             
            for i in range(1,10):
                val = str(i)

                if not ((val in rows[r]) or ( val in cols[c]) or  (val in box[(r//3,c//3)])):
                    
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    box[(r//3,c//3)].add(val)
                    empty.popleft()
                    
                    if backtrack():
                        return True
                  
                    board[r][c] = "."
                    rows[r].remove(val)
                    cols[c].remove(val)
                    box[(r//3,c//3)].remove(val)
                    empty.appendleft([r,c])
                
            return False
                
        backtrack()
        