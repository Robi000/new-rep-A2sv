num = input()
num2 = set(map(int, input().split(" ")))
num = input()
num3 = set(map(int, input().split(" ")))

print (len(num2.union(num3)))
