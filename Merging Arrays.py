i = input()
arr1 = list(map (int , input().split()))
arr2 = list(map (int , input().split()))
 
ans = []
 
i , j = 0 , 0
 
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i += 1
    else:
        ans.append(arr2[j])
        j += 1
 
ans.extend(arr1[i:])
ans.extend(arr2[j:])
 
ans = [str(x) for x in ans ]
print(" ".join(ans))
