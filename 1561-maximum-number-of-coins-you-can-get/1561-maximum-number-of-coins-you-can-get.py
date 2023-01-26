class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        x = len(piles)-1
        y = len(piles)
        
        while y > 0:
            print(x)
            ans += piles[x-1]
            x -= 2
            y -= 3


        return ans