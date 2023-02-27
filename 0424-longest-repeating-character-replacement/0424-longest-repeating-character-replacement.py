class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        maxLen = 0
        window = {}
        
        def changes(counter):
            max_count = 0
            
            total_count = 0
            for i in counter:
                total_count += counter[i]
                max_count = max(max_count,counter[i])
            return total_count - max_count
            
        
        for right,letter in enumerate(s):
            
                window[letter] = window.get(letter,0) + 1
                
                while changes(window) > k:
                    window[s[left]] -= 1
                    
                    if not window[s[left]]:
                        del window[s[left]]
                    left += 1
                
                maxLen = max(maxLen,right - left + 1)
            
        
        return maxLen
    
    