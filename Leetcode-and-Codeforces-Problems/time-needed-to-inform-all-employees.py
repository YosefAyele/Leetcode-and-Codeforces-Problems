class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for employee,manager in enumerate(manager):
            graph[manager].append(employee)

        queue = deque()
        queue.append((headID,0))

        ans = 0
        while queue:
            manager,minutes = queue.popleft()
            ans = max(minutes,ans)

            for employee in graph[manager]:
                queue.append((employee,minutes + informTime[manager]))
        
        return ans
