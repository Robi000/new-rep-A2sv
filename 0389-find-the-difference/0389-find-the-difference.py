class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if len(s) == 0:
            return t
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]