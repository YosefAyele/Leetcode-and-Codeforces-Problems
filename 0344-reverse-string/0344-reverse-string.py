class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(left,right,s):
            
            if left >= right:
                return 
            
            s[left],s[right] = s[right], s[left]
            
            reverse(left+1,right-1,s)
        
        reverse(0,len(s)-1,s)
        