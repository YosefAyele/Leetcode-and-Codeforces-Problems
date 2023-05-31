class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = set([0])
        queue = deque()
        queue.append((0,0))
     
        ans = inf
        
        while queue:
            total, step = queue.popleft()
            if total == amount:
                ans = min(ans,step)
            elif total < amount:
                for coin in coins:
                    newtotal = total + coin
                    if newtotal not in seen:
                        queue.append((newtotal,step + 1))
                        seen.add(newtotal)
                        
        return ans if ans < inf else -1
                        
                        