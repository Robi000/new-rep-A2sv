n1 , n2 = list(map(int , input().split()))
arr1 = list(map(int , input().split()))
arr2 = list(map(int , input().split()))
j = 0
ans= []
for i in arr2:
    while  j < n1:
        if arr1[j] < i:
            j += 1
        else:
            break
    ans.append(j)
 
print(*ans)
