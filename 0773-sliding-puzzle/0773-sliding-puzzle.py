class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        goal = [1,2,3,4,5,0]
        
        curr = board[0] + board[1]
        start = curr.index(0)
        
        dirs = {0:[1,3], 1:[0,2,4],2:[1,5],3:[0,4],4:[3,5,1],5:[4,2]}
        
        queue = deque()
        visited = set()
        queue.append((curr,start,0))
        visited.add(tuple(curr))
        while queue:
            curr_board, start,step = queue.popleft()
            
            if curr_board == goal:
                return step
            for neigh in dirs[start]:
                new = curr_board.copy()
                new[start],new[neigh] = new[neigh], new[start]
                
                if tuple(new) not in visited:
                    queue.append((new,neigh,step + 1))
                    visited.add(tuple(new))
                    
                    
        return -1
                    
        
            