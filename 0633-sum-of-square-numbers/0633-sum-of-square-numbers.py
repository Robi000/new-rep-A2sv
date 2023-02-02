class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low , high = 0 , int(sqrt(c)) +1
        while low <= high:
            power = low **2 + high ** 2
            if power > c:
                high -= 1
            elif power < c:
                low += 1
            else:
                return True
        return False