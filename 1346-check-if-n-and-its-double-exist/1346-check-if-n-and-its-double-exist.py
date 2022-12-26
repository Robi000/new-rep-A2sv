class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        check = set(arr)
        while i < len(arr):
            # print(float(arr[i] /2))
            if arr[i] * 2 in arr[i +1:] or arr[i] / 2 in arr[i+1:]:
                print(arr[i] ,arr[i] * 2 in arr[i +1:] ,arr[i] / 2, arr[i] / 2 in arr[i+1:]  )
                return True 
            i += 1
        return False