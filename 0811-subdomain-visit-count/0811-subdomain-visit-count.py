class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for domain in cpdomains:
            domain = domain.split()
            pairs = domain[1].split(".")
            # print(domain , pairs)
            upto = ""
            for i in range(len(pairs)-1 , -1 , -1):
                if i == len(pairs)-1:
                    upto = pairs[i]
                else:
                    upto = pairs[i]+"."+upto
                dic[upto] = dic.get(upto , 0) + int(domain[0])
        ans = []
        for key , val in dic.items():
            ans.append(str(val) + " " + key)
            
        return(ans)
        