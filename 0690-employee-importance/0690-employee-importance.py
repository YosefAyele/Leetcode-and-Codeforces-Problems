"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
            ans = 0
            visited = set()
            
            employees_dict = {employee.id:employee for employee in employees}
            ans = 0
            def dfs(node):
                
                nonlocal ans
                ans += node.importance
                visited.add(node)
                for child in node.subordinates:
                    if child not in visited:
                        dfs(employees_dict[child])
                
                # return ans + node.importance
            
            dfs(employees_dict[id])
            
            return ans
                    
            
                