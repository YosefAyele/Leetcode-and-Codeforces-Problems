class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                indegree[recipes[i]] += 1
        
        queue = deque()
        for sup in supplies:
            queue.append(sup)
        
        res = []
        while queue:
            ing = queue.popleft()
            
            for child in graph[ing]:
                indegree[child] -= 1
                if not indegree[child]:
                    res.append(child)
                    queue.append(child)
                    
        return res
                
        
        