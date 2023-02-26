class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = 0
        for x in range(len(arr)-1):
            if x == 0:
                diff = arr[x+1] - arr[x]
            else:
                if diff != arr[x+1] - arr[x]:
                    return False
                
        return True
                
            
        
        
        