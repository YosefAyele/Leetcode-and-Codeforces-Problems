class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        
        monQue = deque()
        
        numsSum = [0]+list(accumulate(nums))
        
        res = len(nums) + 1
        
        # print(numsSum)
        for i in range(len(nums)):
            
            num = numsSum[i]
            
            while monQue and num <= numsSum[monQue[-1]]:
                monQue.pop()
            
            
            monQue.append(i)
            
            while monQue and numsSum[monQue[-1] + 1]  - numsSum[monQue[0]]  >= k:
                
                left = monQue.popleft()
                
    
                res = min(i - left + 1,res)
          
            
        
        return res if res < len(nums) + 1 else -1