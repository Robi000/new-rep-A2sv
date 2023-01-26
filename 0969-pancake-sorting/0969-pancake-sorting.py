class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        leng = len(arr)
        place = len(arr)
        ans = []
        for i in range(leng):
            # print(arr)
            maxi = arr[place-1]
            maxx = place
            for j in range(place):
                # print(i , j)
                if arr[j] >maxi:
                    maxi = arr[j]
                    maxx = j


            if maxx == 0:
                ans.append(place)
                arr[:place] = arr[:place][::-1]
                place -= 1
                continue

            elif maxx == place:
                place -= 1
                continue
            else:

                place -= 1
                # print(maxx , place)
                ans.append(maxx+1)
                ans.append(place+1)
                arr[0:maxx+1] = arr[0:maxx+1][::-1]
                arr[0:place+1] = arr[0:place+1][::-1]
        return (ans)