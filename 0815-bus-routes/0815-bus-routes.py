class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0
        stopIdx = defaultdict(list)
        
        for i,route in enumerate(routes):
            for bus in route:
                stopIdx[bus].append(i)
        routes = [set(route) for route in routes]
        start = stopIdx[source]
        
        queue = deque()
        visited = set()
        
        for idx in start:
            queue.append((idx,1))
            visited.add(idx)
        while queue:
            
            idx,buses = queue.popleft()
            if target in routes[idx]:
                return buses
            
            for bus in routes[idx]:
                for i in stopIdx[bus]:
                    if i not in visited:
                        queue.append((i,buses + 1))
                        visited.add(i)
        return -1
            
                
            
        