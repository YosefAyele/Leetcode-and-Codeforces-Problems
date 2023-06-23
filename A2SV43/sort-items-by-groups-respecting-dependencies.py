class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        indegree_items = []
        items = defaultdict(list)
        group_dep = defaultdict(list)
        
        for i,g in enumerate(group):
            if g == -1:
                group[i] = m
                m += 1
        
        indegree_groups = [0]*m
                
        for i,befores in enumerate(beforeItems):
            indegree_items.append(len(befores))
            for j in befores:
                items[j].append(i)
                if group[i] != group[j]:
                    group_dep[group[j]].append(group[i])
                    indegree_groups[group[i]] += 1
        
        # queue for sorting items within their own groups
        queue = deque()
        for i,degree in enumerate(indegree_items):
            if degree == 0:
                queue.append(i)
                
        resGroup = defaultdict(list)

        while queue:
            item = queue.popleft()
            resGroup[group[item]].append(item)
                 
            for child in items[item]:
                indegree_items[child] -= 1
                if indegree_items[child] == 0:
                    queue.append(child)
        
        output = []
        # now populate final output answer by sorting groups
        queue_g = deque()
        for i,deg in enumerate(indegree_groups):
            if deg == 0:
                queue_g.append(i)
        while queue_g:
            g = queue_g.popleft()
            output.extend(resGroup[g])
            
            for child in group_dep[g]:
                indegree_groups[child] -= 1
                if indegree_groups[child] == 0:
                    queue_g.append(child)
        # print(output) 
        if len(output) == n:
             return output
        return []
                
            
        
                
            
        
            
            