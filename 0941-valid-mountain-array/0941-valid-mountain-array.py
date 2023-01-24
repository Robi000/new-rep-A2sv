class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increasing = True
        for i in range(1,len(arr)):
            if arr[i] == arr[i -1]:
                return False
            if increasing and arr[i] < arr[i-1]:
                increasing = False
            if i == 1 and increasing == False:
                return False
            if not increasing and arr[i] > arr[i-1]:
                return False
        if increasing:
            return False
        return True
                
        