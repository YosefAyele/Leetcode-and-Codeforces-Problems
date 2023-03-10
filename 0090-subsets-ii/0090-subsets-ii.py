class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def collect(idx,currList):
            nonlocal res
            
            if idx == len(nums):
                curr = currList[:]

                res.append(curr)
                return
            
            
            # find the new index
            i = idx + 1
            newIdx = i
            
            # case2 is include the current number
            currList.append(nums[idx])
            collect(newIdx,currList)
            currList.pop()
            
            while i < len(nums) and nums[i] == nums[idx]:
                    i += 1
                    newIdx = i
                    
            
            # case1 is not to include the current number
            collect(newIdx,currList[:])

          
                
        collect(0,[])
        res.sort()
        
        return res
        
 