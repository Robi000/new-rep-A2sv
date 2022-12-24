from math import inf
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ind = -1
        minDis = inf
        for pts in points:
            
            if x == pts[0] or y == pts[1]:
                print("*")
                dis = abs(x-pts[0]) + abs(y-pts[1])
                print (dis)
                if minDis > dis :
                    minDis = dis
                    ind = points.index(pts)
                    
        return ind