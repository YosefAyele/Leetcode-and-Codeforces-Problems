class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = defaultdict(list)
        
        self.parent = parent
        for i,p in enumerate(parent):
            if p != -1:
                self.graph[p].append(i)
            
        self.locker = [-1]*len(self.parent)

        
    def lock(self, num: int, user: int) -> bool:
        if self.locker[num] != -1:
            return False
        self.locker[num] = user
        return True
    
    def unlock(self, num: int, user: int) -> bool:
        if self.locker[num] != user:
            return False
        self.locker[num] = -1
        return True
    def upgrade(self, num: int, user: int) -> bool:
        if self.locker[num] != -1: 
            return False # check for unlocked
        
        node = num
        while node != -1: 
            if self.locker[node] != -1: 
                break # locked ancestor
            node = self.parent[node]
        else: 
            stack = [num]
            descendant = []
            while stack: 
                node = stack.pop()
                if self.locker[node] != -1: descendant.append(node)
                for child in self.graph[node]: stack.append(child)
            if descendant: 
                self.locker[num] = user # lock given node 
                for node in descendant: self.locker[node] = -1 # unlock all descendants
                return True 
        return False # locked ancestor
        
    
        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)