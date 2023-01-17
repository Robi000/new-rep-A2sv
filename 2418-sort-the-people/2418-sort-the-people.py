class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         if heights[j] < heights[i]:
        #             heights[j] , heights[i] = heights[i] , heights[j]
        #             names[j] , names[i] = names[i] , names[j]
        for i in range(len(heights)):
            mixx = i
            for j in range( i +1 ,len(heights)):
                if heights[j] > heights[mixx]:
                    mixx = j
            if mixx != i:
                    heights[i] , heights[mixx] = heights[mixx] , heights[i]
                    names[i] , names[mixx] = names[mixx] , names[i]
        return names

                    