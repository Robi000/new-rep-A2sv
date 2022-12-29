if __name__ == '__main__':
    N = int(input())
    arr = []
    for n in range(N):
        x = input().split()
        ch = x[0]
        if ch == "insert":
            
            arr.insert(int(x[1]), int(x[2]))
        elif ch == "print":
            
            print(arr)
        elif ch == "append":
            
            arr.append(int(x[1]))
        elif ch == "sort":
            
            arr.sort()
        elif ch == "reverse":
            
            arr.reverse()
        elif ch == "remove":
            
            arr.remove(int(x[1]))
        elif ch == "pop":
            arr.pop()
