class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        
        tickets_deque = deque([(tickets[i],i) for i in range(len(tickets))])
        
        
        res = 0
        
        while tickets_deque:
            
            curr = tickets_deque[0]
            res += 1
       
            bought = (curr[0]-1,curr[1])
            tickets_deque.popleft()
            
            if bought[0]:
                tickets_deque.append(bought)
            if bought[1] == k and bought[0] == 0:
                return res
            
            
            
            
            
        return res