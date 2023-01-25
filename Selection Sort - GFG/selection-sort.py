#User function Template for python3

class Solution: 
    def select(self, arr, i):
        j = i +1
        while j < len(arr):
            if arr[j] < arr[i]:
                i = j
            j += 1
        return i
    
    def selectionSort(self, arr,n):
        i = 0 
        while i < n:
            ind = self.select(arr , i)
            arr[i],arr[ind] = arr[ind], arr[i]
            i += 1
        
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends