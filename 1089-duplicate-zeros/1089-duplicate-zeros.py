class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr)-1:
            if arr[i] == 0:
                arr.insert(i , 0)
                arr. pop()
                i = i+1
            i += 1
        
                