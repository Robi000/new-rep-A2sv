class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        str = ""
        # print(str)

        index = 0
        while index < len(command):
            if command[index] != "(":
                str += command[index]
                index += 1
            else:
                if command[index + 1] == ")":
                    str += "o"
                    if index + 2 < len(command):
                        index += 2
                    else:
                        break
                else:
                    str += "al"
                    if index + 4 < len(command):
                        index += 4
                    else:
                        break

        return(str)

