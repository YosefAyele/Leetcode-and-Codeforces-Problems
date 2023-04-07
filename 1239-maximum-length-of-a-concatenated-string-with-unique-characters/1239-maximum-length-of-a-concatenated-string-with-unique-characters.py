class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def getBinary(word):
            binary = 0
            
            for letter in word:
                mask = ord(letter) - 97
                shift = 1 << mask
                if binary & shift:
                    return False
                binary |= shift
            
            return binary
        binArr = [getBinary(word) for word in arr]
        
        res = 0
        def backtrack(idx,mask,length):
            nonlocal res
            if idx == len(arr):
                return 
            # not include
            backtrack(idx+1,mask, length)
            
            if not binArr[idx]:
                return
            # include
            if mask & binArr[idx] == 0:
                length += len(arr[idx])
                mask |= binArr[idx]
                
                res = max(res,length)
                backtrack(idx + 1, mask, length)
                
                length -= len(arr[idx])
                mask &= binArr[idx]
                
        backtrack(0,0,0)
        
        return res
        
                    
                    
                    
                    
                    
                    
                
        