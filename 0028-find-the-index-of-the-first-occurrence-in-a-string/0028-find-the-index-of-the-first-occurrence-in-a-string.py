class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while i < len(haystack) - len(needle) +1 :
            if haystack[i] == needle[j]:
                x = i
                while x < len(haystack) and j < len(needle):
                    if haystack[x] == needle[j]:
                        print(haystack[x], needle[j], end=" ")
                        x += 1
                        j+=1
                    else:
                        break
                print()
                if j == len(needle):
                    return i
                else:
                    j= 0
            i+= 1
        return -1