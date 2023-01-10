class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        ind = 0
        spaces = set(spaces)
        for ch in s:
            if ind in spaces:
                ans.append(" ")
            ans.append(ch)
            
            ind += 1
            
        return "".join(ans)
                