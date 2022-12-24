class Solution(object):
    def isAlienSorted(self, words, order):
        letHash = {}
        for leng in range(len(order)):
            letHash[order[leng]] = leng
        # print(letHash)

        index = 1
        while index < len(words):
            str = min(words[index-1: index+1], key=len)
            for count in range(len(str)):
                if letHash[words[index-1][count]] > letHash[words[index][count]]:
                    return False
                if letHash[words[index-1][count]] < letHash[words[index][count]]:
                    break
            else:
                if len(words[index-1]) > len(words[index]):
                    return False
            index += 1
        return True 