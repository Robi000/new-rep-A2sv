class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        x = min(strs, key=len)
        new = ""
        flag = 0
        for y in range(len(x)):
            
            if flag != 0:
                break
            for m in strs:
                if m[y] != x[y]:
                    flag = 1
                    break
            else:
                new = new + x[y]
            
        return new

            
            
        