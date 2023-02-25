class Solution:
    def carFleet(self, tar: int, position: List[int], sp: List[int]) -> int:
        positions=[[position[i],sp[i]] for i in range(len(position))]
        positions.sort(reverse=True)

        monstack=[]
        
        for place,time in positions:
            
            currtime=(tar-place)/time
            
            
            if monstack and currtime<=monstack[-1]:
                currtime=monstack.pop()
            
            monstack.append(currtime)
        return len(monstack)
            