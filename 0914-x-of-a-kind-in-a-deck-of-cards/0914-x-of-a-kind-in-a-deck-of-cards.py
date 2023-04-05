class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcd(n1,n2):
            if not n2:
                return n1
            return gcd(n2,n1%n2)
        
        counts = Counter(deck)
        gcd_val = counts[deck[0]]
        for num in counts:
            gcd_val = gcd(gcd_val,counts[num])
        
        return gcd_val > 1