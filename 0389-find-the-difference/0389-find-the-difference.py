class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for x in t:
            if s.count(x) < t.count(x):
                return x