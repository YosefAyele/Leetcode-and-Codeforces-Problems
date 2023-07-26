class MedianFinder:

    def __init__(self):
        self.smheap = []
        self.lgheap = []
        heapq.heapify(self.smheap)
        heapq.heapify(self.lgheap)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smheap,-num)
        if self.smheap and self.lgheap:
            currsmall = self.smheap[0]
            currlarge = self.lgheap[0]  
            if -currsmall > currlarge:
                heapq.heappush(self.lgheap,-currsmall)
                heapq.heappop(self.smheap)
        if len(self.smheap) - len(self.lgheap) > 1:
            curr = - heapq.heappop(self.smheap)
            heapq.heappush(self.lgheap,curr)
        if len(self.lgheap) - len(self.smheap) > 1:
            curr = heapq.heappop(self.lgheap)
            heapq.heappush(self.smheap,-curr)

    def findMedian(self) -> float:
        if len(self.smheap) > len(self.lgheap):
            ans = -heapq.heappop(self.smheap)
            heapq.heappush(self.smheap,-ans)
        elif len(self.lgheap) > len(self.smheap):
            ans = heapq.heappop(self.lgheap)
            heapq.heappush(self.lgheap,ans)
        else:
            num1 = heapq.heappop(self.smheap)
            num2 = heapq.heappop(self.lgheap)

            ans = (-num1 + num2)/2

            heapq.heappush(self.smheap,num1)
            heapq.heappush(self.lgheap,num2)
        return ans

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

'''
-4 -5 -6 6 8 10
'''
