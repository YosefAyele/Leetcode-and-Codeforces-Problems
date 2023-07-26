class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        heaps = defaultdict(list)

        for num in nums:
            if heaps[num-1]:
                heapq.heappush(heaps[num],heapq.heappop(heaps[num-1])+1)
            else:
                heapq.heappush(heaps[num],1)

        
        for heap in heaps.values():
            for num in heap:
                if num < 3:
                    return False
        return True


            
