class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque()
        visited = set()
        
        queue.append((0,1,0))
        visited.add((0,1))
        
        while queue:
            position, speed, step = queue.popleft()
            # print(position)
            if position == target:
                return step
            
            if position + speed not in visited:
                #execute A
                queue.append((position + speed,speed*2,step +1))
                visited.add((position + speed,speed))
            #execute R
            if speed > 0:
                speed = -1
            else:
                speed = 1
            if (position,speed) not in visited:
                visited.add((position,speed))
                queue.append((position,speed,step + 1))
                
                
            
            

            
        