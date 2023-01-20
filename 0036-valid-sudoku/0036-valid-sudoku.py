class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        drow = {}
        dcol = {}
        dsqr = {}
        allowed = set(["1","2","3","4","5","6","7","8","9","."])
        for i in range(9):
            for j in range(9):
                # print("--->" , i , j)
                item = board[i][j]
                if item not in allowed:
                    return False
                x = drow.get(i , [])
                y = dcol.get(j , [])
                if item in x and item != ".":
                    # print("false 1")
                    return False
                if item in y and item != ".":
                    # print("false 2", dcol)
                    return False
                x.append(item)
                y.append(item)
                drow[i] = x
                dcol[j] = y
                # print("*"*20)
                # print(item)
                uniqid = i * 9 + j
                mod = uniqid % 9
                if uniqid < 27:

                    if mod < 3:
                        strr = "a3"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, "--> 1")
                            return False
                        x.append(item)
                        dsqr[strr] = x

                    elif mod < 6:
                        strr = "a6"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, uniqid , item)
                            return False
                        x.append(item)
                        dsqr[strr] = x
                    else:
                        strr = "a9"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, "--> 3")
                            return False
                        x.append(item)
                        dsqr[strr] = x
                elif uniqid < 54:
                    if mod < 3:
                        strr = "b3"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, "--> 4")
                            return False
                        x.append(item)
                        dsqr[strr] = x

                    elif mod < 6:
                        strr = "b6"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, "--> 5")
                            return False
                        x.append(item)
                        dsqr[strr] = x
                    else:
                        strr = "b9"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, "--> 6")
                            return False
                        x.append(item)
                        dsqr[strr] = x
                else:
                    if mod < 3:
                        strr = "c3"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, "--> 7", dsqr)
                            return False
                        x.append(item)
                        dsqr[strr] = x

                    elif mod < 6:
                        strr = "c6"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, "--> 8")
                            return False
                        x.append(item)
                        dsqr[strr] = x
                    else:
                        strr = "c9"
                        x = dsqr.get(strr , [])
                        if item in x and item != ".":
                            # print("*"*20, "--> 9")
                            return False
                        x.append(item)
                        dsqr[strr] = x
        # print(True)
        return True