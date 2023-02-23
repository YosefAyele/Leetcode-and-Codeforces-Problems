class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(t_count, curr):
            for t_ch in t_count:
                if not t_ch in curr or curr[t_ch] < t_count[t_ch]:
                    return False
            return True
        
        t_count = Counter(t)
        curr = {}
        
        min_length = len(s) + 1
        left_bound, right_bound = -1, -1
        left = 0
        s_len = 0
        for right, letter in enumerate(s):
            
            curr[letter] = curr.get(letter,0) + 1
            while check(t_count, curr):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    left_bound = left 
                    right_bound = right
                    
                curr[s[left]] -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left += 1
            
            
            # print(left_bound,right_bound)
                
        
        return s[left_bound:right_bound+1]
        
   