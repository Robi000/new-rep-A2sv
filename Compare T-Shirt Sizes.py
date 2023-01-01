

d = {
    "S" : -1,
    "M" : 2,
    "L":3
}
for x in range (int(input())):
    size = input().split()
    if d[size[0][-1]]*size[0].count("X") + d[size[0][-1]] > d[size[1][-1]]*size[1].count("X") + d[size[1][-1]]:
        print(">")
    if d[size[0][-1]]*size[0].count("X") + d[size[0][-1]] < d[size[1][-1]]*size[1].count("X")+ d[size[1][-1]]:
        print("<")
    if d[size[0][-1]]*size[0].count("X") + d[size[0][-1]] == d[size[1][-1]]*size[1].count("X")+ d[size[1][-1]]:
        print("=")
    
