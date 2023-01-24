class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        leng = len(arr)
        ans = [0] * leng
        leng = leng -2
        ans[-1] = -1
        while leng >= 0:
            ans[leng] = max(ans[leng+1] , arr[leng+1])
            leng -= 1
        return ans
            
            
        