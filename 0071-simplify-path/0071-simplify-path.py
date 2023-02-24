class Solution:
    def simplifyPath(self, path: str) -> str:
        
        directories = path.split("/")
        
        res = []
        
        print(directories)
        
        for directory in directories:
            if not directory or directory == ".":
                continue
            if directory == "..":
                if res: 
                    res.pop()
            else:
                res.append(directory)
        
        ans = "/" + "/".join(res)
        
        return ans