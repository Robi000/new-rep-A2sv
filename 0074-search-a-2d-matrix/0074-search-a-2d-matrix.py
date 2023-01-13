class Solution:
    def searchMatrix(self, martix: List[List[int]], target: int) -> bool:
        start = 0
        end = (len(martix)-1)*len(martix[0]) + len(martix[0])-1
        coll = len(martix[0])
        # i = 0
        while True:

            startr = start // coll
            startc = start % coll
            endr = end // coll
            endc = end % coll
            mid = (start + end)//2
            midr = mid // coll
            midc = mid % coll
            print(start , end , mid)
            
            if start == end-1 or start == end:
                if martix[startr][startc] == target or martix[endr][endc] == target:
                    return True
                return False
            if martix[startr][startc] == martix[endr][endc]:
                print(False)
                return False
            if martix[midr][midc] == target:
                print(True)
                return True
            elif martix[midr][midc]> target:
                end = mid
            else:
                start = mid
