for x in range (int(input())):
    price = int(input().split()[1])
    orbit = list(map(int , input().split()))
    print(orbit)
    dic = {}
    for x in orbit:
        dic[x] = dic.get(x , 0) +1
    ans = 0
    for y in dic.keys():
        if dic[y] < price:
            ans += dic[y]
        else:
            ans += price

    print(ans)

