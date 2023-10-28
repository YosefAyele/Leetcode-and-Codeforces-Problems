class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        line = defaultdict(int)

        for birth,death in logs:
            line[birth] += 1
            line[death] -= 1
        
        sorted_dates = sorted(line.items())

        running_sum = 0
        max_population = 0
        max_population_year = logs[0][0]
        
        for year,count in sorted_dates:

            running_sum += count
            if running_sum > max_population:
                max_population_year = year
                max_population = running_sum
        
        return max_population_year