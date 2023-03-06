class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.times = times
        self.persons = persons
        
        #caculate winner at index
        self.winnerAtIndex = []
        votesCount = {}
        maxVote = 0
        winner = persons[0]
        for person in persons:
            votesCount[person] = votesCount.get(person,0) + 1
            
            if votesCount[person] >= maxVote:
                winner = person
                maxVote = votesCount[person]
            self.winnerAtIndex.append(winner)
            
        

    def q(self, t: int) -> int:
        
        
        # find the index where the given t is greater
        
        low = -1
        high = len(self.times)
        
        while high > low + 1:
            
            mid = low + (high - low)//2
            
            curr = self.times[mid]
            
            if curr > t:
                high = mid
            else:
                low = mid
        
        idx = low
            
        
        return self.winnerAtIndex[idx]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)