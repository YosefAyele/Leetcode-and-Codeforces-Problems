class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(curr,stt):
            
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in list(stt):
                curr.append(num)
                
                stt.remove(num)
                
                backtrack(curr,stt)
                
                curr.pop()
                stt.add(num)
            return 
        
        backtrack([],set(nums))
        
        return res
            