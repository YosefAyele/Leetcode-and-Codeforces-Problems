class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        
        queue = deque()
        queue.append(("0000", 0))
        visited = set(["0000"])
        
        
        while queue:
            
            curr,step = queue.popleft()
            if curr in deadends:
                continue
            if curr == target:
                return step
            
            for i in range(4):
                new1 = curr[:i] + str((int(curr[i]) + 1)%10) + curr[i+1:]
                new2 = curr[:i] + str((int(curr[i]) - 1)%10) + curr[i+1:]
                
                if new1 not in visited:
                    queue.append((new1,step + 1))
                    visited.add(new1)
                if new2 not in visited:
                    queue.append((new2,step + 1))
                    visited.add(new2)
        return -1
                
                
            
            
                
                
            
        