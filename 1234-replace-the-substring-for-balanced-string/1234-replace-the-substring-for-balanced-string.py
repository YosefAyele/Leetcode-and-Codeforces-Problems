class Solution:
    def balancedString(self, s: str) -> int:
        
        counts = Counter(s)
        freq = len(s)//4
        new = {}
        
        for letter in counts:
            
            curr = counts[letter] - freq
            
            if curr > 0:
                new[letter] = curr
        if not new:
            return 0 
        def check(temp):
            
            for letter in new:
                if letter not in temp:
                    return False
                if new[letter] > temp[letter]:
                    return False
            return True
                
        left = 0
        temp = {}
        res = inf
        # print(new)
        for right,letter in enumerate(s):
            temp[letter] = temp.get(letter,0) + 1
            
            while check(temp):
                res = min(res,right - left + 1)
                temp[s[left]] -= 1
                if temp[s[left]] == 0:
                    del temp[s[left]]
                left += 1
                
        return res
        