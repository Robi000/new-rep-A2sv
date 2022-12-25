class Solution(object):
    def mather(self , arr, num, ind):
        tenth = num//10
        first = num % 10
        arr[ind] = arr[ind] + first
        if arr[ind] > 9:
            arr[ind+1] += 1
            arr[ind] = arr[ind] % 10
        arr[ind + 1] = arr[ind + 1] + tenth
        if arr[ind + 1] > 9:
            arr[ind+2] += 1
            arr[ind + 1] = arr[ind + 1] % 10
        return arr
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0"== num2 or num1== "0":
            return "0"
        len1 = len(num1)
        len2 = len(num2)
        length = len1 + len2
        revAns = [0]*length
        for i in range(len1 - 1, -1, -1):
            numB = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                start = len1-i + len2-j - 2
                numT = int(num2[j])
                # print(revAns, start)
                revAns = self.mather(revAns, numB * numT, start)
        ans = ""
        flag = 0
        length = length-1
        while length > -1:
            if revAns[length] == 0 and flag == 0:
                pass
            else:
                ans += str(revAns[length])
                flag = 1
            length -= 1

        return(ans)
