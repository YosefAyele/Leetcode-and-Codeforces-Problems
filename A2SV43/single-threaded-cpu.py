class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new_arr=[[val[0],val[1],i] for i,val in enumerate(tasks)]
        new_arr.sort()

        heap = []

        i = 1
        time = new_arr[0][0] + new_arr[0][1]
        res = [new_arr[0][2]]

        while i < len(tasks) or heap:

            while i < len(tasks) and new_arr[i][0] <= time:
                start,duration,idx = new_arr[i]
                heapq.heappush(heap,[duration,idx])
                i += 1
            if heap:
                duration,idx = heapq.heappop(heap)
                res.append(idx)
                time += duration
            else:
                time = new_arr[i][0]
                
        return res


        