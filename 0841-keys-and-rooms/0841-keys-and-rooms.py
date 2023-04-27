class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque()
        queue.append(0)
        
        visited = set()
        while queue:
            
            length = len(queue)
            
            for _ in range(length):
                curr = queue.popleft()
                visited.add(curr)
                
                for child in rooms[curr]:
                    if child not in visited:
                        queue.append(child)
                        
        return len(visited) == len(rooms)
                