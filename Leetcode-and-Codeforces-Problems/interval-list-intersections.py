class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        line = defaultdict(int)

        for start,end in firstList + secondList:
            line[start] += 1
            line[end+1] -= 1
        
        sorted_points = sorted(line.items())

        prefix = 0

        res = []
        for i in range(len(sorted_points)-1):
            point,count = sorted_points[i]

            prefix += count

            if prefix == 2:
                next_point = sorted_points[i+1][0]

                res.append([point,next_point-1])

        return res


        
