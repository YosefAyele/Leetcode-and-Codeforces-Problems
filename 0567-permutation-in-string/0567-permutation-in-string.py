class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        curr = {}
        s1_count = Counter(s1)
        left = 0
        
        for right, letter in enumerate(s2):
            
            curr[letter] = curr.get(letter,0) + 1
            
            if right - left + 1 == len(s1):
                
                if s1_count == curr:
                    return True
                curr[s2[left]] -= 1
                if curr[s2[left]] == 0:
                    del curr[s2[left]]
                left += 1
                
        return False
                
            
        
        