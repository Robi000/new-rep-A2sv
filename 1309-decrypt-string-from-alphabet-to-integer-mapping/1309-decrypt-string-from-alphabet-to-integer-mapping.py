class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        _ASCI = {}
        string = ""
        for idx, i in enumerate(list(range(96, 123))):
            _ASCI[str(idx)] = chr(i)
        # print(_ASCI)
        for i in range(len(s)):
            if s[i] != "#":
                string += _ASCI[s[i]]
            else:
                string = string[:-2]
                string += _ASCI[s[i-2:i]]
        return (string)