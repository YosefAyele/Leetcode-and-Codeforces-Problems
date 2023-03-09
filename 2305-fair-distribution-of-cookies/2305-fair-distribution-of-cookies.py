class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        res = inf
        # @cache
        def fair(idx,kids):
            
            nonlocal res
            
            if idx == len(cookies):
                
                if min(kids) != 0 :
                    res = min(res,max(kids))
                # kids = [0]*k
                return
            if max(kids) >= res:
                return
            
            rem_kids = kids.count(0)
            rem_bags = len(cookies) - idx
            if rem_kids > rem_bags:
                return 
            for i in range(k):
                # change kids value
                
                kids[i] += cookies[idx]
                
                fair(idx+1,kids)
                
                kids[i] -= cookies[idx]
            
            
        fair(0,[0]*k)
        
        return res
    