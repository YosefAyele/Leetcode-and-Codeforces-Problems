class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        
        left = 0
        res = 0
        for right,fruit in enumerate(fruits):
            
            window[fruit] = window.get(fruit,0) + 1
            
            while len(window) > 2:
                window[fruits[left]] -= 1
                
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                
                left += 1
            res = max(res,right - left + 1)
        
        return res