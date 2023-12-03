class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        all_players = set()

        for winner,loser in matches:
           all_players.add(winner)
           all_players.add(loser)
           indegree[loser] += 1
        never_lose = []
        once_lose = []
        
        for player in all_players:
            if indegree[player] == 0:
                never_lose.append(player)
            elif indegree[player] == 1:
                once_lose.append(player)

        never_lose.sort()
        once_lose.sort()

        return [never_lose,once_lose]
        
        




