class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        nums = defaultdict(lambda:-1)
        n = len(board)
        l_r= True
        num = 1
        for i in range(n - 1,-1,-1):
            if l_r:
                for j in range(n):
                    if board[i][j] != -1:
                        nums[num] = board[i][j]
                    num += 1
                l_r = False
            else:
                for j in range(n - 1,-1 ,-1):
                    if board[i][j] != -1:
                        nums[num] = board[i][j]
                    num += 1
                l_r = True

        queue = deque()
        seen = set()
        queue.append((1,0))
        seen.add(1)
        
        while queue:
            node,step = queue.popleft()
            if node == n**2:
                return step
        
            for i in range(node + 1,min(node+7,n**2 + 1)):
                if i not in seen:
                    if nums[i] != -1:
                        queue.append((nums[i],step + 1))
                    else:
                        queue.append((i,step + 1))
                    seen.add(i)
        return -1
                    