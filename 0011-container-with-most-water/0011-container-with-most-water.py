class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) -1
        ans = 0
        while i < j:
            # print(i , j)
            if height[i] >= height[j]:
                ans = max( ans , (j-i) * height[j])
                j -= 1
            else:
                ans = max( ans , (j-i) * height[i])
                i += 1
                
        return ans 