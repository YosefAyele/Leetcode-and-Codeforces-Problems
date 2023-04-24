class ThroneInheritance:

    def __init__(self, kingName: str):
        self.isdead = defaultdict(int)
        self.throne = defaultdict(list)
        self.king = kingName
        
    def birth(self, parentName: str, childName: str) -> None:
        self.throne[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.isdead[name] = 1
        

    def getInheritanceOrder(self) -> List[str]:
        
        return self.dfs(self.king,[])
        
    def dfs(self,node,res):
        if not self.isdead[node]:
            res.append(node)
        for child in self.throne[node]:
            self.dfs(child,res)
        return res
        
        
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()