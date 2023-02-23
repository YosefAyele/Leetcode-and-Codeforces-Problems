class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations ={}
        
        for passengers,start,end in trips:
            locations[start] = locations.get(start,0) + passengers
            locations[end] = locations.get(end,0) - passengers
        
        currTotal = 0
        for trip in sorted(locations):
            currTotal += locations[trip]
            
            if currTotal > capacity:
                return False
        
        return True
            