from collections import Counter as c
from math import comb
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        power = set([2**x for x in range(50)])
        x = c(deliciousness)
        y = set(deliciousness)
        check = y.copy()
        ans = 0
        for dec in y:
            for po in power:
                other = po - dec
                if other in check:
                    if other == dec:
                        ans += comb(x[dec] , 2)
                    else:
                        ans += x[dec] * x[other]
            check.remove(dec)
                        
        return  (ans % 1000_000_007)
                        
                        
                    
        
                        
                
            
        