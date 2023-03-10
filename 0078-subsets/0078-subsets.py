class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []
        def collect(idx,currList):
            nonlocal res
            
            if idx == len(nums):
                res.append(currList[:])
                return
            
            
            
            # case1 is not to include the current number
            collect(idx+1,currList)

            # case2 is include the current number
            currList.append(nums[idx])
            collect(idx+1,currList)
            currList.pop()
                
        collect(0,[])
        
        return res
        
 