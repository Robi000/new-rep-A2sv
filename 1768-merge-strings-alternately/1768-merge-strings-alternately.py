class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        minWord = min([word1, word2] , key=len)
        str = ""
        count = 0
        while count < len(minWord):
            str += word1[count]
            str += word2[count]
            count += 1
        str += word1[count:]
        str += word2[count:]
        return str
