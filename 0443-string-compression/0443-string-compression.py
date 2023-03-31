from collections import Counter
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        index=left=0
        
        while left<len(chars):
            
            right=left
            
            while right<len(chars) and chars[left]==chars[right]:
                right+=1
            chars[index]=chars[left]
            index+=1
            
            if right-left>1:
                for c in str(right-left):
                    chars[index]=c
                    index+=1
            left=right
        return index