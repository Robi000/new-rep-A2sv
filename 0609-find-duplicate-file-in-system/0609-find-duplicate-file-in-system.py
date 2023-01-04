class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        dic {
        content: [fullpath , fullpath2]
        }
        
        return for len(dic[key]) > 2
        """
        dic = {}
        for path in paths:
            splited = path.split()
            splited[0] += "/"
            for i in range(1 , len(splited)):
                open = splited[i].index("(") + 1
                closee = splited[i].index(")") 
                cont = splited[i][open:closee]
                dirct = splited[0] + splited[i][:open -1]
                x = dic.get(cont , [])
                x.append(dirct)
                dic[cont] = x
        ans = []
        for value in dic.values():
            if len(value) > 1:
                ans.append(value)
        return(ans)

        