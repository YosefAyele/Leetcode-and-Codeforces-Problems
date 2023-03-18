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
        temp = defaultdict(int)
        res = inf
        # print(new)
        for right,letter in enumerate(s):
            temp[letter] += 1
            
            while left <= right and all(temp[char] >= new[char] for char in new):
                res = min(res,right - left + 1)
                temp[s[left]] -= 1
                left += 1
                
        return res
        