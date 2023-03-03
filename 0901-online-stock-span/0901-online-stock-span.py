class StockSpanner:

    def __init__(self):
        
        self.stockSpan = []

    def next(self, price: int) -> int:
        
        span = 1
        
        while self.stockSpan and price >= self.stockSpan[-1][0]:
            span += self.stockSpan.pop()[1]
        
        self.stockSpan.append((price,span))
        return span 
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)l